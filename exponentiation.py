def looppower(num, power):
    ans = 1
    for i in range(power):
        ans = ans * num
    return ans


print(looppower(10, 2))
