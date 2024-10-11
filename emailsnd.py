from email.message import EmailMessage
import ssl
import smtplib

email_sender ="YourEmail@gmail.com"
email_password= ""# Provide ur pass here
email_receiver= "YourReceivingEmail@gmail.com"

subject="HEY HEY :)"
body="hey hey hey"
em=EmailMessage()

em["From"]=email_sender
em["To"]=email_receiver
em["Subject"]=subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
    print("Done")
   