from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import aiosmtplib
import markdown


from .models import Mail
from src.config import EMAIL_HOSTNAME, EMAIL_PORT, EMAIL_SENDER, EMAIL_USERNAME,EMAIL_PASSWORD

async def send_email(email: Mail):
    mes = MIMEMultipart()
    mes["From"] = EMAIL_SENDER
    mes["To"] = ", ".join(email.recipients)
    mes["Subject"] = email.topic
    mes.attach(MIMEText(markdown.markdown(email.text).replace("\n", "<br>"), "html"))
    try:
        await aiosmtplib.send(
            mes,
            hostname=EMAIL_HOSTNAME,
            port=EMAIL_PORT,
            username=EMAIL_USERNAME,
            password=EMAIL_PASSWORD,
            start_tls=True
        )
    except:
        pass