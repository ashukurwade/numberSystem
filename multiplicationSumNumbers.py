def multiplication_or_sum(num1,num2):
    # calculate product of two numbers
    product = num1 * num2
    # check product is less than 1000
    if product <=1000:
        return product
    # product is greater than 1000 calculate sum
    else:
        return num1 + num2
  
# first condition  
result = multiplication_or_sum(20,30)
print("result is ", result)
# Second condition
result = multiplication_or_sum(30,40)
print("result is ", result)