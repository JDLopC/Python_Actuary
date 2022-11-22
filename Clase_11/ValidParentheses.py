'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.'''

# []
# ()
# {[[()]]}
# (){[]}
# ]
# }
# )
# ([{]]}])
#([{})]
# [



'''
( -> 0
[ -> 1
{ -> 2

0 -> )
1 -> ]
2 -> }
'''

def Valid(s:str):
    stack = []
    apertura = {
        '(': 0,
        '[': 1,
        '{': 2
    }
    cierre = {
        ')': 0,
        ']': 1,
        '}': 2
    }
    for i in s:
        if i in apertura:
            stack.append(apertura[i])
        elif len(stack) == 0:
            return False
        elif stack[-1] != cierre[i]:
            return False
    return True

def Valid2(s:str):
    
    ac = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = []
    
    for i in s:
        if i in ac:
            if not stack:
                return False
            if stack[-1] != ac[i]:
                return False
        stack.append(i)
    return True
    
string = '([{]]}])' # F
string1 = '[]' # T
string2 = '()' # T
string3 = '{}' # T
string4 = '[][]{}' # T
string5 = '[]()(())' # T
string6 = '[]()((]]))' #F
string7 = '[]()(}())' #F
string8 = '[]()({}([])])' #F

print(Valid2(string))
print(Valid2(string1))
print(Valid2(string2))
print(Valid2(string3))
print(Valid2(string4))
print(Valid2(string5))
print(Valid2(string6))
print(Valid2(string7))
print(Valid2(string8))