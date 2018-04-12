#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time    : 2018-04-10 16:56
# @Author  : Gujc
# @File    : dnspod1.py
import json
import urllib3
import requests

login_token = '52689,2d8128176f93dafe36da3403b58228bb'
login_url = "https://dnsapi.cn/Info.Version"
# headers = {"Content-Type": "text/html", "charset": "utf-8"}

class Dnspod(object):
    def __init__(self, login_token, login_url):
        self.login_token = login_token
        self.headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/json", "User-Agent": "dnspod-python/0.01 (im@chuangbo.li; DNSPod.CN API v2.8)"}
        self.s = requests.session()
        self.s.verify = False
        self.data = {
            'login_token': login_token,
            'format': 'json',
            'lang': 'cn',

        }
        self.login_url = login_url

    def login(self):
        req = self.s.post(self.login_url, data=self.data, headers=self.headers, verify=self.s.verify)
        # res = json.loads(req.content)
        # req.encoding = req.apparent_encoding
        print('111')
        print(req.text)

if __name__ == '__main__':

    Dnspod(login_token, login_url).login()