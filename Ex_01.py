def power_2_iternative(k):
    result = 1;
    if k < 0:
        result = -1
    elif k == 0:
        result = 1
    else:
        for i in range(1,k+1):
            result *= 2;
    return result

k = 4
print('2^', k, ' = ',power_2_iternative(4))


#hello