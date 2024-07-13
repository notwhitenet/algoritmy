def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)
        guess = list[mid]

        if guess == item:
            print(mid)
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 2, 4, 10, 20, 43, 204, 505, 506, 777, 999]

binary_search(my_list, 43)

# Сколько максимум нужно шагов что бы найти нужное число из списка 128
# 128 / 2 = 64 - 1
# 64 / 2 = 32 - 2
# 32 / 2 = 16 - 3
# 16 / 2 = 8 - 4
# 8 / 2 = 4 - 5
# 4 / 2 = 2 - 6
# 2 / 2 = 1 - 7

#import math
#print(int(math.log(128, 2)))
