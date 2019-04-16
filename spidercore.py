# -*- coding: utf-8 -*-

#pip install -U requests[socks]
import os
import re

import requests
from bs4 import BeautifulSoup

proxyon = False

PixivMaleLike = 'https://www.pixiv.net/ranking.php?mode=male'
PixivMakleLike_R18 = 'https://www.pixiv.net/ranking.php?mode=male_r18'
PixivMaleLikeLogin = r'https://accounts.pixiv.net/login?return_to=http%3A%2F%2Fwww.pixiv.net%2Franking.php%3Fmode%3Dmale&source=pc&view_type=page'
PixivLogin_api = 'https://accounts.pixiv.net/api/login?lang=zh'

def enableproxy(bool):
    proxie = {
        'http': 'socks5://127.0.0.1:1080',
        'https': 'socks5://127.0.0.1:1080'
    }
    if bool:
        return proxie
    else:
        proxie = {}
        return proxie

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Referer': 'https://www.pixiv.net/'
}

psession = requests.session()  # psession.cookies
r = psession.get(PixivMaleLikeLogin, headers=header, proxies = enableproxy(proxyon))
content = r.content.decode('utf-8')
postkey = re.findall(r"<input.+?name=\"post_key\".+?>",
                     content)[0].split(" ")[3].split("\"")[1]
pdata = {
    'pixiv_id': '',
    'password': '',
    'return_to': 'http://www.pixiv.net/',
    'post_key': postkey
}
r = psession.post(PixivLogin_api, headers=header, data=pdata)
if  r.status_code == 200:
    r = psession.get(PixivMakleLike_R18, headers=header, proxies = enableproxy(proxyon))
    html = r.content.decode('utf-8') 
    soup = BeautifulSoup(html, 'lxml') #一页提供了40张色图 
    '''
    <a class="work _work " href="/member_illust.php?mode=medium&amp;illust_id=74191839" target="_blank">
    <a class="work _work multiple " href="/member_illust.php?mode=medium&amp;illust_id=74184804" target="_blank">
    '''
    work_list = []
    i = 0
    for w,wm in zip(soup.find_all(name='a', attrs={"class": "work _work "}), soup.find_all(name='a', attrs={"class": "work _work multiple "})):
        #print(w.attrs['href'])
        work_list.append(w.attrs['href'])
        #print(wm.attrs['href'])
        work_list.append(wm.attrs['href']) 
        '''work_list.append(w.attrs['href'])
        work_list.append(wm.attrs['href'])'''
    work_list = list(map(lambda x: 'https://www.pixiv.net/' + x, work_list))
    print(work_list)
else:
    print('Connect to Pixiv Failed! Please check your proxy.')

EhNon_nudeCosplay = r'https://e-hentai.org/?f_cats=959&f_search=non-nude&advsearch=1&f_sname=on&f_stags=on&f_sr=on&f_srdd=4&f_spf=&f_spt='
