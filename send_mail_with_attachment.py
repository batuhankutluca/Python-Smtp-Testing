import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 1025  # Your listener port (1025 for the localtest)
smtp_server = "192.168.232.131"

subject = "Test e-mail header"
body = "Test e-mail body"
sender_email = "batuhan@batuhan.com"
receiver_email = "some_receiver@domain.com"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email

message.attach(MIMEText(body, "plain"))

filename = "/root/a.txt"

with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)

part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

message.attach(part)
text = message.as_string()

with smtplib.SMTP(smtp_server, port) as server:
    server.sendmail(sender_email, receiver_email, text)