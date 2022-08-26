from distutils.command.config import config
from io import BytesIO
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os.path
import base64
from django.conf import settings

def enviar_email(attachment, to_email=""):
    try :
        EMAIL = getattr(settings, 'EMAIL', '')
        if to_email == "" :
            return False
        if attachment.find("data:image/jpeg;base64,") != -1 :
            attachment = attachment[len("data:image/jpeg;base64,"):]
            attach = base64.b64decode(attachment)
            email = EMAIL['ID']
            password = EMAIL['PW']
            subject = '스크린샷 입니다!'
            message = 'This is my message'

            msg = MIMEMultipart()
            msg['From'] = email
            msg['To'] = email
            msg['Subject'] = subject

            msg.attach(MIMEText(message, 'plain'))

            image = MIMEImage(attach, name="screenshot.png")
            msg.attach(image)


            # Attach the attachment to the MIMEMultipart object
            # msg.attach(part)
            
            server = smtplib.SMTP('smtp.naver.com', 587)
            server.starttls()
            server.login(email, password)
            text = msg.as_string()
            server.sendmail(email, to_email, text)
            server.quit()
            return (True)
    except :
        return (False)