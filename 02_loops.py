# 1-misol: 1 dan 5 gacha sonlarni chiqarish (for loop)
print("1-misol: For loop bilan sonlar")
for i in range(1, 6):
    print(i)

print("\n")

# 2-misol: List ichidagi elementlarni chiqarish
print("2-misol: Ro'yxatdagi mevalarni chiqarish")
mevalar = ["olma", "banan", "gilos"]
for meva in mevalar:
    print(meva.title())

print("\n")

# 3-misol: While loop bilan hisoblash
print("3-misol: While loop bilan hisoblash")
son = 1
while son <= 5:
    print(f"Son: {son}")
    son += 1

print("\n")

# 4-misol: While loop bilan foydalanuvchi input
print("4-misol: Foydalanuvchi bilan while loop")
savol = "Yoshingizni kiriting (chiqish uchun 'stop' deb yozing): "
while True:
    javob = input(savol)
    if javob.lower() == 'stop':
        print("Dastur to'xtadi.")
        break
    else:
        print(f"Yoshingiz: {javob}")

print("\n")

# 5-misol: FizzBuzz (for loop)
print("5-misol: FizzBuzz")
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

print("\n")

# 6-misol: While loop bilan sanash va shart qo‘yish
print("6-misol: While loop bilan sanash va shart")
raqam = 0
while raqam < 10:
    if raqam % 2 == 0:
        print(f"{raqam} - juft son")
    else:
        print(f"{raqam} - toq son")
    raqam += 1
