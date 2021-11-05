# print("1. Hər hansı bir natural n ədədini götürək. Onu növbəti şəkildə dəyişdirəcəyik: Əgər ədəd cütdürsə, onda onu 2-ə bölək, əgər təkdirsə ona 1 əlavə edək. Bir neçə belə dəyişmədən sonra həmişə 1 alacağıq. Məsələn, 11 ədədindən 12 ədədi alınır, sonra 6, 3, 4, 2 və sonda 1. Beləliklə, 11-dən 1 almaq üçün 6 dəyişiklik etmək lazımdır. Verilmiş natural ədədə görə 1 alınana qədər onun dəyişmələrinin sayını tapın.")



# def operate(num):
#       if(num % 2 == 0):
#           return num // 2
#       else:
#           return num + 1

# def run(num):
#       print(num)
#       while(num != 1):
#             num = operate(num)
#             print(num)

# num = int(input("Eded daxil edin: "))

# print(run(num))

# print("2. n natural ədədi verilmişdir. Əgər n ədədi hər hansı bir m natural ədədinin kvadratıdırsa, onda m ədədini çap edin, əks halda No çap edin. Məsələn: User 25 daxil etsə ekrana 5 verilsin 27 daxil etsə, NO yazılsın")

# import math

# n = int(input("Natural eded daxil edin: "))

# if math.sqrt(n) == int(math.sqrt(n)):
#     print(int(math.sqrt(n)))
# else:
#     print("NO")

# print("3. User bir ədəd daxil etsin həmin ədədə qədər bütün ədədləri çapa verin.")

# eded = int(input("Eded daxil edin: "))
# for i in range(0,eded):
#     print(i+1)

# print("4. İnternetdən bir mətni bir dəyişkəndə saxlayın. Həmin mətnin cüt indexlərində olan simvolları bir sətirdə çapa verin.")

# text = "Lothar Collatz likely posed the eponymous conjecture in the 1930s. The problem sounds like a party trick. Pick a number, any number. If it’s odd, multiply it by 3 and add 1. If it’s even, divide it by 2. Now you have a new number. Apply the same rules to the new number. The conjecture is about what happens as you keep repeating the process."

# print(text[0::2])

# print("5. Random bir rəqəm götürsün proqram 1-4 aralığında. İstifadəçidən həmin rəqəmi təxmin etməyi istəyin. Hər doğru təxmin etdikcə istifadəçi bir xal qazansın. 5 xala çatanda istifadəçinin 5 xala çatması üçün etdiyi cəhdlərin sayını çapa verin.")

# import random


# cehd = 0
# point = 0

# while point!=5:
#     randomNum = random.randint(1,4)
#     suggesstion = int(input("1 ile 4 arasinda bir eded yazin: "))
#     cehd+=1
#     if randomNum == suggesstion:
#         point+=1
#         print(f'{point} xaliniz var.')
#     else:
#         print("tekrar cehd edin")
# print(cehd)

# print("6. Userdən daxil etmısini tələb edin. 1-dən sonra gələn ən kiçik bölünəni çapa verin.")


# n=int(input("Boluneni daxil edin:"))
# lis1=[]
# for i in range(2,n+1):
#     if(n%i==0):
#         lis1.append(i)
# lis1.sort()
# print("1-den sonra en kicik bolen:",lis1[0])

# print("7. Masa üzərində n sikkə var. Onların bəzilərinin reşka (1) üzü, bəzilərinin isə gerb( 0) üzü yuxarıdır. Bütün sikkələrin eyni üzlərinin yuxarı olması üçün çevriləcək sikkələrin minimal sayını tapın. İstifadəçi birinci inputda sikkələrin sayını daxil edir. O daxil etdiyi sayda siz userdən sikkələrin hansı üzdə düşdüyünü soruşmalısız. Bütün üzləri daxil etdikdən sora siz bütün sikkələri eyni üzə çevirmək üçün ən minumum sayı tapmalısız. Məsələn birinci inputda sikkələrin sayını user 5 daxil edib. Ardınca 5 sikkənin hər birinin üzünü daxil edir. 1, 0, 0, 1, 0. Bu sikkələrin üzünü bir etmək üçün iki yolumuz var: ya hamısını 0 ya da hamısını 1 etməliyik. 1-ləri 0 etmək daha qısa yoldur, çünki onların sayı azdır. Bu səbəbdən edəcəyimiz minimal hərəkət sayı ikidir. Əgər 0 və 1 eyni sayda olarsa, EQUAL çapa verin.")

# sikkeSayi = int(input("Nece sikke daxil etmek isteyirsiniz?: "))
# sikkeler = []
# for i in range(0,sikkeSayi):
#     sikkeUzu = input("Sikkeler hansi uzdedir?0/1 ")
#     sikkeler.append(sikkeUzu)

# if sikkeler.count("0")>sikkeler.count("1"):
#     print(f'Sikkelerin hamisinin eyni uze cevirmek ucun min say: {sikkeler.count("1")}')
# elif sikkeler.count("0")==sikkeler.count("1"):
#     print("EQUAL")
# else:
#     print(f'Sikkelerin hamisinin eyni uze cevirmek ucun min say: {sikkeler.count("0")}')

# print("8. Userdən bir ədəd daxil etməsini tələb edin. Ekrana həmin ədəddəki ədədlərin hasilini çapa verin.")

# x = input("Eded daxil edin: ")

# list = []
# list.append(x)
# result = 1

# for elem in str(list[0]):
#     result*=int(elem)

# print(result)


print("9. Kvadrat tənliyin əmsallarını daxil etsin user. Həmin əmsallara görə tənliyin köklərini daxil edin.")
import math

print("Kvadrat tenlik: a*x*x + b*x + c = 0")

a = int(input("a emsalini daxil edin: "))
b = int(input("b emsalini daxil edin: "))
c = int(input("c emsalini daxil edin: "))
d = math.pow(b,2) - 4*a*c

if d>0:
    print("Kvadrat tenliyin 2 koku var.")
    x1 = (-b + math.sqrt(d))/(2*a)
    print(f'x1 = {x1}')
    x2 = (-b - math.sqrt(d))/(2*a)
    print(f'x2 = {x2}')
elif d == 0:
    print("Kvadrat tenliyin 2 beraber, yeni 1 koku var.")
    x1 = (-b)/(2*a)
    print(f'x1 = x2 = {x1}')
else:
    print("Kvadrat tenliyin heqiqi koku yoxdur.")
    x1 = (-b + math.sqrt(math.pow(-b,2) + 4*a*c))/(2*a)
    print(f'x1 = {x1}')
    x2 = (-b - math.sqrt(math.pow(-b,2) + 4*a*c))/(2*a)
    print(f'x2 = {x2}')

# print("10. 1-50 arasında ədədlərdən 3-ə bölünən ədədlərə three, 5-ə bölünən ədədlərə five, həm 3 və həm də 5-ə bölünənlərə isə ThreeFive print edin. Əgər heç birinə bölünməsə sadəcə ədədin özünü çapa verin.")

# for i in range(1,51):
    
#     if i % 3 == 0 and i % 5 == 0:
#         print("ThreeFive")
#     elif i % 5 == 0:
#         print("five")
#     elif i % 3 == 0:
#         print("three")
#     else:
#         print(i)