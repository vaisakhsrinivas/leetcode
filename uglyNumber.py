'''
An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

Given an integer n, return true if n is an ugly number.
'''


def uglyNumber(n):

    primeFactors = [2,3,5]
    if n < 0:
        return False
    for f in primeFactors:
        while n % f == 0:
            n //= f
    return n == 1

number = uglyNumber(6)
print(number)

number = uglyNumber(1)
print(number)

number = uglyNumber(14)
print(number)
