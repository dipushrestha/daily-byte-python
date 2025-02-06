"""
This question is asked by Amazon. Given a string s consisting of only letters
and digits, where we are allowed to transform any letter to uppercase or
lowercase, return a list containing all possible permutations of the string.

Ex: Given the following string…

S = "c7w2", return ["c7w2", "c7W2", "C7w2", "C7W2"]
"""


def string_permutations(s):
    if not s:
        return [s]

    if s[0].isalpha():
        permutations = [s[0].lower(), s[0].upper()]
    else:
        permutations = [s[0]]

    for char in s[1:]:
        new_permutations = []
        for perm in permutations:
            if char.isalpha():
                new_permutations.append(perm + char.lower())
                new_permutations.append(perm + char.upper())
            else:
                new_permutations.append(perm + char)
        permutations = new_permutations

    return permutations


# backtracking approach
# def string_permutations(s):
#     permutations = []

#     def backtrack(i, path):
#         if i == len(s):
#             permutations.append(path)
#             return

#         if s[i].isalpha():
#             backtrack(i + 1, path + s[i].lower())
#             backtrack(i + 1, path + s[i].upper())
#         else:
#             backtrack(i + 1, path + s[i])

#     backtrack(0, "")

#     return permutations


assert string_permutations("c7w2") == ["c7w2", "c7W2", "C7w2", "C7W2"]
