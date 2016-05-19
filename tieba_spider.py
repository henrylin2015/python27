# /usr/bin/python python2.7
# _*_ coding=utf-8 _*_
import urllib2

def file_write(file_name,txt):
    '''
    文件的写入，把txt写入到file_name文件中
    '''
    #打开文件
    f = open(file_name,'w')
    #写入文件
    f.write(txt)
    #关闭文件
    f.close()

def load_spider(url):
    '''
    通过 url抓取数据
    '''
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}
    req = urllib2.Request(url,headers=headers)
    respose = urllib2.urlopen(req)
    html = respose.read()
    #print url + "   ok"
    return html

def load_pages(url,start_page,end_page):
    '''
    加载也是，拼接url
    '''
    # i = 1  pn = 0
    # i = 2  pn = 50
    # i = 3  pn = 100
    # i = 4  pn = 150
    for i in range(int(start_page),int(end_page) + 1):
        pn = (i - 1) * 50
        myurl = url + str(pn)
        content = load_spider(myurl)
        file_write(str(i)+".html",content)
        print str(i) + ".html 抓取成功！"
        #print myurl

if __name__ == "__main__":
    url = raw_input("请您输入url:")
    #print url
    start_page = raw_input("请您输入开始页数：")
    end_page = raw_input("请您输入结束页数：")
    #print start_page
    #print end_page
    load_pages(url,start_page,end_page)