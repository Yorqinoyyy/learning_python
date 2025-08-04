# lists_dicts_files.py
# Day 4: Lists, Dictionaries, and File Handling Examples (18 examples)

# =====================
# 📌 LISTLAR (LISTS)
# =====================

# 1️⃣ Do'stlar ro'yxatini yaratish
friends = ['John', 'Alex', 'Danny', 'Sobirjon', 'Vanya']
print("1️⃣ Dastlabki do'stlar:", friends)

# 2️⃣ Ro'yxatga yangi do'stlarni qo'shish
friends.append('Hasan')
friends.insert(0, 'Husan')      
friends.insert(2, 'Ivan')       
print("2️⃣ Qo'shilgan do'stlar:", friends)

# 3️⃣ Mehmonlar ro'yxatini yaratish (.pop bilan elementlarni olish)
mehmonlar = []
mehmonlar.append(friends.pop(3))  
mehmonlar.append(friends.pop(-1)) 
mehmonlar.append(friends.pop(0))  
print("3️⃣ Mehmonlar:", mehmonlar)

# 4️⃣ 120 dan 1200 gacha bo'lgan juft sonlar ro'yxati
sonlar = list(range(120, 1200, 2))
print("4️⃣ Juft sonlar:", sonlar[:10], "...")

# 5️⃣ Ro'yxatdan 20 ta bosh, o'rtadagi va oxirgi elementlarni chiqarish
print("5️⃣ Birinchi 20:", sonlar[:20])
print("5️⃣ O'rtadagi 20:", sonlar[530:550])
print("5️⃣ Oxirgi 20:", sonlar[-20:])

# 6️⃣ Matnlardan iborat ro'yxat – har bir elementni katta harfga o‘zgartirish
def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()

ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)
print("6️⃣ Ismlar katta harf bilan:", ismlar)

# 7️⃣ Ro'yxatdan eng katta va eng kichik sonlarni topish
numbers = [12, 45, 2, 78, 34, 23]
print("7️⃣ Eng katta son:", max(numbers))
print("7️⃣ Eng kichik son:", min(numbers))

# 8️⃣ Ro'yxatni tartiblash (sort va reverse)
numbers.sort()
print("8️⃣ Tartiblangan ro'yxat:", numbers)
numbers.reverse()
print("8️⃣ Teskari tartib:", numbers)

# 9️⃣ Foydalanuvchidan ism ro'yxatini olib chiqarish
ismlar = []
print("9️⃣ 5 ta ism kiriting:")
for i in range(5):
    ismlar.append(input(f"{i+1}-ism: "))
print("Kiritilgan ismlar:", ismlar)

# 🔟 Foydalanuvchi kiritgan sonlar ro‘yxati, ularni yig‘indisi va o‘rtachasi
sonlar = []
print("🔟 5 ta son kiriting:")
for i in range(5):
    sonlar.append(int(input(f"{i+1}-son: ")))
print(f"Yig‘indi: {sum(sonlar)}, O‘rtacha: {sum(sonlar)/len(sonlar)}")

# =====================
# 📌 LUG'ATLAR (DICTIONARIES)
# =====================

# 11️⃣ Python izohli lug'ati va kalit so'z orqali izlash
python_izohli_lugati = {
    'integer': "Butun son",
    'float': "O'nlik son",
    'string': "Matn",
    'list': "Ro'yxat",
    'tuple': "O'zgarmas ro'yxat"
}
kalit = input("11️⃣ Kalit so'z kiriting: ").lower()
print(python_izohli_lugati.get(kalit, "Bunday so'z mavjud emas"))

# 12️⃣ Lug‘at ichidan barcha kalitlarni chiqarish
print("12️⃣ Lug‘atdagi kalitlar:")
for k in python_izohli_lugati.keys():
    print(k.title())

# 13️⃣ Lug‘atdagi qiymatlarni chiqarish
print("13️⃣ Lug‘atdagi qiymatlar:")
for v in python_izohli_lugati.values():
    print(v)

# 14️⃣ Lug‘atdagi kalit-qiymat juftliklarini chiqarish
print("14️⃣ Kalit-qiymat juftliklari:")
for k, v in python_izohli_lugati.items():
    print(f"{k} ➡️ {v}")

# =====================
# 📌 FAYLLAR (FILES)
# =====================

# 15️⃣ Ro'yxatni faylga yozish
with open("friends.txt", "w") as file:
    for friend in friends:
        file.write(friend + "\n")
print("\n15️⃣ 'friends.txt' fayliga yozildi.")

# 16️⃣ Fayldan o‘qish
with open("friends.txt", "r") as file:
    content = file.read()
print("\n16️⃣ Fayldan o‘qilgan ma'lumot:\n", content)

# 17️⃣ Foydalanuvchidan matn kiritib faylga yozish
with open("notes.txt", "w") as file:
    for i in range(3):
        file.write(input(f"{i+1}-izoh: ") + "\n")
print("17️⃣ 'notes.txt' fayliga yozildi.")

# 18️⃣ Fayldan qatorma-qator o‘qish
with open("notes.txt", "r") as file:
    print("18️⃣ Izohlar:")
    for line in file:
        print(line.strip())
