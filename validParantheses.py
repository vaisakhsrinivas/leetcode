def validParantheses(s):

    stack = []
    valid = {"()", "{}", "[]"}

    for bracket in s:
        if bracket in "({[":
            stack.append(bracket)
        else:
            if not stack or stack.pop()+bracket not in valid:
                return False
    return not stack


s = "()"
#output true
print(validParantheses(s))
s = "()[]{}"
#output true
print(validParantheses(s))
s = "(]"
#output false
print(validParantheses(s))
s = "([])"
#output true
print(validParantheses(s))
s = "([)]"
#output false
print(validParantheses(s))
