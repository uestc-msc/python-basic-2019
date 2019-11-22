#! /usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import platform
import time
import random
import shutil
import ctypes
import requests
from urllib import request

############################# Basic Configuration ##############################
# path to store the Picture cache
path = os.path.join(os.path.expanduser("~"), "Pictures/Pixiv-WallPaper-Cache")
# time period to change the Picture (minutes)
period = 1
# api link
url = "https://api.pixivic.com/illust?w_h_ratio=16-9&minWidth=1080&range=0.0001&isR18=false&getDetail=true"
################################################################################

# detect if your platform is Windows or Linux
system = platform.system()
# anti-anti-crawler: User-Agent
userAgents = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
]

while True:
    req = request.Request(url, headers={"User-Agent": random.choice(userAgents)})
    try:
        realURL = request.urlopen(req).geturl()
    except:
        print('Error happened, trying again to get URL of the picture')
        continue
    print('Got URL of the picture')
    picName = realURL[(realURL.find('?id') + 4):realURL.find('&title')]
    # skip broken image
    if picName.find('sina') != -1:
        continue
    picPath = os.path.join(path, (picName + ".jpg"))
    # detect if the cache folder exist, if not, make one
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        # detect if there is cache pictures, if so, delete them
        shutil.rmtree(path)
        os.system('mkdir ' + path)
    #  request.urlretrieve(realURL, picPath)
    picture = requests.get(realURL)
    with open(picPath, 'wb') as file:
        file.write(picture.content)
    print('Picture downloaded')
    if system == 'Windows':
        # set pic as wallpaper
        ctypes.windll.user32.SystemParametersInfoW(20, 0, picPath, 0)
    if system == 'Linux':
        # set pic as wallpaper
        # the first command is to make sure the script is able to change gsettings
        os.system('export GIO_EXTRA_MODULES=/usr/lib/x86_64-linux-gnu/gio/modules/ && gsettings set org.gnome.desktop.background picture-uri "file://%s"' % (picPath))
    print('Wallpaper updated')
    print('waiting for %d more minutes' % (period))
    time.sleep(period * 60)  # time period to change the Pic
