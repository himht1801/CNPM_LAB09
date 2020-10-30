def power_2_recursion(k):
    if k < 0:
        return -1
    if k == 0:
        return 1
    return 2*power_2_recursion(k-1)

k = 4
print('2^', k, ' = ', power_2_recursion(4))