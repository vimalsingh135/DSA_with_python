def count_all_numbers(numbers):
    """
    Counts the total number of elements in the given list of numbers.

    Parameters:
    numbers (list): A list of numbers.

    Returns:
    int: The count of numbers in the list.
    """
    return len(numbers)

##reverse a given number
def reverse_number(num):
    return int(str(num)[::-1])

num = 78939837303918137
print("the reversed number is", reverse_number(num))


## check if a give number is palindrome or not
def is_palindrome(n):
     if str(n)== str(n)[::-1]:
         return True
     else:
         return False
     
n=7887
print("the given number", n, "is palindrome:", is_palindrome(n))

## greatest common divisor of two numbers
def gcd(a,b):
    for i in range(1, min(a,b)+1):
        if a%i==0 and b%i==0:
            gcd=i
    return gcd
print("the gcd of 99 and 11 is", gcd(99,11))

## prime number 
def prime(u):
    if u > 1:
        for i in range(2, int(u**0.5) + 1):
            if u % i == 0:
                return False
        return True
    else:
        return False
print("the given number 11 is prime:", prime(11))


def primee(o):
    if n>1:
        for i in range(2,o):
            if o%2==0:
                return False
            else :
                return True
print("the given number is prime:", primee(89))

##sum of n numbers
def sum_of_n_numbers(n):
    return n * (n + 1) // 2
print("the sum of first 10 numbers is", sum_of_n_numbers(10)
      )

## factorial
def factorial(m):
    if m == 0 or m == 1:
        return 1
    else:
        return m * factorial(m - 1)
    
print( "the factorial is", factorial(m=5))

##check if a string is a palindrome or not
def is_string_palindrome(s):
    if s==s[::-1]:
        return True
    else:
       return False
print("the string is palindrome",is_string_palindrome(s="utuu"))

## fibonacci number
def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n
print("this is a fibanacci number", is_fibonacci(n=21))