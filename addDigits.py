'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
'''


def addDigits(num):

    if num == 0:
        return 0
    if num % 9 == 0:
        return 9
    else:
        return (num % 9)


ans = addDigits(38)
print(ans)
#output - 2
ans = addDigits(0)
print(ans)
#output - 1
ans = addDigits(123)
print(ans)
#output - 6