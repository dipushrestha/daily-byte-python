"""
This question is asked by Amazon. Given a 2D board that represents a word
search puzzle and a string word, return whether or the given word can be
formed in the puzzle by only connecting cells horizontally and vertically.

Ex: Given the following board and words…

board =
[
  ['C','A','T','F'],
  ['B','G','E','S'],
  ['I','T','A','E']
]
word = "CAT", return true
word = "TEA", return true
word = "SEAT", return true
word = "BAT", return false
"""


def word_search(board, word):
    if not board or not board[0] or not word:
        return False

    rows, cols = len(board), len(board[0])

    def backtrack(i, j, k):
        if k == len(word):
            return True

        if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[k]:
            return False

        temp = board[i][j]
        board[i][j] = "#"

        found = (
            backtrack(i + 1, j, k + 1)
            or backtrack(i - 1, j, k + 1)
            or backtrack(i, j + 1, k + 1)
            or backtrack(i, j - 1, k + 1)
        )

        board[i][j] = temp

        return found

    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0):
                return True

    return False


board = [["C", "A", "T", "F"], ["B", "G", "E", "S"], ["I", "T", "A", "E"]]
assert word_search(board, "CAT") is True
assert word_search(board, "TEA") is True
assert word_search(board, "SEAT") is True
assert word_search(board, "BAT") is False
assert word_search(board, "SIT") is False
assert word_search(board, "CBI") is True
