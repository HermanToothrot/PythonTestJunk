import smtplib, ssl
from email.message import EmailMessage
from Settings import brevo_sender_email, brevo_password, destination_email_address
smtp_server = "smtp-relay.brevo.com"
port = 587
sender_email = brevo_sender_email  # Enter your address
receiver_email = destination_email_address  # Enter receiver address
password = brevo_password

subject = "Python - brevo"

body = """\
Subject: Hi there

This message is sent from Python."""

em=EmailMessage()
em['From'] = sender_email
em['to'] = receiver_email
em['Subject'] = subject

em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.set_debuglevel(1)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, em.as_string())
