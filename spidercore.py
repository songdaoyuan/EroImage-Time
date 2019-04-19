# -*- coding: utf-8 -*-

# pip install -U requests[socks]
import os
import re

import requests
from bs4 import BeautifulSoup

'''proxyon = False

PixivMaleLike = 'https://www.pixiv.net/ranking.php?mode=male'
PixivMakleLike_R18 = 'https://www.pixiv.net/ranking.php?mode=male_r18'
PixivMaleLikeLogin = 'https://accounts.pixiv.net/login?return_to=http%3A%2F%2Fwww.pixiv.net%2Franking.php%3Fmode%3Dmale&source=pc&view_type=page'
PixivLogin_api = 'https://accounts.pixiv.net/api/login?lang=zh'

#NOT WORK SOMETIMES
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

pheader = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Referer': 'https://www.pixiv.net/',
    'Host': 'www.pixiv.net',
    'Connection': 'keep-alive'
}

print(requests.get('http://ifconfig.me/ip').text)
psession = requests.session()  # psession.cookies
r = psession.get(PixivMaleLikeLogin, headers=pheader, proxies = enableproxy(proxyon)) #add this attr if you use  proxy : proxies = enableproxy(proxyon)
content = r.content.decode('utf-8')
postkey = re.findall(r"<input.+?name=\"post_key\".+?>",
                     content)[0].split(" ")[3].split("\"")[1]
pdata = {
    'pixiv_id': '953801092@qq.com',
    'password': '',
    'return_to': 'http://www.pixiv.net/',
    'post_key': postkey
}
r = psession.post(PixivLogin_api, headers=pheader, data=pdata, proxies = enableproxy(proxyon))
if  r.status_code == 200:
    r = psession.get(PixivMakleLike_R18, headers=pheader) #add this attr if you use  proxy : proxies = enableproxy(proxyon)
    phtml = r.content.decode('utf-8') 
    psoup = BeautifulSoup(phtml, 'lxml') #一页提供了40张色图 
    #<a class="work _work " href="/member_illust.php?mode=medium&amp;illust_id=74191839" target="_blank">
    #<a class="work _work multiple " href="/member_illust.php?mode=medium&amp;illust_id=74184804" target="_blank">
    work_list = []
    i = 0
    for w,wm in zip(psoup.find_all(name='a', attrs={"class": "work _work "}), psoup.find_all(name='a', attrs={"class": "work _work multiple "})):
        #print(w.attrs['href'])
        work_list.append(w.attrs['href'])
        #print(wm.attrs['href'])
        work_list.append(wm.attrs['href']) 
    work_list = list(map(lambda x: 'https://www.pixiv.net/' + x, work_list))
    print(work_list)
else:
    print('Connect to Pixiv Failed! Please check your proxy.')
'''
EhForumsAccount = 'https://forums.e-hentai.org/index.php?act=Login&CODE=00'
Ehlogin_api = 'https://forums.e-hentai.org/index.php?act=Login&CODE=01'
EhNon_nudeCosplay = r'https://e-hentai.org/?f_cats=959&f_search=non-nude&advsearch=1&f_sname=on&f_stags=on&f_sr=on&f_srdd=4&f_spf=&f_spt='
eheader = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Host': 'forums.e-hentai.org',
    'Referer': 'https://forums.e-hentai.org/index.php?act=Login&CODE=00'
}

exheader = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Host': 'https://exhentai.org/',
    'Referer': 'https://forums.e-hentai.org/index.php?act=Login&CODE=00',
    'Accept': 'image/webp,*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}
edata = {
    'UserName': 'symboll',
    'PassWord': '',
    'CookieDate': '1',
    'referer': 'https://exhentai.org/'
}
esession = requests.session()
r = esession.get(EhForumsAccount, headers=eheader)
r = esession.post(Ehlogin_api, headers=eheader, data=edata)
'''ecookies = requests.utils.dict_from_cookiejar(esession.cookies)
for key, value in ecookies.items():
	esession.cookies.set(key, value, domain='.exhentai.org', path='/')'''
print(esession.cookies)
excookie = {
    'BL_D_PROV': 'undefined',
    'BL_T_PROV': 'undefined',
    'igneous': '3a5db5854',
    'ipb_member_id': '2161404',
    'ipb_pass_hash': '',
    'lv': '1552390687-1552554415',
    's': '94cddf74d',
    'sk': '3kv2yt03d23gsjkx90c155x1p1xc'
}
r = requests.get('https://exhentai.org/g/1400431/5db103df11/', headers=exheader, cookies=excookie)
print(r.content.decode('utf-8'))
