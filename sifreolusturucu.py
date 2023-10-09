import random

olasi_karakterler = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

karakter_sayisi = int(input('Şifrenizin karakterinin sayısını giriniz:'))

sifre = ('')

for i in range(karakter_sayisi):
    sifre += random.choice(olasi_karakterler)

print(sifre)



