import random


karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifre = int(input("lütfen bir şifre giriniz"))
b = random.choices(0,100)
sifre = []

for i in range(sifre):
    sifre.append(karakterler[b])

print(sifre)
