'''
# clever approach
def valid_palindrome_with_removal(x):
    left, right = 0, len(x) - 1
    has_mismatch = False
    while left < right:
        if x[left] != x[right]:
            if has_mismatch: return False
            has_mismatch = True
            if x[left+1] == x[right]: left += 1
            elif x[left] == x[right-1]: right -= 1
            else: return False
        left += 1
        right -= 1
    return True
'''

# standard approach
def valid_palindrome_with_removal(x):
    def is_palindrome(start, end):
        while start < end:
            if x[start] != x[end]: return False
            start += 1
            end -=1
        return True

    left, right = 0, len(x) - 1
    while left < right:
        if x[left] != x[right]: 
            return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
        left += 1
        right -=1
    return True

assert valid_palindrome_with_removal("abcba") == True
assert valid_palindrome_with_removal("foobof") == True
assert valid_palindrome_with_removal("abccab") == False
assert valid_palindrome_with_removal("abcbca") == True
assert valid_palindrome_with_removal("abcdcbx") == False
assert valid_palindrome_with_removal("abbca") == True

# Single character - should be true
assert valid_palindrome_with_removal("a") == True

# Two characters - any two chars should be true since you can remove one
assert valid_palindrome_with_removal("ab") == True
assert valid_palindrome_with_removal("aa") == True

# Three characters
assert valid_palindrome_with_removal("aba") == True  # Already palindrome
assert valid_palindrome_with_removal("abc") == False  # Can't make palindrome with one removal

# Empty string
assert valid_palindrome_with_removal("") == True

# Already palindrome cases
assert valid_palindrome_with_removal("racecar") == True
assert valid_palindrome_with_removal("aaa") == True

# Cases where removal needed at start/end
assert valid_palindrome_with_removal("xracecar") == True  # Remove first char
assert valid_palindrome_with_removal("racecarx") == True  # Remove last char

# Cases with multiple possible removals
assert valid_palindrome_with_removal("abcddcbxa") == True  # Can remove either 'a' or 'x'

# Cases requiring specific character removal
assert valid_palindrome_with_removal("abcxcba") == True  # Must remove 'x' in middle
assert valid_palindrome_with_removal("abccba") == True   # Already palindrome - no removal needed

# Long strings
assert valid_palindrome_with_removal("aaaaaaaaaaabaaaaaaaaaa") == True
assert valid_palindrome_with_removal("abcdefghijklmnopqrstuvwxyz") == False

# Repeated characters
assert valid_palindrome_with_removal("abbbba") == True
assert valid_palindrome_with_removal("abbbbxa") == True  # Remove 'x'
