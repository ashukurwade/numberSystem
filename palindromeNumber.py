#take input
print("Enter Your Number ")
number = int(input())
#print(type(number))
temp = number
reverse = 0

while(number>0):
    dig = number%10
    reverse = reverse *10 + dig 
    number = number // 10
    
#print(reverse)
if temp==reverse:
    print("Number is a Palindrome")
else:
    print("Number is not a Palindrome")
    
    
