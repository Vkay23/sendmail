import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv  # pip install python-dotenv

PORT = 587
EMAIL_SERVER = "smtp.gmail.com"  # Adjust server address, if you are not using @outlook

# Load the environment variables
current_dir = Path(
    __file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# Read environment variables
sender_email = os.getenv("vamseerathod57@gmail.com")
password = os.getenv()#enter your password in this format("a1b2c3d4e5g6h7i8") https://www.lifewire.com/get-a-password-to-access-gmail-by-pop-imap-2-1171882


def send_email(subject, receiver_email, name, due_date):
  # Create the base text message.
  msg = EmailMessage()
  msg["Subject"] = "Happy Birthday🎉🎉🎁"
  msg["From"] = formataddr(("Birthday Greetings.", f"{sender_email}"))
  msg["To"] = receiver_email
  msg["BCC"] = sender_email

  msg.set_content(f"""\
        Hi 👋{name},
        I hope you are enjoying your birthday🎊.
        This is to tell you how special your birthday is.🎉🎉🎁
        Happy Birthday!
        Best regards🧧
        Vk
        """)
  # Add the html version.  This converts the message into a multipart/alternative
  # container, with the original text message as the first part and the new html
  # message as the second part.
  msg.add_alternative(
      f"""\
    <html>
      <body>
        <p>Hi 👋{name},</p>
        <p>I hope you are enjoying your birthday🎊.</p>
        <p>This is to tell you how special your birthday is.</p>
        <p>Happy Birthday!</p>
        <p>Best regards🧧</p>
        <p>Vk</p>
      </body>
    </html>
    """,
      subtype="html",
  )

  with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
    server.starttls()
    server.login('vamseerathod57@gmail.com', password)
    server.sendmail('vamseerathod57@gmail.com', receiver_email,
                    msg.as_string())


if __name__ == "__main__":
  send_email(
      subject="Birthday Greetings",
      name="user",
      receiver_email="vamseerathod4@gmail.com",
      due_date="11, Aug 2022",
      # invoice_no="INV-21-12-009",
      # amount="5",
  )
