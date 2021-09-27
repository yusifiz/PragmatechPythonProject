print("1. Kvadrat yaratmaq olarsa daxil edilən 4 ədəddən, ekrana kvadratın sahəsini, olmazsa, həmin ədədlərin cəmini verin.")

def kvadrat(a,b,c,d):

    if a == b == c == d:
        print("Kvadratin sahesi: " + f'{a**2}')
    else:
        print("Ededlerin cemi: " + f'{a+b+c+d}')



a = int(input("1-ci ededi daxil edin: "))
b = int(input("2-ci ededi daxil edin: "))
c = int(input("3-cu ededi daxil edin: "))
d = int(input("4-cu ededi daxil edin: "))

kvadrat(a,b,c,d)

print("2. Dörd ədəd daxil edin. Onlardan ən böyüyünü çapa verin.")

nums = []

while True:
    if len(nums) < 4:
        num = int(input("Eded daxil edin:" ))
        nums.append(num)
    else:
        break

nums.sort()
print(nums[3])

print("3. Proqram run olunanda, istifadəçiyə meyvələr menyusu təqdim olunsun. Userdən menyunuzdakı meyvələrdən birinin adını daxil etməsini tələb edin və ekrana meyvənin qiymətini yazdırın. (İstədiyiniz qiyməti yazdırın). Əgər menyuda olmayan meyvə daxil edilsə, ekrana error mesajı verin.")

fruits = ["Alma","Portagal","Banan","Kivi"]

print(str(fruits))
fruit = input("Istediyiniz meyvenin adini yazin : ")
if fruit == fruits[0]:
    print("0.5 azn")
elif fruit == fruits[1]:
    print("2 azn")
elif fruit == fruits[2]:
    print("1.5 azn")
elif fruit == fruits[3]:
    print("3 azn")
else:
    print("Meyvenin adini duzgun qeyd edin!")

print("4. Qeydiyyat formu düzəldin. İstifadəçi adını daxil etsin. Adın uzunlu 3-dən kiçik 11-dən böyük ola bilməz.Əgər adını düzgün daxil edərsə, soyadının daxil etməsini istəyin. Soyad 5 hərfdən kiçik, 15 hərfdən uzun olmasın. Əgər soyad düzgün daxil edilsə, Daha sonra doğulduğu ili daxil etsin. Doğum ilinin uzunluğu 4 simvoldan ibarət olmalıdır. Sonra email daxil etməsini tələb edin. Emailin uzunluğu 10 hərifdən qısa 22 hərfdən uzzun olmasın, tərkibində @gmail.com olsun və bu hissə daxil etdiyi emailin sonunda olsun. Ardınca parol axil etsin. Parol 6-13 simvol aralığında olmalıdır. Sonra parolu təsdiqləməyini tələb edin. Təsdiqlədiyi parol birinci yazdığı parol ilə eyni olmalıdır. Bütün bunlar düzgün daxil edilərsə, Qeydiyyat tamamlandı mesajı verilsin və istifadəçidən qeydiyyatın detallarına baxmaq istəyib-istəməməsi soruşulsun. Əgər hə desə, aşağıdakı görüntü çapa verilsin: (Qeyd: Yuxarıda sizin verdiyiniz şərtlərə uyğun istifadəçi input daxil etmsəsə, hər verdiyibiz şərtə uyğun error tipli mesaj verin. Məsələn doğum ilini 5 simvoldan ibarət daxil etsə, mesaj verilsin ki 4 simvol daxil edin. Yəni hər şərti müvafiq mesajlar ilə userə izah edin. ============================================= Ad: Murad Soyad: Əliyev Yaş: 22 Email: muradaliyev1996@gmail.com Parol: 123456789 ============================================= Əgər yox desə, Murad Əliyev, Uğurlar! Yazılsın.")

print("QEYDIYYAT")



name = input("Adinizi daxil edin: ")
if 3<len(name)<11:
    surname = input("Soyadinizi daxil edin: ")
    if 5<len(surname)<15:
        year = input("Dogum ilinizi daxil edin: ")
        if len(year) == 4:
            email = input("Emailinizi daxil edin: ")
            if 10<len(email)<22 and email.split("@")[1] == "gmail.com":
                password = input("Parolunuzu daxil edin: ")
                if 6<len(password)<13:
                    confirm_password = input("Parolunuzu tesdiqleyin: ")
                    if confirm_password == password:
                        print("Qeydiyyat tamamlandi!")
                        question = input("Qeydiyyatin detallarina baxmaq isteyirsiniz?Y/N")
                        if question == "Y" or question == "y":
                            print(f'Adiniz: {name}, Soyadiniz: {surname}, Dogum iliniz: {year}, Emailiniz: {email}, Parolunuz: {password}')
                        else:
                            print(f'{name}, Ugurlar!')
                    else:
                        print("Parol eyni deyil!")
                else:
                    print("Parol min. 6, maks. 13 simvoldan ibaret ola biler!")
            else:
                print("Email min. 10, maks. 22 simvoldan ibaret ola biler ve sonu @gmail.com ile bitmelidir.")
        else:
            print("Dogum iliniz 4 simvoldan ibaret olmalidir!")
    else:
        print("Soyadiniz min. 5, maks. 15 simvoldan ibaret ola biler!")
else:
    print("Adiniz min. 3, maks. 11 simvoldan ibaret ola biler.")

print("5. Listin elementlerini toplayan alqoritm yazin. Sum funksiyasindan istifade etmeyin.")

numList = [10,20,30,40]
sum = 0
for i in range(0,len(numList)):
    sum = sum + numList[i]

print(sum)

print("6. Listin en boyuk elementini max funksiyasini istifade etmededen tapan alqoritm yazin.")

list = [12,34,45,123,46]

maxnum = 0

for i in list:
    if i > maxnum:
        maxnum = i

print(maxnum)

print("7. Listin en kicik elementini min funksiyasini istifade etmededen tapan alqoritm yazin.")

list1 = [13,34,45,561,1,23]

minnum = list1[0]

for i in list1:
    if i < minnum:
        minnum = i

print(minnum)

print("8. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2")

list2 = ['abc', 'xyz', 'aba', '1221','ana','salam','ata']
sym = 0

for i in list2:
    if i[0] == i[-1]:
        sym+=1

print(sym)

print("9. Write a Python program to check a list is empty or not.")

list3 = [1,2,3]

if len(list3) == 0:
    print("List bosdur.")
else:
    print(list3,"List doludur.")

print("10. my_text = “Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.” my_text stringindeki sozler elifba sirasi ile duzub string formatinda ekrana yazdirin.")

my_text = "write a python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings."

word = my_text.split()
sorted_word = sorted(word)
print(" ".join(sorted_word).lower())

print("11. Write a Python program to select the odd items of a list.")

list4 = [23,354,34,12,75,87,35,22,109]
odd = 0
for i in list4:
    if i % 2 ==1:
        odd+=1
print(odd)


print("12. Write a Python function to sum all the numbers in a list.Sample List : (8, 2, 3, 0, 7) Expected Output : 20")

def func(sumlist):
    sum =0
    for i in sumlist:
        sum = sum + i
    return sum
sumlist = [8, 2, 3, 0, 7]

print(func(sumlist))


print("13. Write a Python function to multiply all the numbers in a list.Sample List : (8, 2, 3, -1, 7) Expected Output : -336")

def func(multiplylist):
    multi =1
    for i in multiplylist:
        multi = multi * i
    return multi
multiplylist = [8, 2, 3, -1, 7]

print(func(multiplylist))

print("14. Write a function called returnDay. This function takes in one parameter ( a number from 1-7) and returns the day of the week ( 1 is Sunday, 2 is Monday etc.). If the number is less than 1 or greater than 7, the function should return None.")
numday = int(input("Bir reqem yazin: "))
def day(numday):
    if numday == 1:
        return "Monday"
    elif numday == 2:
        return "Tuesday"
    elif numday == 3:
        return "Wednesday"
    elif numday == 4:
        return "Thursday"
    elif numday == 5:
        return "Friday"
    elif numday == 6:
        return "Saturday"
    elif numday == 7:
        return "Sunday"
    else:
        return None

print(day(numday))
