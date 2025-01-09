'''
This question is asked by Amazon. Given two strings s and t, which represents 
a sequence of keystrokes, where # denotes a backspace, return whether or not 
the sequences produce the same result.

Ex: Given the following strings...

s = "ABC#", t = "CD##AB", return true
s = "como#pur#ter", t = "computer", return true
s = "cof#dim#ng", t = "code", return false
'''

def compare_keystrokes(s, t):
    def result_sequence(keystrokes):
        stack = []

        for keystroke in keystrokes:
            if stack and keystroke == "#":
                stack.pop()
            else:
                stack.append(keystroke)

        return stack
    
    return result_sequence(s) == result_sequence(t)


assert compare_keystrokes("ABC#", "CD##AB") == True
assert compare_keystrokes("como#pur#ter", "computer") == True
assert compare_keystrokes("cof#dim#ng", "code") == False
