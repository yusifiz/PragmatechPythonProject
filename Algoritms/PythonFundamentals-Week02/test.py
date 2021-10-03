# 1. Numbers=(1,2,3,4) map()-den istifade ederek her elementi iki defe artirin.

from typing import List


def foo(num):
    return num * 2

nums = [1,2,3,4]

print(list(map(foo,nums)))

# 2. filter()-den ve lambda-dan istifade ederek, NumberS(100,21,53,44) listinde cut reqemleri elde edin.
print("-------------------------------------")
func = lambda x: x % 2 == 0

x = (100,21,53,44)
print(list(filter(func,x)))

# 3. sampleList=[1,2,3,3,3,3,4,5]
#    uniqueList=[1,2,3,4,5]
print("-------------------------------------")
def unique(n):
    uniqueList=[]
    for i in n:
        if i not in uniqueList:
            uniqueList.append(i)
        
    print(uniqueList)
sampleList=[1,2,3,3,3,3,4,5]
unique(sampleList)

# 4. Write a Python program to sort each sublist of strings in a given list of lists using lambda.
# Original list:
# [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]

# After sorting each sublist of the said list of lists:
# [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
print("-------------------------------------")
def sortedList(list):
    result = [sorted(x, key=lambda x:x[0]) for x in list]
    return result

list = [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]

print(sortedList(list))

# 5. x ededinin [a,b] intervalinda olub-olmadigini teyin edin.
print("-------------------------------------")


a1 = int(input("a ededini daxil edin:" ))
x1 = int(input("x ededini daxil edin:" ))
b1 = int(input("b ededini daxil edin:" ))

if x1<a1 or x1>b1:
    print("IN")
else:
    print("OUT")

# 6. Kar Karic Pin meselesi. Verilenler: hundurluk-h, en-w, uzunluq-l,kubmetr-k
print("-------------------------------------")

_h = int(input("Hundurluyu daxil edin: " ))
_w = int(input("Eni daxil edin: " ))
_l = int(input("Uzunlugu daxil edin: " ))
_k = int(input("Kubmetri daxil edin: " ))

print(f'Istifade olunmali en az batareya: {(_h*_w*_l)/_k}')

# 7. Tort meselesi. Verilenler masanin radiusu-r, tortun eni-w, tortun uzunlugu-l

# QEYD: eger tortun diaqonali (d) masanin diametrinden (r*2) kicikdirse, yerlesecek.
print("-------------------------------------")
import math

_w1 = int(input("Tortun enini daxil edin: " ))
_l1 = int(input("Tortun uzunlugunu daxil edin: " ))
_r = int(input("Masanin radiusunu daxil edin: "))
_d = math.sqrt(math.pow(_w1,2)+math.pow(_l1,2)) # Tortun diaqonali

if _r*2>=_d:
    print("YES")
else:
    print("NO")
