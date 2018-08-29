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
    #模拟浏览器进行访问
    req = urllib.request.Request(url)
    req.add_header("User-Agent", random_userAget)
    #使用ip代理进行访问
    proxy_support = urllib.request.ProxyHandler({"http":random_proxy})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    html = urllib.request.urlopen(req)
    return html.read().decode('utf-8')

URL = ""

if __name__ == "__main__":
    text = get_html(URL,user_agents,myproxies)
