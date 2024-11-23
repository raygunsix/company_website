import smtplib

host = "smtp.example.com"
port = 465

username = "user@example.com"
password = "password"

receiver = "user2@example.com"
context = ssl.create_default_contect()

# Backslash required when including subject in email text
message = """\
Subject: Inquiry
Hi, how are you?
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
