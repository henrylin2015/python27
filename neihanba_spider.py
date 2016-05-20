# _*_ coding=utf-8 _*_
import urllib2
import re

class Spider:
    '''
    创建一个爬虫类
    '''
    def __init__(self, url, start_page, end_page):
        '''
        构造函数，初始化时，传递三个参数，url，起始页码，结束页码
        '''
        self.url = url
        print url, start_page, end_page
        self.load_page(self.url)

    def load_page(self, url):
        headers =  {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
        req = urllib2.Request( self.url,  headers = headers)
        response = urllib2.urlopen(req)
        html = response.read()
        #new_html = html.decode('gbk').encode('utf-8')
        ret = self.page_filter(html)
        for item in ret:
            print "==================="
            print item
            print "==================="

    def page_filter(self, content):
        #patt = re.compile(r'<div\s+class=\"text-column-item box box-790\">\w\W+<\/div>')
        patt = re.compile(r'<div.*?class="text-column-item box box-790">(.*?)</div>',re.S)
        html = patt.findall(content)
        return html




if __name__ == "__main__":
    url = "http://www.neihan8.com/article/";
    start_page = 1
    end_page = 10
    myspider = Spider(url, start_page, end_page)