# 25/04/21
# Graziela Maria
# Palavra de fibonacci recursiva


def fibo(n):
    if n == 0:
        return "b"
    elif n == 1:
        return "a"
    else:
        return fibo(n-1) + fibo(n-2)


N = int(input())
if N == 0:
    print("b")
elif N == 1:
    print("a")
else:
    result = fibo(N)
    print(result)
