# lists_dicts_files.py
# Day 4: Lists, Dictionaries, and File Handling Examples (18 examples)

# =====================
# 📌 LISTLAR (LISTS)
# =====================

# 1.  Do'stlar ro'yxatini yaratish
friends = ['John', 'Alex', 'Danny', 'Sobirjon', 'Vanya']
print(" Dastlabki do'stlar:", friends)

# 2. Ro'yxatga yangi do'stlarni qo'shish
friends.append('Hasan')
friends.insert(0, 'Husan')      
friends.insert(2, 'Ivan')       
print(" Qo'shilgan do'stlar:", friends)

# 3. Mehmonlar ro'yxatini yaratish (.pop bilan elementlarni olish)
mehmonlar = []
mehmonlar.append(friends.pop(3))  
mehmonlar.append(friends.pop(-1)) 
mehmonlar.append(friends.pop(0))  
print(" Mehmonlar:", mehmonlar)

# 4. 120 dan 1200 gacha bo'lgan juft sonlar ro'yxati
sonlar = list(range(120, 1200, 2))
print(" Juft sonlar:", sonlar[:10], "...")

# 5. Ro'yxatdan 20 ta bosh, o'rtadagi va oxirgi elementlarni chiqarish
print(" Birinchi 20:", sonlar[:20])
print(" O'rtadagi 20:", sonlar[530:550])
print(" Oxirgi 20:", sonlar[-20:])

# 6. Matnlardan iborat ro'yxat – har bir elementni katta harfga o‘zgartirish
def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()

ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)
print(" Ismlar katta harf bilan:", ismlar)

# 7 Ro'yxatdan eng katta va eng kichik sonlarni topish
numbers = [12, 45, 2, 78, 34, 23]
print(" Eng katta son:", max(numbers))
print(" Eng kichik son:", min(numbers))

# 8 Ro'yxatni tartiblash (sort va reverse)
numbers.sort()
print(" Tartiblangan ro'yxat:", numbers)
numbers.reverse()
print(" Teskari tartib:", numbers)

# 9 Foydalanuvchidan ism ro'yxatini olib chiqarish
ismlar = []
print(" 5 ta ism kiriting:")
for i in range(5):
    ismlar.append(input(f"{i+1}-ism: "))
print("Kiritilgan ismlar:", ismlar)

# 10. Foydalanuvchi kiritgan sonlar ro‘yxati, ularni yig‘indisi va o‘rtachasi
sonlar = []
print("5 ta son kiriting:")
for i in range(5):
    sonlar.append(int(input(f"{i+1}-son: ")))
print(f"Yig‘indi: {sum(sonlar)}, O‘rtacha: {sum(sonlar)/len(sonlar)}")

# =====================
# 📌 LUG'ATLAR (DICTIONARIES)
# =====================

# 11 Python izohli lug'ati va kalit so'z orqali izlash
python_izohli_lugati = {
    'integer': "Butun son",
    'float': "O'nlik son",
    'string': "Matn",
    'list': "Ro'yxat",
    'tuple': "O'zgarmas ro'yxat"
}
kalit = input("Kalit so'z kiriting: ").lower()
print(python_izohli_lugati.get(kalit, "Bunday so'z mavjud emas"))

# 12 Lug‘at ichidan barcha kalitlarni chiqarish
print("Lug‘atdagi kalitlar:")
for k in python_izohli_lugati.keys():
    print(k.title())

# 13 Lug‘atdagi qiymatlarni chiqarish
print("Lug‘atdagi qiymatlar:")
for v in python_izohli_lugati.values():
    print(v)

# 14 Lug‘atdagi kalit-qiymat juftliklarini chiqarish
print("Kalit-qiymat juftliklari:")
for k, v in python_izohli_lugati.items():
    print(f"{k} ➡️ {v}")

# =====================
# 📌 FAYLLAR (FILES)
# =====================

# 15 Ro'yxatni faylga yozish
with open("friends.txt", "w") as file:
    for friend in friends:
        file.write(friend + "\n")
print("\n'friends.txt' fayliga yozildi.")

# 16 Fayldan o‘qish
with open("friends.txt", "r") as file:
    content = file.read()
print("\nFayldan o‘qilgan ma'lumot:\n", content)

# 17 Foydalanuvchidan matn kiritib faylga yozish
with open("notes.txt", "w") as file:
    for i in range(3):
        file.write(input(f"{i+1}-izoh: ") + "\n")
print("'notes.txt' fayliga yozildi.")

# 18 Fayldan qatorma-qator o‘qish
with open("notes.txt", "r") as file:
    print("Izohlar:")
    for line in file:
        print(line.strip())
