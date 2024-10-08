import smtplib
import ssl


def send_email():
    # common host for sending email using smtp
    host = "smtp.gmail.com"
    port = 465

    # app key along with sender information
    username = "suhas675g@gmail.com"
    password = "iecbujgrlhtuiehc"

    # receiver address and context
    receiver = "suhas675g@gmail.com"
    context = ssl.create_default_context()
    message = "Hello how are you suhas?"
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


send_email()