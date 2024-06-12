import smtplib
from email.message import EmailMessage

fromMy = 'hgreen3041@yahoo.com' # fun-fact: "from" is a keyword in python, you can't use it as variable.. did anyone check if this code even works?
to  = 'hunt3041@gmail.com'
subj='What up dawg'
date='05/25/24'
message_text='Sending an email via python'

msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( fromMy, to, subj, date, message_text )



with smtplib.SMTP(host='smtp.mail.yahoo.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('hgreen3041@yahoo.com', 'Bigdeer3041')
    smtp.sendmail(fromMy, to, msg)
    print('Email sent!')


