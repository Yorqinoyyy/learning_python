# 1-misol: Ikki sonni solishtirish
def solishtir(x, y):
    """Ikki sonni solishtiruvchi funksiya"""
    if x > y:
        print(f"{x} > {y}")
    elif x < y:
        print(f"{y} > {x}")
    else:
        print(f"{x} = {y}")

solishtir(10, 20)
solishtir(-9, 12)
solishtir(15, 15)

# 2-misol: Sonning darajasini hisoblash (y uchun standart qiymat = 2)
def daraja(x, y=2):
    """Sonning darajasini hisoblovchi funksiya"""
    print(f"{x} ning {y}-darajasi {x**y} ga teng")

daraja(5, 2)
daraja(6)  # faqat x berilsa y=2 bo'ladi

# 3-misol: Sonning 2-10 ga bo‘linishini tekshirish
def bolinish_alomatlari(son):
    """Sonning 2-10 oralig'idagi sonlarga bo'linishini tekshiradi"""
    for n in range(2, 11):
        if son % n == 0:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")

bolinish_alomatlari(20)

# 4-misol: Mijoz haqida ma'lumot qaytaruvchi funksiya
def mijoz_info(ism, familiya, tyil, tjoy, email='', tel=None):
    """Mijoz haqida ma'lumotlarni lug'at ko'rinishida qaytaradi"""
    mijoz = {
        'ism': ism,
        'familiya': familiya,
        'tyil': tyil,
        'yoshi': 2025 - tyil,
        'tjoy': tjoy,
        'email': email,
        'telefon': tel
    }
    return mijoz

print(mijoz_info('Ali', 'Valiyev', 2000, 'Toshkent', 'ali@gmail.com', '99890xxxxxxx'))

# 5-misol: Mijozlar ro'yxatini shakllantirish
mijozlar = []
while False:  # True qilsangiz foydalanuvchidan ma'lumot so'raydi
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    tyil = int(input("Tug'ilgan yili: "))
    tjoy = input("Tug'ilgan joyi: ")
    email = input("Email: ")
    telefon = input("Telefon raqami: ")
    mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
    javob = input("Davom etasizmi? (ha/yo'q): ")
    if javob.lower() != 'ha':
        break

# 6-misol: Matn ro'yxatidagi so'zlarni bosh harfga o'tkazish
def katta_harf(matnlar):
    """Matn ro'yxatidagi so'zlarni bosh harfga o'tkazadi"""
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()

ismlar = ['ali', 'vali', 'hasan']
katta_harf(ismlar)
print(ismlar)

# 7-misol: Fibonachchi ketma-ketligi
def fibonacci(n):
    """Fibonachchi ketma-ketligidagi sonlar ro'yxatini qaytaradi"""
    sonlar = []
    for x in range(n):
        if x < 2:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1] + sonlar[x-2])
    return sonlar

print(fibonacci(10))

# 8-misol: Sonlar yig'indisini qaytaruvchi funksiya
def yigindi(sonlar):
    """Ro'yxatdagi sonlar yig'indisini qaytaradi"""
    return sum(sonlar)

print(yigindi([10, 20, 30]))

# 9-misol: Minimal qiymatni topish
def min_son(sonlar):
    """Ro'yxatdagi eng kichik sonni topadi"""
    return min(sonlar)

print(min_son([23, 5, 9, 12]))

# 10-misol: Kvadratlar ro'yxatini tuzish
def kvadratlar(sonlar):
    """Berilgan sonlar ro'yxatining kvadratlarini qaytaradi"""
    return [son**2 for son in sonlar]

print(kvadratlar([2, 4, 6]))

# 11-misol: Juft sonlarni qaytaruvchi funksiya
def juft_sonlar(sonlar):
    """Ro'yxatdan faqat juft sonlarni qaytaradi"""
    return [son for son in sonlar if son % 2 == 0]

print(juft_sonlar([1, 2, 3, 4, 5, 6]))

# 12-misol: Sonlarni darajaga oshirish
def darajalar(sonlar, daraja=2):
    """Ro'yxatdagi sonlarni berilgan darajaga oshiradi"""
    return [son**daraja for son in sonlar]

print(darajalar([1, 2, 3, 4], 3))

# 13-misol: Ismlarni tozalash (strip)
def tozalash(ismlar):
    """Ism ro'yxatidagi bo'sh joylarni olib tashlaydi"""
    return [ism.strip() for ism in ismlar]

print(tozalash([' Ali ', ' Vali  ', 'Hasan']))
