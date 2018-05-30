
# recursive lucas function
def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        result = lucas(n-1) + lucas(n-2)
        return result