# recursive function to find a value in a list

def binary_search(my_list, value):
    print(my_list)
    if len(my_list) == 0:
        return False
    elif len(my_list) == 1:
        return my_list[0] == value
    else:
        mid = len(my_list) // 2
        if value < my_list[mid]:
            new_list = my_list[:mid]
        else:
            new_list = my_list[mid:]
        return binary_search(new_list, value)
