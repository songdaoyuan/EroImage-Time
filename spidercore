# -*- coding: utf-8 -*-
import os
import re

import requests
from bs4 import BeautifulSoup

PixivMaleLikeLogin = r'https://accounts.pixiv.net/login?return_to=http%3A%2F%2Fwww.pixiv.net%2Franking.php%3Fmode%3Dmale&source=pc&view_type=page'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
}

psession = requests.session()  # psession.cookies
r = psession.get(PixivMaleLikeLogin, headers=header)
content = r.content.decode('utf-8')
postkey = re.findall(r"<input.+?name=\"post_key\".+?>",
                     content)[0].split(" ")[3].split("\"")[1]

pdata = {
    'pixiv_id': '',
    'password': '',
    'return_to': 'http://www.pixiv.net/ranking.php?mode=male',
    'post_key': postkey
}

'''r = requests.post(PixivMaleLikeLogin, headers=pheader, cookies = cookie, data=pdata)
html = r.content.decode('utf-8')
print(html)'''

EhNon_nudeCosplay = r'https://e-hentai.org/?f_cats=959&f_search=non-nude&advsearch=1&f_sname=on&f_stags=on&f_sr=on&f_srdd=4&f_spf=&f_spt='
