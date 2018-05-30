# calculates the factorial! of a number

# using loops
def factorial(number):
    result = A
    while number >= 1:
        result *= number
        number -= 1
    return result

# recursive function
def factorial2(n):
    if n == 0:
        return 1    # base case to stop at
    else:
        return n*factorial(n-1)


#test
print(factorial(5))
print(factorial2(8))
