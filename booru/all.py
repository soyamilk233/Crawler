# -*- coding: UTF-8 -*-
import urllib.request
import requests
import random
import re
import time
from contextlib import closing
import os

user_agents = [
    "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
    "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
    "Mozilla/5.0(iPhone;U;CPUiPhoneOS4_3_3likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8J2Safari/6533.18.5",
    "Mozilla/5.0(iPad;U;CPUOS4_3_3likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8J2Safari/6533.18.5"
    ]

myproxies=["220.189.249.80:80","124.248.32.43:80"]

def get_html(url,headers,proxies):
    random_userAget = random.choice(headers)
    random_proxy = random.choice(proxies)
    req = urllib.request.Request(url)
    req.add_header("User-Agent", random_userAget)
    proxy_support = urllib.request.ProxyHandler({"http":random_proxy})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    html = urllib.request.urlopen(req)
    return html.read().decode('utf-8')

def get_list(res, reg):
    reg_img = re.compile(reg)
    return reg_img.findall(res)

def Download(imglist, page, name, num):
    i = 0;
    while(i < len(imglist)):
        a = imglist[i]
        b = num[i]
        mypath = 'G:\\temp\\' + name + '\\' + b + '.' + a[2]
        if(os.path.exists(mypath)):
            print(name + '-page' + str(page)+ '-' + str(num[i]) + ' already done')
            i+=1
            continue
        print(str(i) + ' - ' + mypath)
        cnt = 5;
        while cnt > 0:
            try:
                mp4data = requests.get(a[1], timeout=30).content
            except: #requests.exceptions.ReadTimeout:
                print ('Timeout, try agian')
                cnt-=1
            else:
                with open(mypath, 'wb') as f:
                    f.write(mp4data)
                break;
        else:
            print (name + '-page' + str(page)+ '-' + b + ' Try 5 times, But all failed')
        print(name + '-page' + str(page)+ '-' + b + ' done')
        i+=1
        time.sleep(5)

if __name__ == "__main__":
    who = input("Name:")
    tpath = 'G:\\temp\\' + who
    proto1 = "https://www.sakugabooru.com/post?"
    proto2 = "tags="
    uu = proto1 + proto2 + who
    rr1 = r'\bNobody\b'
    rr2 = r'a class="directlink (smallimg|largeimg)" href="(.+?\.(mp4|png|gif|jpg))"'
    rr3 = r'\bnext_page disabled\b'
    rr4 = r'id="p(\d+?)"'
    html = get_html(uu,user_agents,myproxies)
    list1 = get_list(html, rr1)
    if(len(list1) > 0):
        print("Not Found")
        exit();
    if(not os.path.exists(tpath)):
        os.makedirs(tpath)
    page = 1;
    while True:
        uu = proto1 + "page=" + str(page) + "&" + proto2 + who
        html = get_html(uu,user_agents,myproxies)
        #print(html)
        list2 = get_list(html, rr2)
        list4 = get_list(html, rr4)
        Download(list2, page, who, list4)
        list3 = get_list(html, rr3)
        if(len(list3)>0):
            break;
        page+=1
    print("okk")
