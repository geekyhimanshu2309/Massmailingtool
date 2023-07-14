import pandas as p
import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

data = p.read_excel("student.xlsx")
print(type(data))
email_col = data.get("email")
list_of_emails = list(email_col)
print(list_of_emails)

try:
    server = sm.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("entersenderemailaddress","enterpassword")
    from_= "entersenderemailaddress"
    to_=list_of_emails
    message=MIMEMultipart("alternative")
    message['Subject']="This is just testing message"
    message["from"]="entersenderemailaddress"
    html='''
        <html>
        <head>
        
        </head>
        <body>
        <h1>Learning Coding</h1>
        <p>This is just testing para</p>
        <button style="padding:20px;background:green;color:white;">Varify</button>
        
        </body>
        </html>
    '''
    text = MIMEText(html,"html")
    message.attach(text)
    server.send(from_,to_, message.as_string())
    print("message has been sent to the emails")
except Exception as e:
    print(e)
    