# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 20:31:26 2018

@author: Harrison
"""

import smtplib

gmail_user = 'harrisonsam2002@gmail.com'
gmail_pass = '************'

sent_from = gmail_user
to = [gmail_user,'nelsondoss@hotmail.com','jeremyvictor007@gmail.com','jebajothipriya@hotmail.com']
subject = 'Sending e-mails witht the help of Python'
body = 'Hi, if you are reading this, just to let you know, this email was sent through Python'

email_text = '''\
From: %s
To: %s
Subject %s

%s
''' % (sent_from, ','.join(to), subject, body)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_user,gmail_pass)
server.sendmail(sent_from, to, email_text)
server.quit()