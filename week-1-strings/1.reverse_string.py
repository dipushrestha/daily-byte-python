'''
This question is asked by Google. Given a string, reverse all of its characters
and return the resulting string.

Ex: Given the following strings...

“Cat”, return “taC”
“The Daily Byte”, return "etyB yliaD ehT”
“civic”, return “civic”
'''

def reverse_string(x):
    reverse_list = []
    for i in range(len(x) - 1, -1, -1):
        reverse_list.append(x[i])
    return ''.join(reverse_list)


assert reverse_string("Cat") == "taC"
assert reverse_string("The Daily Byte") == "etyB yliaD ehT"
assert reverse_string("civic") == "civic"
