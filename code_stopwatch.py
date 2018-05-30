import time

# enter any expression/function as code
def timer(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

# examples
print timer(1+1)
print timer (10**10)

