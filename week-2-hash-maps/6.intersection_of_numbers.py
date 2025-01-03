'''
This question is asked by Google. Given two integer arrays, return their intersection.
Note: the intersection is the set of elements that are common to both arrays.

Ex: Given the following arrays...

nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []
'''

def intersection_of_numbers(nums1, nums2):
    nums1_set = set(nums1)
    intersection_set = set()
    intersection = []
    for num in nums2:
        if num in nums1_set and num not in intersection_set:
            intersection_set.add(num)
            intersection.append(num)
    return intersection


assert intersection_of_numbers([2, 4, 4, 2], [2, 4]) == [2, 4]
assert intersection_of_numbers([1, 2, 3, 3], [3, 3]) == [3]
assert intersection_of_numbers([2, 4, 6, 8], [1, 3, 5, 7]) == []
