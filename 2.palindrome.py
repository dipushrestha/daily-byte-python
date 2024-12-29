def palindrome(x):
    left, right = 0, len(x) - 1

    while left < right:
        while left < right and not x[left].isalpha():
            left += 1
        while left < right and not x[right].isalpha():
            right -=1
        if x[left].lower() != x[right].lower():
            return False
        left += 1
        right -= 1
    return True


assert palindrome("level") == True
assert palindrome("algorithm") == False
assert palindrome("A man, a plan, a canal: Panama.") == True
