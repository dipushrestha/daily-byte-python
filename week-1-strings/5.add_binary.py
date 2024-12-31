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
