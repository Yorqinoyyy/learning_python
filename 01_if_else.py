# if_else.py

# 1-misol: Juft yoki toq sonni aniqlash
son = 7
if son % 2 == 0:
    print(f"{son} juft son")
else:
    print(f"{son} toq son")
  

# 2-misol: Harorat tekshirish
harorat = 35
if harorat > 30:
    print("Havo juda issiq")
else:
    print("Havo normal")
  

# 3-misol: Imtihon natijasi
ball = 82
if ball >= 90:
    print("A'lo baho")
elif ball >= 70:
    print("Yaxshi baho")
else:
    print("Qoniqarli yoki pastroq")
  

# 4-misol: Login tekshirish
login = "admin"
parol = "12345"

if login == "admin" and parol == "12345":
    print("Xush kelibsiz, admin!")
else:
    print("Login yoki parol xato!")

  
  # 5-misol: .upper(), .title()
  avtolar = ['bmw', 'audi', 'toyota', 'honda'] 
  for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
    if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
        print(avto.upper()) # avto nomini hamma harflarini katta bilan yozadi.
    else: # aks holda ... 
        print(avto.title()) # avto nomini faqat birinchi harfini katta bilan yozadi.
      

# 6-misol:1.Qiymatlarning teng emasligini tekshirish;
ism = input('Ismingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
    print(f"Uzr, {ism.title()} biz Alini kutayapmiz.") # quyidagi xabar chiqadi
else:
    print("Salom, Ali")

# 6-misol: 2.Qiymatlarning teng emasligini tekshirish;
login = input("Login kiriting: ")
if login.lower() == 'admin':
  print("Kechirasiz bunday login kirita olmaysiz")
else:
  print(f"Xush kelibsiz {login.title()}!")


# 7-misol: Sonlarni solishtirish;
yil = int(input("Tug'ilgan yilingizni kiriting:"))
if 2025-yil<18: 
    print(f"Yoshingiz {2025-yil}da ekan.")
    print("Kirish mumkin emas!")
else:
    print("Xush kelibsiz!")
