'''
This question is asked by Amazon. Given a string representing your stones 
and another string representing a list of jewels, return the number of stones 
that you have that are also jewels.

Ex: Given the following jewels and stones...

jewels = "abc", stones = "ac", return 2
jewels = "Af", stones = "AaaddfFf", return 3
jewels = "AYOPD", stones = "ayopd", return 0
'''

def jewels_and_stones(jewels, stones):
    jewels_set = set(jewels)
    num_stones_with_jewels = 0
    for stone in stones:
        if stone in jewels_set: 
            num_stones_with_jewels += 1
    return num_stones_with_jewels


assert jewels_and_stones("abc", "ac") == 2
assert jewels_and_stones("Af", "AaaddfFf") == 3
assert jewels_and_stones("AYOPD", "stones") == 0
