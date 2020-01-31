import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# import ssl

SMTP_SERVER = "localhost"
SMTP_PORT = 1025
SMTP_SENDER = "me@test.com"
SMTP_PASSWORD = "test"


def send_email(receiver: str, msg: str, msg_html: str = ""):
    """End email to a specified address."""

    try:
        # context = ssl.create_default_context()
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        # server.starttls(context=context)  # Secure the connection
        # server.login(SMTP_SENDER, SMTP_PASSWORD)

        message = MIMEMultipart("alternative")
        message["Subject"] = "BBT Online"
        message["From"] = SMTP_SENDER
        message["To"] = receiver
        message.attach(MIMEText(msg, "plain"))
        message.attach(MIMEText(msg_html, "html"))

        server.sendmail(SMTP_SENDER, receiver, message.as_string())
    except smtplib.SMTPException as exception:
        print(exception)
    finally:
        server.quit()
