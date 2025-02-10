"""
This question is asked by Facebook. Given an integer N, where N represents the
number of pairs of parentheses (i.e. ”(“ and ”)”) you are given, return a list
containing all possible well-formed parentheses you can create.

Ex: Given the following value of N…

N = 3,
return [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
]
"""


def parenthesis_generation(n):
    result = []

    def backtack(current, left, right):
        if len(current) == n * 2:
            result.append(current)
            return

        if left < n:
            backtack(current + "(", left + 1, right)

        if right < left:
            backtack(current + ")", left, right + 1)

    backtack("", 0, 0)

    return result


assert parenthesis_generation(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
