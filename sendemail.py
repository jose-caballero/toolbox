#!/usr/bin/env python


import smtplib

try:
        from email.mime.text import MIMEText
except:
        from email.MIMEText import MIMEText


sender = 'neo@matrix.net' 
serverhost = 'localhost'



to = 'someone@world.com'
cc = ''
subject = '[TEST]'
body = 'this is a test'
message = MIMEText(body)
message['subject'] = subject
message['From'] = sender 
message['To'] = to
message['Cc'] = cc
to = [x.strip() for x in to.split()]


server = smtplib.SMTP(serverhost)
server.sendmail(sender, to, message.as_string())
server.close()

