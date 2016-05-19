# /usr/bin/python python2.3
# _*_ coding=utf-8 _*_
import urllib2

respose = urllib2.urlopen("https://docs.python.org/2.7/library/urllib2.html?highlight=urllib2#module-urllib2")
html = respose.read()
print html
