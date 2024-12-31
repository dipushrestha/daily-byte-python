'''
This question is asked by Microsoft. Given an array of strings, return the 
longest common prefix that is shared amongst all strings.
Note: you may assume all strings only contain lowercase alphabetical characters.

Ex: Given the following arrays...

["colorado", "color", "cold"], return "col"
["a", "b", "c"], return ""
["spot", "spotty", "spotted"], return "spot"
'''

'''
def longest_common_prefix(*words):
    min_len = min(len(y) for y in words)
    prefix = ''
    for i in range(min_len):
        for j in range(len(words)):
            if words[0][i] != words[j][i]: return prefix
        prefix += words[0][i]
    return prefix
'''

# sorting approach
def longest_common_prefix(*words):
    sorted_words = sorted(words)
    first, last = sorted_words[0], sorted_words[-1]
    first_len, last_len = len(first), len(last)
    for i in range(first_len):
        if i >= last_len or first[i] != last[i]: return first[:i]
    return first

assert longest_common_prefix("colorado", "color", "cold") == "col"
assert longest_common_prefix("a", "b", "c") == ""
assert longest_common_prefix("spot", "spotty", "spotted") == "spot"
