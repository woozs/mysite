#!/usr/bin/env python
# -*- coding:utf-8 -*-
#version:3.5.0
#author:wuzushun
import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    subject, from_email, to = '来自www.wuzushun.com的测试邮件', 'wuzushun@aliyun.com', 'wzsfighting@163.com'
    text_content = '欢迎访问www.wuzushun.com，这是一个登录系统的练习项目，专注于Python和Django技术的分享！'
    html_content = '<p>欢迎访问<a href="www.wuzushun.com" target=blank>www.wuzushun.com</a>，欢迎访问www.wuzushun.com，这是一个登录系统的练习项目，专注于Python和Django技术的分享！！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()