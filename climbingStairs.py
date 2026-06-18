def climbStairs(n):
    # recursion solution times out for n = 44

    one = 1
    two = 1

    for i in range(n-1):
        tmp = one
        one = one + two
        two = tmp
    return one


n = 2
print(climbStairs(n))
n = 3
print(climbStairs(n))
n = 4
print(climbStairs(n))