import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = "qsx459@gmail.com"
receiver = ["work240729@gmail.com","qsx459@gmail.com"]
password = "tbmj vpqf msll zvke"
for i in receiver:

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = i
    msg["Subject"] = Header("Test send email","utf-8").encode()

    body = "美女下午好"

    msg_text=MIMEText(body)
    msg.attach(msg_text)
    c = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=c) as server:
      server.login(sender,password)
      server.sendmail(sender,i,msg.as_string())
print("success send email")