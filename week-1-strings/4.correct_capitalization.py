'''
This question is asked by Google. Given a string, return whether or not it uses
capitalization correctly. A string correctly uses capitalization if all letters
are capitalized, no letters are capitalized, or only the first letter is capitalized.

Ex: Given the following strings...

"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true
'''

def correct_capitalization(x):
    if not x: return False
    return (
        x.isupper() or
        x.islower() or 
        (x[0].isupper() and x[1:].islower())
    )

assert correct_capitalization("USA") == True
assert correct_capitalization("Calvin") == True
assert correct_capitalization("compUter") == False
assert correct_capitalization("coding") == True
assert correct_capitalization("uSA") == False
assert correct_capitalization("cAlvin") == False
