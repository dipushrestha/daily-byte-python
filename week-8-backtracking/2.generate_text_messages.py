"""
This question is asked by Google. Given a string of digits, return all possible
text messages those digits could send. Note: The mapping of digits to letters is as follows…

0 -> null
1 -> null
2 -> "abc"
3 -> "def"
4 -> "ghi"
5 -> "jkl"
6 -> "mno"
7 -> "pqrs"
8 -> "tuv"
9 -> "wxyz"

Ex: digits = "23" return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
"""


def generate_text_messages(digits):
    if not digits:
        return []

    digits_map = {
        "0": "",
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    text_messages = [char for char in digits_map[digits[0]]]

    for digit in digits[1:]:
        new_text_messages = []
        for text_message in text_messages:
            for char in digits_map[digit]:
                new_text_messages.append(text_message + char)
        text_messages = new_text_messages

    return text_messages


# def generate_text_messages(digits):
#     if not digits:
#         return []

#     digits_map = {
#         "0": "",
#         "1": "",
#         "2": "abc",
#         "3": "def",
#         "4": "ghi",
#         "5": "jkl",
#         "6": "mno",
#         "7": "pqrs",
#         "8": "tuv",
#         "9": "wxyz",
#     }

#     text_messages = []

#     def backtrack(i, path):
#         if i == len(digits):
#             text_messages.append(path)
#             return

#         letters = digits_map.get(digits[i], "")

#         if not letters:
#             backtrack(i + 1, path)
#         else:
#             for char in letters:
#                 backtrack(i + 1, path + char)

#     backtrack(0, "")

#     return text_messages

assert generate_text_messages("23") == [
    "ad",
    "ae",
    "af",
    "bd",
    "be",
    "bf",
    "cd",
    "ce",
    "cf",
]
