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
