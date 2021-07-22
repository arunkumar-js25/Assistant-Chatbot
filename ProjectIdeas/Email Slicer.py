import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# your credentials
email = "arun25897@gmail.com"
password = 'h7yeyn2x7u'

def SendMail(email,password,message, TO):
    # the sender's email
    #FROM = "arun25897@gmail.com"
    # the receiver's email
    #TO = "kumaran25897@gmail.com"
    # the subject of the email (subject)
    subject = "Test Mail from Python/n/n" + message

    # initialize the message we wanna send
    msg = MIMEMultipart()
    # set the sender's email
    msg["From"] = email
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
    server.sendmail(email, TO, msg.as_string())

    # terminate the SMTP session
    server.quit()

to_list = input("Enter the Recipient Mail Addresses : ").split(';')
to_list = [x.strip() for x in to_list]
for id in to_list:
    print("UserName: "+id.split('@')[0].ljust(20,' ')+" , Domain: "+id.split('@')[1].ljust(20,' '))

send = input("Do you want send any mail (y/n): ")
if(send in ['y','yes','Y','Yes']):
    message = input("Enter Your Message to Convey: ")
    SendMail(email,password,message,to_list)