'''
This question is asked by Apple. Given two binary strings 
(strings containing only 1s and 0s) return their sum (also as a binary string).
Note: neither binary string will contain leading 0s unless the string itself is 0

Ex: Given the following binary strings...

"100" + "1", return "101"
"11" + "1", return "100"
"1" + "0", return  "1"
'''

def add_binary(x, y):
    max_len = max(len(x), len(y))

    x_norm = x.zfill(max_len)
    y_norm = y.zfill(max_len)

    result = ''
    carry = 0

    for i in range(max_len - 1, -1, -1):
        step_sum = carry
        step_sum += 1 if x_norm[i] == '1' else 0
        step_sum += 1 if y_norm[i] == '1' else 0

        if step_sum > 1:
            carry = 1
            result = ('1' if step_sum == 3 else '0') + result
        else:
            carry = 0
            result = str(step_sum) + result
    
    if carry == 1: result = '1' + result
    return result


assert add_binary("100", "1") == "101"
assert add_binary("11", "1") == "100"
assert add_binary("1", "0") == "1"
