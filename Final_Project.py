import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()

sender_mail = "refkihidayat29@gmail.com"
password = input(str("Masukkan password : "))

server.login(sender_mail, password)
print("Login sukses")

receiver_mail = input(str("Masukkan alamat email penerima : "))
message = input(str("Masukkan isi pesan : "))

server.sendmail(sender_mail, receiver_mail, message)
print("Pesan terkirim")





