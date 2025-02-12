"""
This question is asked by Google. Given a string s, return all possible
partitions of s such that each substring is a palindrome.

Ex: Given the following string s…

s = "abcba",
return [
    ["a","b","c","b","a"],
    ["a","bcb","a"],
    ["abcba"]
]
"""


def palindrome_splitting(s):
    palindromes = []

    def backtrack(current, start):
        if start == len(s):
            palindromes.append(current.copy())
            return

        for i in range(start, len(s)):
            cur_s = s[start : i + 1]
            if cur_s == cur_s[::-1]:
                current.append(cur_s)
                backtrack(current, i + 1)
                current.pop()

    backtrack([], 0)
    return palindromes


assert palindrome_splitting("abcba") == [
    ["a", "b", "c", "b", "a"],
    ["a", "bcb", "a"],
    ["abcba"],
]
