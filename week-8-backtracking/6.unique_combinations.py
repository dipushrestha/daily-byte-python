"""
This question is asked by Apple. Given a list of positive numbers without duplicates
and a target number, find all unique combinations of the numbers that sum to the target.
Note: You may use the same number more than once.

Ex: Given the following numbers and target…

numbers = [2,4,6,3], target = 6,
return [
    [2,2,2],
    [2,4],
    [3,3],
    [6]
]
"""


def unique_combinations(numbers, target):
    result = []
    numbers.sort()

    def backtrack(start, current, current_sum):
        if current_sum == target:
            result.append(current.copy())
            return

        for i in range(start, len(numbers)):
            num = numbers[i]

            if current_sum + num > target:
                break

            current.append(num)

            backtrack(i, current, current_sum + num)

            current.pop()

    backtrack(0, [], 0)

    return result


assert unique_combinations([2, 4, 6, 3], 6) == [[2, 2, 2], [2, 4], [3, 3], [6]]
