# recursive function that sorts a list from small to large numbers

import random

def quick_sort(num):
    if len(num) <= 1:
        return num
    else:
        # select a random value of the list as the pivot
        pivot = num.pop( random.randint( 0, len(num)-1 ) )

        # separate values smaller than pivot from those bigger or equal than the pivot
        less, greater = [], []
        for val in num:
            if val < pivot:
                less.append(val)
            else:
                greater.append(val)

        # concat sorted smaller values + pivot + sorted greater values
        return quick_sort(less) + [pivot] + quick_sort(greater)

numbers = [3, 4, 2, 5, 3, 8, 1]
print(quick_sort(numbers))