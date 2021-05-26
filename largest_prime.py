import math
  
# A function to find largest prime factor
def largestPrime(n):
    # initialize maxPrime 
    maxPrime = -1
      
    # while n is even, divide by 2
    while n%2==0:
        maxPrime = 2
        n /= 2
          
    # n must be odd at this point, so we
    # iterate only for odd integers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n%i==0:
            maxPrime = i
            n = n/i
      
    # If n is neither divisible by even nor odd
    # it must be a prime number
    if n > 2:
        maxPrime = n
      
    return int(maxPrime)
  
# test cases
n = 100
print(largestPrime(n))

n = 15
print(largestPrime(n))

n = 17
print(largestPrime(n))
  
n = 600851475143
print(largestPrime(n))

# Answer: 6,857
