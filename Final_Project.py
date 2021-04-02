import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()

sender_mail = input(str("Masukkan email : "))
password = input(str("Masukkan password : "))

server.login(sender_mail, password)
print("Login sukses")


receiver_list = open("receiver_list.txt", "r")
receiver_mail = [(line.strip()).split() for line in receiver_list]

print(receiver_mail)
subject = input(str("Masukkan subject : "))
message = input(str("Masukkan isi pesan : "))

msg = F"Subject: {subject}\n\n{message}"
for mail in receiver_mail:
    server.sendmail(sender_mail, mail, msg)

print("Pesan terkirim")





