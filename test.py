from ultron_functions import *
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
def emailscript(email,subject,massage,filename,filelocation):
    fromaddr = "ultronai2020@gmail.com"
    toaddr = email
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = toaddr 
    msg['Subject'] = subject
    body = massage
    msg.attach(MIMEText(body, 'plain'))
    attachment = open(filelocation, "rb") 
    p = MIMEBase('application', 'octet-stream') 
    p.set_payload((attachment).read()) 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(fromaddr, "ultronpersonal2020") 
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text) 
    s.quit()
def emailscript1(email,subject,massage):
    fromaddr = "ultronai2020@gmail.com"
    toaddr = email
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = toaddr 
    msg['Subject'] = subject
    body = massage
    msg.attach(MIMEText(body, 'plain'))
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(fromaddr, "ultronpersonal2020") 
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text) 
    s.quit()