'''
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...
'''

def excelSheetColumnTitle(columnNumber):

    alphabets  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while columnNumber:
        columnNumber -= 1
        result = alphabets[columnNumber%26] + result
        columnNumber //= 26
    return result


columnNumber = 1
print(excelSheetColumnTitle(columnNumber))
#output = A

columnNumber = 28
print(excelSheetColumnTitle(columnNumber))
#output = AB

columnNumber = 701
print(excelSheetColumnTitle(columnNumber))
#output = ZY