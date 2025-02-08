"""
This question is asked by Amazon. Given a 2D matrix that represents a gold mine,
where each cell’s value represents an amount of gold, return the maximum amount
of gold you can collect given the following rules:

    You may start and stop collecting gold from any position
    You can never visit a cell that contains 0 gold
    You cannot visit the same cell more than once
    From the current cell, you may walk one cell to the left, right, up, or down

Ex: Given the following gold mine…

goldMine = [
    [0,2,0],
    [8,6,3],
    [0,9,0]
],

return 23 (start at 9 and then move to 6 and 8 respectively)
"""


def gold_rush(gold_mine):
    if not gold_mine or not gold_mine[0]:
        return 0

    rows, cols = len(gold_mine), len(gold_mine[0])

    def backtrack(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or gold_mine[i][j] == 0:
            return 0

        current_gold = gold_mine[i][j]
        gold_mine[i][j] = 0

        max_gold = current_gold + max(
            backtrack(i, j + 1),
            backtrack(i + 1, j),
            backtrack(i, j - 1),
            backtrack(i - 1, j),
        )

        gold_mine[i][j] = current_gold
        return max_gold

    max_gold = 0
    for i in range(rows):
        for j in range(cols):
            max_gold = max(max_gold, backtrack(i, j))
    return max_gold


assert gold_rush([[0, 2, 0], [8, 6, 3], [0, 9, 0]]) == 23
