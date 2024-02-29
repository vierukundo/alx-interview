#!/usr/bin/python3
"""
Count number of coins required to make a given value.
"""


def makeChange(coins, total):
    """Least number of coins to make change"""
    if total <= 0:
        return 0
    number_of_coins = 0

    for coin in sorted(coins, reverse=True):
        while total >= coin:
            number_of_coins += total // coin
            total = total % coin
    if total == 0 and number_of_coins > 0:
        return number_of_coins
    return -1
