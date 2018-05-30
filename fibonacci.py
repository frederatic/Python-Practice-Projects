
# iterative function using loop
def fibo(n):
    current = 0
    after = 1
    for i in range(0,n):
        current, after = after, current + after
    return current


# recursive function
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        result = fibonacci(n-1)+fibonacci(n-2)
        return result


#fibo(5)-> 4      +      3
#        3 + 2    +    2 + 1
#       2+1  1+0  +   1+0  1
#       1+0 1 1 1 +   1 1  1
#       1 1 1 1 1 +   1 1  1    