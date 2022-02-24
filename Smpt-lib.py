import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('p200179@pwr.nu.edu.pk', 'Kalilinix99')
server.sendmail('p200179@pwr.nu.edu.pk', 'dj835048@gmail.com', 'Hi💕dj! I Love ❤️You ')