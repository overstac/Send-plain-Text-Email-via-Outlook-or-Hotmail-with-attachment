import smtplib
import email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


sender= "usualhotmailemail@hotmail.com"
receiver= "radoyov923@kahase.com"
password= "parolata112233"

message= MIMEMultipart()
message["From"] = sender
message["To"] = receiver
message["Subject"] = "Hello again!"

body= """
<h2>Hi there!</h2>
There are only two cats flying today!
Let's hope for more!
"""

mimetext= MIMEText(body, "html")
message.attach(mimetext)

server= smtplib.SMTP("smtp.office365.com", 587)
server.starttls()
server.login(sender, password)
message_text= message.as_string()
print(message_text)
server.sendmail(sender, receiver, message_text)
server.quit()