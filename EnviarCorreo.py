import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    sender_email = "miguelh.espinosa@onestopgroup.com"
    receiver_email = "oscar.lopez@onestopgroup.com"
    password = "Municipal22"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Asunto"
    message["From"] = sender_email
    message["To"] = receiver_email

    html = """\
    <html>
        <body>
            <p>Hola,<br>
            Como estas?<br>
            Espero que muy bien, que tengas un buen dia
            </p>
        </body>
    </html>
    """

    html_part = MIMEText(html,"html")
    message.attach(html_part)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
        server.login(sender_email,password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

send_email()
