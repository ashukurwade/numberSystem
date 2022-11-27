def sumPrime(rangeLeft, rangeRight):
 
    sum = 0
 
    for i in range(rangeRight, (rangeLeft - 1), -1) :
 
        # Check for prime
        isPrime = checkPrime(i)
         
        if (isPrime) :
 
            # Sum the prime number
            sum += i
        return sum
 