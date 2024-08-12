import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "suhas675g@gmail.com"
password = "iecbujgrlhtuiehc"

receiver = "suhas675g@gmail.com"
context = ssl.create_default_context()

message = "Hello how are you suhas?"

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
