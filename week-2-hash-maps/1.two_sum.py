'''
# bruteforce approach
def two_sum(nums, k):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == k: 
                return True
    return False
'''

def two_sum(nums, k):
    checked = set()
    for num in nums:
        diff = k - num
        if diff in checked: return True
        checked.add(num)
    return False


assert two_sum([1, 3, 8, 2], 10) == True
assert two_sum([3, 9, 13, 7], 8) == False
assert two_sum([4, 2, 6, 5, 2], 4) == True

# Basic cases
assert two_sum([2, 7, 11, 15], 9) == True   # 2 + 7 = 9
assert two_sum([1, 5, 3, 6], 10) == False 
assert two_sum([1, 2, 3, 4], 8) == False    # No pair sums to 8

# Edge cases
assert two_sum([], 5) == False              # Empty list
assert two_sum([5], 5) == False             # Single element
assert two_sum([1, 1], 2) == True           # Pair sums to target
assert two_sum([1, 1, 1], 3) == False       # Only duplicates, no valid pair

# Negative numbers
assert two_sum([-3, 4, 3, 90], 0) == True   # -3 + 3 = 0
assert two_sum([-2, -1, -5, -4], -6) == True # -1 + -5 = -6
assert two_sum([-2, -3, -4, -5], -10) == False # No pair sums to -10

# Repeated elements
assert two_sum([1, 2, 3, 4, 4], 8) == True  # 4 + 4 = 8
assert two_sum([5, 5, 5, 5], 10) == True    # 5 + 5 = 10
assert two_sum([2, 2, 2, 2], 5) == False    # No pair sums to 5

# Large numbers
assert two_sum([1000000, 999999, 2], 1999999) == True # 1000000 + 999999 = 1999999
assert two_sum([1000000, 1, 2, 3], 1000002) == True  # 1000000 + 2 = 1000002
assert two_sum([1000000, 500000], 2000000) == False  # No pair sums to 2000000

# Mixed positive and negative
assert two_sum([-10, 20, -5, 15], 10) == True        # -10 + 20 = 10
assert two_sum([0, -1, 1], 0) == True               # -1 + 1 = 0
assert two_sum([-3, -1, 2, 5], 1) == True           # -1 + 2 = 1
assert two_sum([-10, -20, 30, 10], 0) == True   
