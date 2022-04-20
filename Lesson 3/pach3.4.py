def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res


print(power(float(input("Первое значение - ")), int(input("Второе значение - "))))





def pow_h(base, degree, module):
    degree = bin(degree)[2:]
    r = 1

    for i in range(len(degree) - 1, -1, -1):
        r = (r ** 2) % module
        r = (r * base ** int(degree[i])) % module
    base = (base ** 2) % module
    return r

def my_func(x, y):
    return 1 / x ** abs(y)
    #return x ** y
print(my_func(2, -3))