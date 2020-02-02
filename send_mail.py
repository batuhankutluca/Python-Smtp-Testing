import smtplib, ssl

port = 1025  # Your listener port (1025 for the localtest)
smtp_server = "192.168.232.131"
sender_email = "batuhan@batuhan.com"
receiver_email = "some_receiver@domain.com"
#password = ""
message = """\
Subject: Hello there

This is a test message."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    #server.ehlo()  # Can be omitted
    #server.starttls(context=context)
    #server.ehlo()  # Can be omitted
    #server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)