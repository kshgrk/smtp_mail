import os
import smtplib
#import pandas as pd
from email.message import EmailMessage

### Pandas can be used to read csv/excel files for mail recipients ###
# df = pd.read_csv('<path to file>')

### It is always adviced to use email and password from environment variables for security reasons.
your_mail = os.environ.get('YOUR_MAIL')
your_pass = os.environ.get('YOUR_PASS')

recipients = ['dummymail@gmail.com', 'dummymail2@gmail.com', 'dummymail3@gmail.com', 'dummymail4@gmail.com', 'dummymail5@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Testing multiple recepients and HTML'
msg['From'] = your_mail
msg['TO'] = recipients
msg.set_content('You have html disable that\'s why u r seeing this')

msg.add_alternative("""\
### HTML ###
""", subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(your_mail, your_pass)
	smtp.send_message(msg)
