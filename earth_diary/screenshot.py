import smtplib
from PIL import ImageGrab
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os.path

def enviar_email():
    email = 'email'
    password = 'password'
    subject = 'This is the subject'
    message = 'This is my message'
    file_location = 'ss1.jpg'

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    # Setup the attachment
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb").read()
    image = MIMEImage(attachment, name=filename)
    msg.attach(image)


    # Attach the attachment to the MIMEMultipart object
    # msg.attach(part)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, email, text)
    server.quit()

def main():
    imagem = ImageGrab.grab()
    imagem.save('ss1.jpg', 'jpeg')
    enviar_email()

if __name__ == '__main__':
    main()