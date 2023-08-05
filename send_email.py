import smtplib, ssl

def send(message):

    host = 'smtp.gmail.com'
    port = 465


    password = 'ybozscygzljmqywa'
    username = 'vuvietdu2003@gmail.com'

    receiver = 'saranghae123578@gmail.com'


    my_context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL(host, port, context = my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message )