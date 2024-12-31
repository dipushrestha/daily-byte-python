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
