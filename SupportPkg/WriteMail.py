import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# your credentials
email = "arun25897@gmail.com"
password = "h7yeyn2x7u"

# the sender's email
FROM = "arun25897@gmail.com"
# the receiver's email
TO   = "kumaran25897@gmail.com"
# the subject of the email (subject)
subject = "Test Mail from Python"

"""
Note: If you're using Gmail account to send,
make sure you turn "Allow less secure apps" to ON, 
although this will make everyone can access your gmail account just with your email and password.
"""

# initialize the message we wanna send
msg = MIMEMultipart()
# set the sender's email
msg["From"] = FROM
# set the receiver's email
msg["To"] = TO
# set the subject
msg["Subject"] = subject
# set the body of the email
text = MIMEText("This email is sent using <b>Python</b> !", "html")
# attach this body to the email
msg.attach(text)


# initialize the SMTP server
# ALL SMTP SERVER and PORT LIST - https://www.arclab.com/en/kb/email/list-of-smtp-and-pop3-servers-mailserver-list.html
server = smtplib.SMTP("smtp.gmail.com", 587)
# connect to the SMTP server as TLS mode (secure) and send EHLO
server.starttls()                                
# login to the account using the credentials
server.login(email, password)
# send the email
server.sendmail(FROM, TO, msg.as_string())
# terminate the SMTP session
server.quit()
