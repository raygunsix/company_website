import smtplib, ssl


def send_email(message):
    """ sends message via email """
    host = "smtp.example.com"
    port = 465

    username = "user@example.com"
    password = "password"

    receiver = "user2@example.com"
    context = ssl.create_default_context()

    # with smtplib.SMTP_SSL(host, port, context=context) as server:
    #     server.login(username, password)
    #     server.sendmail(username, receiver, message)

    print(message)
