'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
'''

def reverse(num):
    r = 0
    while num > 0:
        mod = num % 10
        r = r * 10 + mod
        num //= 10
    return r

def reverseInteger(x):
    if x < 0:
        x = abs(x)
        revnum = reverse(x)
        revnum = revnum*-1
    else:
        revnum = reverse(x)
    if revnum < -2**31 or revnum > (2**31 - 1):
        return 0
    return revnum

x = -123
# output = -321
print(reverseInteger(x))

x = 123
# output = 321
print(reverseInteger(x))

x = 120
# output = 21
print(reverseInteger(x))

x = -120
# output = -21
print(reverseInteger(x))