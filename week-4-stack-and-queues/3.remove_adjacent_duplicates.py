'''
This question is asked by Facebook. Given a string s containing only lowercase 
letters, continuously remove adjacent characters that are the same and return the result.

Ex: Given the following strings...

s = "abccba", return ""
s = "foobar", return "fbar"
s = "abccbefggfe", return "a"
'''

def remove_adjacent_duplicates(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)    

    return "".join(stack)


assert remove_adjacent_duplicates("abccba") == ""
assert remove_adjacent_duplicates("foobar") == "fbar"
assert remove_adjacent_duplicates("abccbefggfe") == "a"
