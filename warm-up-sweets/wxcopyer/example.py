#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# 微信转载图片本地保存及链接转换小能手

import sys
import os
import re
from urllib.request import urlretrieve

os.chdir(sys.path[0])

filePath = sys.argv[1]
saveFolder = re.sub('.html', '', filePath)
folderName = os.path.basename(saveFolder)
# make the directory for asset images, nothing happens if it exists.
os.makedirs(saveFolder, exist_ok=True)
# a dic to record the mapping of wechat image links and local image links so
# that the link mappings can be reused.
imageLinks = {}

# pageCache is only readable, while page is only writeable (cover)
with open(filePath) as pageCache:
    lines = pageCache.readlines()
with open(filePath, "w") as page:
    for lineNumber, line in enumerate(lines):
        # skip writing if the is the line of "data-src"
        if not re.search(r'\A\s*data-src', line):
            # if wechat image links are found, if are new ones, save and replace
            # them, if are known ones, replace them
            # if re.search(r'\A\s*src', line):
            if re.search('https://mmbiz.qpic.cn', line):
                # imageURL = line[line.find('https://mmbiz.qpic.cn'):-2]
                imageURL = re.search(r'https://mmbiz.qpic.cn.+?wx_fmt=.+?(?=")', line).group()
                if imageURL not in imageLinks:
                    match = re.search(r'(?<=wx_fmt=)(.+?)(?=&|")', imageURL)
                    if not match:
                        match = re.search(r'(?<=wx_fmt=).+', imageURL)
                    extensionName = match.group()
                    picName = str(lineNumber) + '.' + extensionName
                    savePath = saveFolder + '/' + picName
                    urlretrieve(imageURL, savePath)
                    imageLinks[imageURL] = savePath
                else:
                    savePath = imageLinks[imageURL]
                    picName = os.path.basename(savePath)
                line = re.sub(re.escape(imageURL), os.path.join('.', folderName, picName), line)
            page.write(line)
