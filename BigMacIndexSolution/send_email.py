import smtplib
from email.message import EmailMessage

def send_email(sender, receiver, password):
    msg = EmailMessage()
    msg.set_content('Monika Kusiak - Dane zostały umieszczone na s3')

    msg['Subject'] = 'Monika Kusiak - Dane zostały umieszczone na s3'
    msg['From'] = f"{sender}"
    msg['To'] = f"{receiver}"

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(f"{sender}", f"{password}")
    server.send_message(msg)
    server.quit()


