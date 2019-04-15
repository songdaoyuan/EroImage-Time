# -*- coding: utf-8 -*-
import os
import re

import requests
from bs4 import BeautifulSoup

PixivMaleLike = 'https://www.pixiv.net/ranking.php?mode=male'
PixivMakleLike_R18 = 'https://www.pixiv.net/ranking.php?mode=male_r18'
PixivMaleLikeLogin = r'https://accounts.pixiv.net/login?return_to=http%3A%2F%2Fwww.pixiv.net%2Franking.php%3Fmode%3Dmale&source=pc&view_type=page'
PixivLogin_api = 'https://accounts.pixiv.net/api/login?lang=zh'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Referer': 'https://www.pixiv.net/'
}

psession = requests.session()  # psession.cookies
r = psession.get(PixivMaleLikeLogin, headers=header)
content = r.content.decode('utf-8')
postkey = re.findall(r"<input.+?name=\"post_key\".+?>",
                     content)[0].split(" ")[3].split("\"")[1]
print(postkey)
pdata = {
    'pixiv_id': '',
    'password': '',
    'return_to': 'http://www.pixiv.net/',
    'post_key': postkey
}
r = psession.post(PixivLogin_api, headers=header, data=pdata)
print(r.status_code)
r = psession.get(PixivMakleLike_R18, headers=header)
print(r.status_code)
print(psession.cookies)
html = r.content.decode('utf-8')
soup = BeautifulSoup(html, 'lxml')
with open('cache.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

EhNon_nudeCosplay = r'https://e-hentai.org/?f_cats=959&f_search=non-nude&advsearch=1&f_sname=on&f_stags=on&f_sr=on&f_srdd=4&f_spf=&f_spt='
