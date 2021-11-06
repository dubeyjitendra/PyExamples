# SENDING MAIL
# What is SMTP
# POP IMAP
# what is Portocol?

# SMTP 
# SMTP (Simple Mail Transfer Protocol) is a TCP/IP protocol used in sending and receiving e-mail. ... 
#In other words, users typically use a program that uses SMTP for sending e-mail and either POP3 or IMAP
#for receiving e-mail. On Unix-based systems, sendmail is the most widely-used SMTP server for e-mail.


# EHLO
# Extended HELO (EHLO) is an Extended Simple Mail Transfer Protocol (ESMTP) command sent by an email server 
# to identify itself when connecting to another email server to start the process of sending an email. ...
# The EHLO command tells the receiving server it supports extensions compatible with ESMTP

# POP3
# Post Office Protocol version 3 (POP3) is a standard mail protocol used to receive emails 
#from a remote server to a local email client. POP3 allows you to download email messages on
#your local computer and read them even when you are offline

#IMAP
# IMAP (Internet Message Access Protocol) is a standard email protocol that stores email messages on a mail server, but allows the end user to
#view and manipulate the messages as though they were stored locally on the end user's computing device(s).


# First python mail source code
'''import smtplib
message = 'Subject: {}\n\n{}'.format("Test", "Hi ")
fromby="XXXXXXXXXXXXXXXXXXXXX"
to="XXXXXXXXXXXXXXXXXXXXXX"
# Init
mail=smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()
mail.login("XXXXXXXXXXXXXXXXXXXXX","XXXXXXXXXXXXXXXXXXXXX")
mail.sendmail(fromby,to,message)
mail.quit()
print('Mail sent sucessfully')'''


# Mail Subject With Atatchement
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# https://docs.python.org/2/library/email.mime.html

# Ordinarily, you get a message object structure by passing a file or some text to a parser, which parses the text
#and returns the root message object. However you can also build a complete message structure from scratch, or
#even individual Message objects by hand. In fact, you can also take an existing structure and add new Message objects,
#move them around, etc. This makes a very convenient interface for slicing-and-dicing MIME messages.
#You can create a new object structure by creating Message instances, adding attachments and all the appropriate headers manually. 
#For MIME messages though, the email package provides some convenient subclasses to make things easier.

# Whatis MIME
# Multipurpose Internet Mail Extensions (MIME) is an Internet standard that extends the format of email
#to support: Text in character sets other than ASCII. Non-text attachments: audio, video, images, application programs etc.


msg = MIMEMultipart()
msg['From'] = 'XXXXXXXXXXXXXXXXXXXXX'
msg['To'] = 'XXXXXXXXXXXXXXXXXXXXX'
msg['Subject'] = "test mail"
body = "Hi First test mail"

msg.attach(MIMEText(body, 'plain'))
filename = "test2.txt"
attachment = open("test2.txt", "rb")

# MIMEBASE
# This is the base class for all the MIME-specific subclasses of Message . Ordinarily you won't create instances
# specifically of MIMEBase , although you could.

p = MIMEBase('application', 'octet-stream')

# MIMEBase is provided primarily as a convenient base class for more specific ... 
#It should use get_payload() and set_payload() to change the payload to encoded

p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(p)
message = 'Subject: {}\n\n{}'.format("Test", "Hi ")
s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
text=msg.as_string()
s.login("XXXXXXXXXXXXXXXXXXXXX","XXXXXXXXXXXXXXXXXXXXX")
s.sendmail('XXXXXXXXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXXXXXXXX',text)
s.quit()
print('mail sent')
