import smtplib
from email.utils import make_msgid
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

email_id = 'your_email_here'
pswd = 'your_password_here'

details=["Raunak Kumar","raunakraunak077@gmail.com","9800000000","Software","Hardware","Event","SXC","VIsit my Portfolio Website"]
applicant_name = details[0]
applicant_email = details[1]
applicant_phone = details[2]
applicant_choice1 = details[3]
applicant_choice2 = details[4]
applicant_choice3 = details[5]
applicant_college = details[6]
applicant_essay = details[7]

image_cid = make_msgid(
    domain='https://www.raunakmishra.com.np/assets/images/facebook-logo.png')

msg = MIMEMultipart()

html = '''\
<html>
    <head></head>
    <body>
        <h1 style="color:#500050; text-align: center;">Thank You for interest in us...</h1>
        <h2 style="color: #500050; text-align: center;">Here is the copy of the response you submitted.</h2>
        <div style="color: white; background-color: rgba(22,34,57,0.95); box-shadow: 5px 10px #888888; border-radius: 24px; margin-left:25px; margin-right: 25px; text-align: center; border: 2px solid grey;">
            <h4>Your Name: </h4><p>'''+applicant_name+'''</p>
            <h4>Your Email Address: </h4><p>'''+applicant_email+'''</p>
            <h4>Your Phone Number: </h4><p>'''+applicant_phone+'''</p>
            <hr style="width: 50%;">
            <h4>Department Choice First:</h4><p>'''+applicant_choice1+'''</p>
            <h4>Department Choice Second:</h4><p>'''+applicant_choice2+'''</p>
            <h4>Department Choice Third:</h4><p>'''+applicant_choice3+'''</p>
            <hr style="width: 50%;">
            <h4>College Name:</h4><p>'''+applicant_college+'''</p>
            <h4>Why Join Us?</h4><p>'''+applicant_essay+'''</p>
            <hr>
            <div>
                <h3 style="margin-bottom: 40px;">Feel free to contact us for any queries:</h3>
                <a style="font-size: 24px;cursor: pointer; border: none; border-radius: 15px; box-shadow: 0 9px #999; outline: none; text-align: center; text-decoration: none; color:whitesmoke; background-color:brown; padding: 15px 25px;" href="https://pdscorg.com/#section6">Contact Us</a>
            </div>
        </div>
    </body>
</html>'''

content = ""

msg['Subject'] = 'Application Summary of PDSC Membership Application'
msg['From'] = email_id
msg['To'] = details[1]
part = MIMEText(html, "html")
msg.attach(part)

msgAlternative = MIMEMultipart('alternative')
msg.attach(msgAlternative)
msgText = MIMEText('<br><br><p style="color:#500050;"><b>Follow us on:</b><br><a href="https://www.facebook.com/pdscorg"><img width="35" height="35" src="cid:image_fb"></a>   <a href="https://github.com/pdscorg"><img width="35" height="35" src="cid:image_gh"></a>   <a href="https://www.instagram.com/pdscorg/"><img width="35" height="35" src="cid:image_ig"></a>   <a href="https://www.youtube.com/channel/UCtBAL5IGsN6Hyk_deE2BQOw"><img width="35" height="35" src="cid:image_yt"></a></p>', 'html')
msgAlternative.attach(msgText)
#Attach Images
fp1 = open('D://Innovation//Portfolio Pull request//v2.O//assets//images//facebook-logo.png',
          'rb')  # Read image
msgImage1 = MIMEImage(fp1.read())
fp1.close()
msgImage1.add_header('Content-ID', '<image_fb>')
msg.attach(msgImage1)
fp2 = open('D://Innovation//Portfolio Pull request//v2.O//assets//images//instagram-logo.png',
          'rb')  # Read image
msgImage2 = MIMEImage(fp2.read())
fp2.close()
msgImage2.add_header('Content-ID', '<image_ig>')
msg.attach(msgImage2)
fp3 = open('D://Innovation//Portfolio Pull request//v2.O//assets//images//gitHub-logo.png',
          'rb')  # Read image
msgImage3 = MIMEImage(fp3.read())
fp3.close()
msgImage3.add_header('Content-ID', '<image_gh>')
msg.attach(msgImage3)
fp4 = open('D://Innovation//Portfolio Pull request//v2.O//assets//images//youtube-logo.png',
          'rb')  # Read image
msgImage4 = MIMEImage(fp4.read())
fp4.close()
msgImage4.add_header('Content-ID', '<image_yt>')
msg.attach(msgImage4)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_id, pswd)
    smtp.sendmail(email_id, details[1], msg.as_string())
    smtp.quit()
    print("Email sent successfully...")
