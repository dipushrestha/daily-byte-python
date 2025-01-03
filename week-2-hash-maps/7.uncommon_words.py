'''
This question is asked by Amazon. Given two strings representing sentences, 
return the words that are not common to both strings (i.e. the words that only 
appear in one of the sentences). You may assume that each sentence is a 
sequence of words (without punctuation) correctly separated using space characters.

Ex: given the following strings...

sentence1 = "the quick", sentence2 = "brown fox", return ["the", "quick", "brown", "fox"]
sentence1 = "the tortoise beat the haire", sentence2 = "the tortoise lost to the haire", return ["beat", "to", "lost"]
sentence1 = "copper coffee pot", sentence2 = "hot coffee pot", return ["copper", "hot"]
'''

# output as per the words order in the sentence
def uncommon_words(sentence1, sentence2):    
    sentence1_words = sentence1.split(" ")
    sentence2_words = sentence2.split(" ")
    intersection_set = set(sentence1_words) & set(sentence2_words)
    return [word for word in sentence1_words + sentence2_words if word not in intersection_set]


assert uncommon_words("the quick", "brown fox") == ["the", "quick", "brown", "fox"]
assert uncommon_words("the tortoise beat the haire", "the tortoise lost to the haire") == ["beat", "lost", "to"]
assert uncommon_words("copper coffee pot", "hot coffee pot") == ["copper", "hot"]
