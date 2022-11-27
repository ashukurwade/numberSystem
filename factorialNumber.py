# Program to calculate factorial
# 3! = 3*2*1
#from ast import main
#from math import factorial

print("Enter the number")
number = int(input())
factorial = 1

if (number<0):
    print("Error: Factorial of a negative number is not defined")
    
elif(number==0):
    print(1)
    
else:
    for i in range(1, number+1):
        factorial = factorial*i
        
        print("The factorial of", number, "is ", factorial)
        