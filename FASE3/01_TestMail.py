import smtplib
import ssl
import getpass

port = 465  # For SSL
password = getpass.getpass()
message = "Hello world!"

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("test.pc.fcfm@gmail.com", password)
    server.sendmail(sender_email, receiver_email, message)
