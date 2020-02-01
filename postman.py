import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from jinja2 import Environment, FileSystemLoader

# import ssl

SMTP_SERVER = "localhost"
SMTP_PORT = 1025
SMTP_SENDER = "me@test.com"
SMTP_PASSWORD = "test"

JINJA = Environment(loader=FileSystemLoader("./templates"))


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


def send(receiver: str, template: str):
    send_email(receiver,
               JINJA.get_template(template + ".plain.jinja2").render(),
               JINJA.get_template(template + ".html.jinja2").render())


def send_welcome_email(receiver: str):
    send(receiver, "welcome")
