import smtplib

def send_email(subject,message,to):
    to = ["oscar.lopez@onestopgroup.com"]
    subject = "Hola Oscar"
    message = "Prueba de cuerpo de correo"
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('miguelh.espinosa@onestopgroup.com','Municipal22')
        message = 'Subject:{}\n\n{}'.format(subject, message)
        server.sendmail('miguelh.espinosa@onestopgroup.com','oscar.lopez@onestopgroup.com',message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")
