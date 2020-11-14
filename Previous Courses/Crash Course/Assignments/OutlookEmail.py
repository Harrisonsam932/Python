# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 22:18:54 2018

@author: Harrison
"""
import smtplib

outlook_user = 'nelson_harrison@outlook.com'  
outlook_password = '********!'

sent_from = outlook_user  
to = ['harrisonsam2002@gmail.com']  
subject = 'OMG Super Important Message'  
body = "Hey, what's up?"

email_text = """\  
From: %s  
To: %s  
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

server = smtplib.SMTP_SSL('smtp.office365.com', 465)
server.ehlo()
server.login(outlook_user, outlook_password)
server.sendmail(sent_from, to, email_text)
server.close()