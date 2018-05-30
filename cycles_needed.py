# calculates the number of cycles needed for a starting number to reach a given target with a spread

def cycles(n, spread, target):
    if n >= target:
        return 0
    else:
        return 1 + cycles(n+n*spread, spread, target)


# example: 5 people have a virus (n=5) and infect 10 other people every hour (spread=10)
# to calculate how long it takes to infect 100 people (target=100)
print(cycles(5,10,100))
#>>2 hours