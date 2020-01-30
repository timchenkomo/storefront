import smtplib
# import ssl

SMTP_SERVER = "localhost"
SMTP_PORT = 1025
SMTP_SENDER = "me@test.com"
SMTP_PASSWORD = "test"


def send_email(receiver: str, message: str):
    """End email to a specified address."""
    # context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        # server.starttls(context=context)  # Secure the connection
        # server.login(SMTP_SENDER, SMTP_PASSWORD)

        server.sendmail(SMTP_SENDER, receiver, message)
    except smtplib.SMTPException as exception:
        print(exception)
    finally:
        server.quit()
