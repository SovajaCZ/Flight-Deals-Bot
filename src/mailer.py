import os
import smtplib
from email.mime.text import MIMEText


def send_email(subject, body, recipient):
    """
    Odeslání emailu přes SMTP Seznam.cz
    """

    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")

    if not smtp_user or not smtp_password:
        print("SMTP credentials nejsou nastaveny")
        return

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = smtp_user
    msg["To"] = recipient

    try:
        print(f"Odesílám email na {recipient}...")

        with smtplib.SMTP_SSL("smtp.seznam.cz", 465) as server:
            server.login(smtp_user, smtp_password)
            server.send_message(msg)

        print("Email úspěšně odeslán")

    except Exception as e:
        print(f"Chyba při odesílání emailu: {e}")
