# /usr/bin/python python2.7
# _*_ coding=utf-8 _*_

import urllib2

url="https://www.baidu.com"

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}

req = urllib2.Request(url,headers=headers)

respose = urllib2.urlopen(req)

html = respose.read()
f = open('text.html','w');

f.write(html)
f.close()
print "ok"