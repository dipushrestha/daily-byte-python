"""
This question is asked by Google. You are given a bag of coins, an initial
energy of E, and want to maximize your number of points (which starts at zero).
To gain a single point you can exchange coins[i] amount of energy (i.e. if I
have 100 energy and a coin that has a value 50 I can exchange 50 energy to
gain a point). If you do not have enough energy you can give away a point in
exchange for an increase in energy by coins[i] amount (i.e. you give away a
point and your energy is increased by the value of that coin: energy += coins[i]).
Return the maximum number of points you can gain.
Note: Each coin may only be used once.

Ex: Given the following coins and starting energy…

coins = [100, 150, 200] and E = 150, return 1
coins = [100,200,300,400] and E = 200, return 2
coins = [300] and E = 200, return 0
"""


def max_points(coins, energy):
    coins.sort()
    left, right = 0, len(coins) - 1
    points, max_points = 0, 0

    while left <= right:
        if coins[left] <= energy:
            energy -= coins[left]
            points += 1
            max_points = max(max_points, points)
            left += 1
        elif points > 0:
            energy += coins[right]
            points -= 1
            right -= 1
        else:
            break

    return max_points


assert max_points([100, 150, 200], 150) == 1
assert max_points([100, 200, 300, 400], 200) == 2
assert max_points([300], 200) == 0
