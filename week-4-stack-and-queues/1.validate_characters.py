'''
This question is asked by Google. Given a string only containing the following 
characters (, ), {, }, [, and ] return whether or not the opening and closing characters are in a valid order.

Ex: Given the following strings...

"(){}[]", return true
"(({[]}))", return true
"{(})", return false
'''

def validate_characters(chars):
    stack = []
    bracket_pairs = { "(": ")", "{": "}", "[": "]" }

    for char in chars:
        if char in bracket_pairs:
            stack.append(char)
        else:
            if not stack or char != bracket_pairs[stack.pop()]:
                return False
    
    return len(stack) == 0


assert validate_characters("(){}[]") == True
assert validate_characters("(({[]}))") == True
assert validate_characters("{(})") == False
