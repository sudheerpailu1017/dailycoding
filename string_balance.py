'''
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.'''

def balance(s):
    ls = []
    for c in s:
        if c in ["(", "[", "{"]:
            ls.append(c)
        else:
            if not ls:
                return False
            if (c == ")" and ls[-1] != "(") or \
               (c == "]" and ls[-1] != "[") or \
               (c == "}" and ls[-1] != "{"):
                return False
            ls.pop()
    return len(ls) == 0
    
s=input()
print(balance(s))