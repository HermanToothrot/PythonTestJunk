import smtplib, ssl
from Settings import gmail_username, gmail_password, destination_email_address, gmail_account_name
from email.message import EmailMessage
smtp_server = "smtp.gmail.com"
port = 465
sender_email = gmail_username  # Enter your address
receiver_email = destination_email_address  # Enter receiver address
password = gmail_password

subject = "Python"

body = """\
Subject: Hi there

This message is sent from Python."""

em=EmailMessage()
em['From'] = f'{gmail_account_name}{sender_email}'
em['to'] = receiver_email
em['Subject'] = subject

em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.set_debuglevel(1)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, em.as_string())
