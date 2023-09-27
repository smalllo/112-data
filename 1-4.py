#109021049-羅浩維
import math

# Function to check if a is divisible by b
def divisible(a, b):
    return a % b == 0

# Function to check if n is a prime number
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    
    # Calculate the square root of n
    sqrt_n = math.isqrt(n)
    
    # Check for divisibility from 2 to sqrt_n
    for i in range(2, sqrt_n + 1):
        if divisible(n, i):
            return False
    
    return True

# Main program
n = int(input("Enter an integer to check if it's prime: "))

if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
