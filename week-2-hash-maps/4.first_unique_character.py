'''
This question is asked by Microsoft. Given a string, return the index of its
first unique character. If a unique character does not exist, return -1.

Ex: Given the following strings...

"abcabd", return 2
"thedailybyte", return 1
"developer", return 0
'''

def first_unique_character(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    return -1


assert first_unique_character("abcabd") == 2
assert first_unique_character("thedailybyte") == 1
assert first_unique_character("developer") == 0

assert first_unique_character("") == -1  # Empty string
assert first_unique_character("a") == 0  # Single character
assert first_unique_character("aa") == -1  # No unique character
assert first_unique_character("ab") == 0  # Both unique, return first

assert first_unique_character("a" * 10**6 + "b") == 10**6  # Unique character at the end
assert first_unique_character("a" * 10**6) == -1  # No unique character
