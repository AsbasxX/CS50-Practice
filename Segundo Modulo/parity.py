"""Check if a number is even or odd.
x = int(input("What's x? "))

if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")
"""

def main():
    x = int(input("What's x? "))
    if isEven(x):
        print("x is even")
    else:
        print("x is odd")

"""Return True if n is even, else False.
def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False
"""

"""
def isEven(n):
    return True if n % 2 == 0 else False
"""

def isEven(n):
    return n % 2 == 0

main()