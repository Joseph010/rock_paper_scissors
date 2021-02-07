import random

print("TAŞ/KAĞIT/MAKAS OYUNUNA H.O. - created by \"Yusuf Tamer Akyol\" - V 1.6 ")
print("Bir değer seçiniz : Taş/Kağıt/Makas")

a=0
x=0
y=0


while True:

    while True:
        oyuncu = input(">>")

        if (oyuncu=="taş"):
            break
        elif(oyuncu=="kağıt"):
            break
        elif(oyuncu=="makas"):
            break
        else:
            print("taş, kağıt veya makas yazınız")

    while True:

        if (oyuncu=="taş"):
            print("Siz  :  Taş")
            break
        elif(oyuncu=="kağıt"):
            print("Siz  :  kağıt")
            break
        elif(oyuncu=="makas"):
            print("Siz  :  Makas")
            break





    liste = ["taş","kağıt","makas"]
    robot = random.choice(liste)
    print("Robot: " ,robot)


    if(oyuncu==robot):
        print("\033[1;32;36m             ~~Berabere\033[0;00;00m")
    elif(oyuncu=="taş"):
        if(robot=="kağıt"):
            print("\033[1;32;31m             ~~Kaybettiniz..\033[0;00;00m")
            y+=1
        elif(robot=="makas"):
            print("\033[1;32;32m             ~~Kazandınız\033[0;00;00m")
            x+=1
    elif (oyuncu == "kağıt"):
        if (robot == "taş"):
            print("\033[1;32;32m             ~~Kazandınız\033[0;00;00m")
            x += 1
        elif (robot == "makas"):
            print("\033[1;32;31m             ~~Kaybetiniz...\033[0;00;00m")
            y += 1
    elif (oyuncu == "makas"):
        if (robot == "kağıt"):
            print("\033[1;32;32m             ~~Kazandınız\033[0;00;00m")
            x += 1
        elif (robot == "taş"):
            print("\033[1;32;31m             ~~Kaybettiniz..\033[0;00;00m")
            y+=1

    print("                         Sizin Puanınız:", x)
    print("                         A.I puanı     :", y)
    print("                         Bitirilen Tur: ", a+1, "/7")
    a+=1

    if(a==7):
        break
print("\n~~~~~~~~~~~~~~~~~\n")
if(y==x):
    print("\033[1;32;36mOYUN BERABERE\033[0;00;00m")
elif(x >= y):
    print("\033[1;32;32mOYUNU KAZANIDIZ\033[0;00;00m")
elif(x <= y):
    print("\033[1;32;31mOYUNU KAYBETTİNİZ\033[0;00;00m")
print("OYNADIĞINIZ İÇİN TEŞEKKÜRLER- created by jOSEPH")
emek=input("Emeği Geçenleri görmek için \"x\" komutunu giriniz\n?>" )
if (emek == "x"):
    print("~~~~~~~~~~~~~~~~~~~~~~\n~~Kaptan Kaan Nam~ı Diğer Havalı Jojuk\n~~Ertuğrul Recep Nam~ı Diğer Kocaman\n~~Muhammed Buğra Nam~ı Diğer Elazığlı\n~~~~~~~~~~~~~~~~~~~~~~~\nKodlarda hiç bir yardımları dokunmamış olsalarda yardım ettikleri için teşeķkürler...")