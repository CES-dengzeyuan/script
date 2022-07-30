import mimetypes
import smtplib
import sys
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import datetime
from email.utils import formataddr

def send_email(name):
    filepath = name
    smtp_server = "smtp.qq.com"
    username = "1418069493@qq.com"
    password = "albnyzusqgenghad"
    sender = "1418069493@qq.com"
    receivers = ['15618348169@163.com']
    EMAIL_FROM_NAME = 'Aria testing'
    time = datetime.datetime.today().strftime("%m-%d %H: %M")
    msg = MIMEMultipart()
    msg.attach(MIMEText("Hi!", 'plain', 'utf-8'))
    msg['From'] = formataddr(pair=(EMAIL_FROM_NAME, sender))
    msg['To'] = ";".join(receivers)
    subject = str(time) + "Aria"
    msg['Subject'] = subject
    data = open(filepath, 'rb')
    ctype, encoding = mimetypes.guess_type(filepath)
    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    file_msg = MIMEBase(maintype, subtype)
    file_msg.set_payload(data.read())
    data.close()
    encoders.encode_base64(file_msg)
    file_msg.add_header('Content-Disposition', 'attachment', filename=name)
    msg.attach(file_msg)
    try:
        server = smtplib.SMTP(smtp_server)
        server.login(username, password)
        server.sendmail(sender, receivers, msg.as_string())
        server.quit()
        print("Success!")
    except Exception as err:
        print("Error!")
if __name__ == "__main__":
    send_email(sys.argv[1])
