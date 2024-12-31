'''
This question is asked by Amazon. Given a string representing the sequence 
of moves a robot vacuum makes, return whether or not it will return to its 
original position. The string will only contain L, R, U, and D characters, 
representing left, right, up, and down respectively.

Ex: Given the following strings...

"LR", return true
"URURD", return false
"RUULLDRD", return true
'''

def vacuum_cleaner_route(moves):
    x, y = 0, 0
    for move in moves:
        if move == "L": x -= 1
        elif move == "R": x += 1
        elif move == "U": y -= 1
        elif move == "D": y += 1
    return x == 0 and y == 0

assert vacuum_cleaner_route("LR") == True
assert vacuum_cleaner_route("URURD") == False
assert vacuum_cleaner_route("RUULLDRD") == True
