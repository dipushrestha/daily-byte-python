'''
This question is asked by Facebook. Given two strings s and t return whether or not s is an anagram of t.
Note: An anagram is a word formed by reordering the letters of another word.

Ex: Given the following strings...

s = "cat", t = "tac", return true
s = "listen", t = "silent", return true
s = "program", t = "function", return false
'''

def valid_anagram(s, t):
    if len(s) != len(t): return False
    letter_count = {}
    for letter in s:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    for letter in t:
        if letter not in letter_count or letter_count[letter] == 0:
            return False
        letter_count[letter] -= 1
    return True


assert valid_anagram("cat", "tac") == True
assert valid_anagram("listen", "silent") == True
assert valid_anagram("program", "function") == False
