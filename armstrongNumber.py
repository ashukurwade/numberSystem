#from ast import Num

Num = int(input("Enter a number:"))
sum = 0
temp = Num
while temp > 0:
    digit = temp % 10
    sum+= digit 
    temp //= 10
if Num == sum:
    print(Num,"is an Armstrong number")
else:
    print(Num,"is not a Armstron number")
