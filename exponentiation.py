def looppower(a, n):
    ans = 1
    for i in range(n):
        ans = ans * a
    return ans


# divide and conquer
def recPower(a, n):
    if n == 0:
        return 1
    else:
        factor = recPower(a, n//2)
        if n % 2 == 0:
            return factor*factor
        else:
            return factor*factor*a


print(recPower(2, 3))
