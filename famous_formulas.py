## fibonacci series
def fib(n):
    if n<=1:
        values=n
    else:
        values= fib(n-1)+fib(n-2)
    return values
print(fib(10))

## the fibonacci series using dynamic programming,
#  see our fibonacci series code is correct but what if we have to find the fibonacci of larger numbers lets say 1000 or something than our computer will take the long time to compute that or sometime it may crash, this is becauseit has to repetitative to the calculation of smaller number again and again so that why we will use fibonacci series with dymanic programming
fibtable={}
def fib_dp(n):
    if n in fibtable.keys():
        return (fibtable[n])
    if n<=1:
        values=n
    else:
        values=fib_dp(n-1)+fib_dp(n-2)
        fibtable[n]=values
    return values
print (fib_dp(101))

## factorial of a number
def fact(n):
    if n==0 or n==1:
        return 1 
    else:
        return n*fact(n-1)
print(fact(5))