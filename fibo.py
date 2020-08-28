def fibo(n):
    curr = 1
    prev = 1
    for i in range(n-2):
        curr, prev = curr + prev, curr
        print(curr)


fibo(6)
