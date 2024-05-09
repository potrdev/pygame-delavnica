def f(x):
    st = 0
    for i in range(1, x + 1):
        if x % i == 0:
            st += 1

    return st == 2

st = int(input())
print(f(st))    