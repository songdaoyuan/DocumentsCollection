# -*- coding: utf-8 -*-
import csv
import os
import time
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
}


if not os.path.exists('txt'):
    os.mkdir('txt')

def gettophost(url):
    host = urlparse(url).netloc
    p = host.find('.', 0, len(host))
    th = host[p+1:-1] + host[-1]
    if th in ['weibo.cn', 'csdn.net', 'cnblogs.com']:
        return host
    else:
        return th


def nothing(finish, number):
    textfilename = number + '.txt'
    with open(os.path.join('txt/', textfilename), 'w', encoding=('utf-8')) as f:
        if finish:
            f.write('')
        else:
            f.write('没写')


def blog_csdn(url, number):
    session  = requests.session()
    r = session.get(url, headers=header)
    soup = BeautifulSoup(r.content.decode('utf-8'), 'lxml')
    textfilename = number + '.txt'
    for div in soup.find_all(name='div', attrs={'id': 'content_views'}, limit=1):
        with open(os.path.join('txt/', textfilename), 'w', encoding=('utf-8')) as f:
            f.write(div.get_text().strip())


def bbs_csdn(url, number):
    session = requests.session()
    r = session.get(url, headers=header)
    soup = BeautifulSoup(r.content.decode('utf-8'), 'lxml')
    textfilename = number + '.txt'
    for div in soup.find_all(name='div', attrs={'class': 'post_body_min_h'}, limit=1):
        for js in div.find_all('script'):
            bbs_csdn_article = div.get_text()
            bbs_csdn_article = bbs_csdn_article.replace(js.get_text(), '').strip()
    with open(os.path.join('txt/', textfilename), 'w', encoding=('utf-8')) as f:
        f.write(bbs_csdn_article)

def cnblogs(url, number):
    session = requests.session()
    r = session.get(url, headers=header)
    soup = BeautifulSoup(r.content.decode('utf-8'), 'lxml')
    textfilename = number + '.txt'
    for div in soup.find_all(name='div', attrs={'id': 'cnblogs_post_body'}):
        with open(os.path.join('txt/', textfilename), 'w', encoding=('utf-8')) as f:    
            f.write(div.get_text())


def zybuluo(url, number):
    session = requests.session()
    r = session.get(url, headers=header)
    soup = BeautifulSoup(r.content.decode('utf-8'), 'lxml')
    textfilename = number + '.txt'
    for div in soup.find_all(name='div', attrs={'id': 'wmd-preview'}):
        with open(os.path.join('txt/', textfilename), 'w', encoding=('utf-8')) as f:
            f.write(div.get_text())


def bokee(url, number):
    session = requests.session()
    r = session.get(url, headers=header)
    soup = BeautifulSoup(r.content.decode('utf-8'), 'lxml')
    textfilename = number + '.txt'
    with open(os.path.join('txt/', textfilename), 'w', encoding=('utf-8')) as f:
        if url.find('i.bokee', 0, len(url)) == -1:
            for div in soup.find_all(name='div', attrs={'class': 'txt clearfix'}):
                f.write(div.get_text())
        else:
            for div in soup.find_all(name='div', attrs={'class': 'cont'}):
                f.write(div.get_text())


def sohu(url, number):
    session = requests.session()
    r = session.get(url, headers=header)
    soup = BeautifulSoup(r.content.decode('gbk'), 'lxml')
    textfilename = number + '.txt'
    for div in soup.find_all(name='div', attrs={'id': 'main-content'}):
        with open(os.path.join('txt/', textfilename), 'w', encoding=('utf-8')) as f:    
            f.write(div.get_text().replace('阅读(?)评论(0)编辑删除', '').strip())


def sina(url, number):
    #唯一的一篇新浪博客没有访问权限
    textfilename = number + '.txt'
    with open(os.path.join('txt/', textfilename), 'w', encoding=('utf-8')) as f:
        f.write('')


def lofter(url, number):
    session = requests.session()
    r = session.get(url, headers=header)
    soup = BeautifulSoup(r.content.decode('utf-8'), 'lxml')
    textfilename = number + '.txt'
    for div in soup.find_all(name='div', attrs={'class': 'text'}):
        with open(os.path.join('txt/', textfilename), 'w', encoding=('utf-8')) as f:
            f.write(div.get_text().strip())


def jianshu(url, number):
    session = requests.session()
    r = session.get(url, headers=header)
    soup = BeautifulSoup(r.content.decode('utf-8'), 'lxml')
    textfilename = number + '.txt'
    for div in soup.find_all(name='div', attrs={'class': 'show-content-free'}):
        with open(os.path.join('txt/', textfilename), 'w', encoding=('utf-8')) as f:
            f.write(div.get_text().strip())


def zhihu(url, number):
    session = requests.session()
    r = session.get(url, headers=header)
    soup = BeautifulSoup(r.content.decode('utf-8'), 'lxml')
    textfilename = number + '.txt'
    for div in soup.find_all(name='div', attrs={'class': 'RichText ztext Post-RichText'}):
        with open(os.path.join('txt/', textfilename), 'w', encoding=('utf-8')) as f:
            f.write(div.get_text())


def weibo(url, number):
    session = requests.session()
    r = session.get(url, headers=header)
    soup = BeautifulSoup(r.content.decode('utf-8'), 'lxml')
    textfilename = number + '.txt'
    for obj in soup.find_all(name='object', attrs={'id': 'newsArticle'}):
        with open(os.path.join('txt/', textfilename), 'w', encoding=('utf-8')) as f:    
            f.write(obj.get_text().strip())


def m_weibo(url, number):
    #已经无法在浏览器中打开,需要使用weibo客户端
    textfilename = number + '.txt'
    with open(os.path.join('txt/', textfilename), 'w', encoding=('utf-8')) as f:    
        f.write('')


csvfile = 'All_Data_Original.csv'  # edit this attr to the file name you need
with open(csvfile) as f:
    reader = csv.reader(f)
    head_col = next(reader)
    for col in reader:
        # col[18] = Link(May including something useless), col[19] = Student name
        sourcelink = col[18]
        keystr = 'http'
        position = sourcelink.find(keystr, 0, len(sourcelink))
        if position == -1:
            print('序号' + str(reader.line_num - 1) + col[19] + '没写')
            nothing(False, str(reader.line_num - 1))
        else:
            link = sourcelink[position:-1] + sourcelink[-1]
            # print('序号'+ str(reader.line_num - 1) + col[19] + '的作品链接' + link)
            tophost = gettophost(link)
            # print(tophost)
            if tophost == 'bbs.csdn.net':
                bbs_csdn(link, str(reader.line_num - 1))
                time.sleep(2.5)
            elif tophost == 'blog.csdn.net':
                blog_csdn(link, str(reader.line_num - 1))
                time.sleep(2.5)
            elif tophost == 'm.weibo.cn':
                m_weibo(link, str(reader.line_num - 1))
            elif tophost == 'media.weibo.cn':
                print('调用media.weibo解析器')
                nothing(True, str(reader.line_num - 1))
            elif tophost == 'weibo.cn':
                weibo(link, str(reader.line_num - 1))
            elif tophost == 'zybuluo.com':
                zybuluo(link, str(reader.line_num - 1))
            elif tophost == 'blog.sohu.com':
                sohu(link, str(reader.line_num - 1))
            elif tophost == 'bokee.com':
                bokee(link, str(reader.line_num - 1))
            elif tophost == 'zhihu.com':
                zhihu(link, str(reader.line_num - 1))
            elif tophost == 'lofter.com':
                lofter(link, str(reader.line_num - 1))
            elif tophost == 'home.cnblogs.com':
                nothing(True, str(reader.line_num - 1))
            elif tophost == 'www.cnblogs.com':
                cnblogs(link, str(reader.line_num - 1))
                time.sleep(2.5)
            elif tophost == 'jianshu.com':
                jianshu(link, str(reader.line_num - 1))
            elif tophost == 'sina.cn':
                sina(link, str(reader.line_num - 1))
            elif tophost == 'wenjuan.com':
                nothing(True, str(reader.line_num - 1))
            else:
                print('无法解析wps在线文档,请手动保存')
                nothing(True, str(reader.line_num - 1))
