# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 20:31:26 2018

@author: Harrison
"""

import smtplib
import getpass


gmail_user = input("Enter email: ")
gmail_pass = getpass.getpass(prompt="Enter password: ")

sent_from = gmail_user
to = [gmail_user, 'nelson_harrison@outlook.com']
subject = input("Enter subject: ")
body = input("Enter body: ")

email_text = '''\
From: %s
To: %s
Subject %s

%s
''' % (sent_from, ','.join(to), subject, body)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_user, gmail_pass)
server.sendmail(sent_from, to, email_text)
server.quit()
