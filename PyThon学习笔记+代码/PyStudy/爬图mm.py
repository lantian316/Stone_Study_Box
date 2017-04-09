# -*- coding: UTF-8 -*-

import urllib
import urllib.request
import re

'''
def gethtml():
    openweb = urllib.request.urlopen('http://www.mmjpg.com/tag/xiuren')
    html = openweb.read().decode('UTF-8')
    print(html)
    return html

x = 0
def getimg(html):
    reimg = re.compile(r'src="(http:\/\/.*?[jpg|png])"')
    listimg = re.findall(reimg, html, flags=0)
    for imgurl in listimg:
        global x
        urllib.request.urlretrieve(imgurl,'img\%s.jpg'%x)
        x += 1
        print ("正在下载%s张图片"%x)
        print(imgurl)

html = gethtml()
getimg(html)
'''
text = "JGood is a handsome boy, he is cool, clever, and so on..."
reimg = re.sub(r'\s+','_',text)
print(reimg)