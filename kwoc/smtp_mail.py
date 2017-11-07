import os
import sys
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#Next, log in to the server
#print(str(os.environ['PASSWD']))
server.login(str(os.environ['EMAIL']), str(os.environ['PASSWD']))

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "Kharagpur Winter of Code <kwoc@kossiitkgp.in>"
you = sys.argv[1]

msg = MIMEMultipart('alternative')
msg['Subject'] = "Registration successful"
msg['From'] = me
msg['To'] = you

#Send the mail
html ="""\
<html>
  <head></head>
  <body>
    <p>Hello mentor!<br>
       Welcome to KWoC!<br>
       Please read the manual <a href="https://kwoc.kossiitkgp.in/static/files/KWoCMentorManual.pdf">here</a>.
    </p>
  </body>
</html>
""" # The /n separates the message from the headers

#part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

#msg.attach(part1)
msg.attach(part2)

server.sendmail(me, you, msg.as_string())
print("Sent")
