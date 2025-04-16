
#Initial version by me
def isValid(s):
    
    opening_stack = []
    paired_parentheses = ["()", "[]", "{}"]

    if len(s) % 2 != 0:
        return False

    for symbol in s:
        if symbol == "(" or symbol == "[" or symbol == "{":
            opening_stack.append(symbol)
        else:
            if not opening_stack or opening_stack[-1] + symbol not in paired_parentheses:
                return False
            opening_stack.pop()
            
    if not opening_stack:
        return True
    else:        
        return False
    
# Optimized version after getting hints from ChatGPT
def isValid2(s):
    
    opening_stack = []
    paired_parentheses = {')': '(', ']': '[', '}': '{'}

    # Check if the total amount of parentheses is odd 
    if len(s) % 2 != 0:
        return False

    for symbol in s:
        if symbol == "(" or symbol == "[" or symbol == "{":
            opening_stack.append(symbol)
        else:
            if not opening_stack or opening_stack[-1] != paired_parentheses[symbol]:
                return False
            
            opening_stack.pop()
            
    return not opening_stack


print(isValid2('((()))'))     