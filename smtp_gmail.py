import os
import smtplib
import pandas as pd
from email.message import EmailMessage

#df = pd.read_excel('/home/kshgrk/Desktop/GUC/test.xlsx', 'r')

guc_mail = os.environ.get('GUC_MAIL')
guc_pass = os.environ.get('GUC_SMTP_PASS')

recipents = ['dummymail@gmail.com', 'dummymail2@gmail.com', 'dummymail3@gmail.com', 'dummymail4@gmail.com', 'dummymail5@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Testing multiple recepients and HTML'
msg['From'] = guc_mail
msg['TO'] = recipents[i]
msg.set_content('You have html disable that\'s why u r seeing this')

msg.add_alternative("""\
### HTML ###
""", subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(guc_mail, guc_pass)
	smtp.send_message(msg)
