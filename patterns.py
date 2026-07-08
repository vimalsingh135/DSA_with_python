##triangular pattern 

def pattern():
    for i in range(5):
        for j in range(i + 1):
            print("*", end="")
        print()
pattern()

## square pattern
def pattern_square():
    for i in range(5):
        for j in range(5):
            print("*", end="")
        print()
pattern_square()

## diamond pattern 
def diamond_pattern(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
diamond_pattern(n=5)

## right triangle pattern
def right_triangle_pattern(n):
    for i in range(n):
        print("*" * (i + 1))

right_triangle_pattern(n=5) 

## inverted right triangle pattern
def inverted_right_triangle_pattern(n):
    for i in range(n, 0, -1):
        print("*" * i)

inverted_right_triangle_pattern(n=5)

## hollow square pattern
def hollow_square_pattern(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


hollow_square_pattern(n=5)

## number pyramid pattern
def number_pyramid_pattern(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + str(i) * (2 * i - 1))
        
number_pyramid_pattern(n=5)

## sqare number pattern
def square_number_pattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(j, end=" ")
        print()

square_number_pattern(n=5) 

def number_square(n):
    for i in range(1, n+1):
        for j in range(n):
            print(i, end="")
        print()

number_square(5)

def pattern(n):
    for i in range(n):
        stars = n - i
        spaces = i * 2
        if i == 0:
            print("*" * n * 2)
        else:
            print("*" * stars + " " * spaces + "*" * stars)

pattern(5)

### hourglass pattern
def something(n):
    for i in range(n):
        print("*" * (n-i) + " " * (i*2) + "*" * (n-i))
    for i in range(n):
        print("*" * (i+1) + " " * (n-i-1)*2 + "*" * (i+1))

something(n=5)