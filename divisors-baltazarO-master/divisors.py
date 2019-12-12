def divisors(num):
    my_list = [num]
    if num == 1:
        return my_list
    for x in range(1, (num // 2) + 1):
        if num % x == 0:
            my_list.append(x)
    my_list.sort()
    return my_list
