def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        a = f(n-1)
        b = f(n-2)
        return a + b


print(f(100))