import smtplib
import os

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()

sender_mail = "refkihidayat29@gmail.com"
password = input(str("Masukkan password : "))

server.login(sender_mail, password)
print("Login sukses")

receiver_list = open("receiver_list.txt", "r")
receiver_mail = len(receiver_list.read())

subject = input(str("Masukkan subject : "))
message = input(str("Masukkan isi pesan : "))

msg = F"Subject: {subject}\n\n{message}"

server.sendmail(sender_mail, receiver_mail, msg)
print("Pesan terkirim")





