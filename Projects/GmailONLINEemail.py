# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 22:08:38 2018

@author: Harrison
"""

import smtplib

gmail_user = 'harrisonsam2002@gmail.com'  
gmail_password = '*************'

sent_from = gmail_user  
to = ['harrisonsam2002@gmail.com', 'harrisonsam2002@gmail.com']  
subject = 'OMG Super Important Message'  
body = "Hey, what's up?"

email_text = """\  
From: %s  
To: %s  
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)
server.sendmail(sent_from, to, email_text)
server.close()