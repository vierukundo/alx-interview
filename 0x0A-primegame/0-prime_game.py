#!/usr/bin/python3
"""
 Prime Game
"""


def determine_winner(n, rounds):
    """Return the player with more wins"""
    players = {'Maria': 0, 'Ben': 0}
    for _ in range(rounds):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not primes
        for p in range(2, n + 1):
            if primes[p]:
                if p * p <= n:
                    for i in range(p * p, n + 1, p):
                        primes[i] = False
                if players['Maria'] == players['Ben']:
                    players['Maria'] += 1
                else:
                    players['Ben'] += 1
    return 'Maria' if players['Maria'] > players['Ben'] else 'Ben'


def isWinner(x, nums):
    """Returns the winner of the game"""
    players = {'Maria': 0, 'Ben': 0}
    for n in nums:
        winner_of_round = determine_winner(n, x)
        players[winner_of_round] += 1
    if players['Maria'] == players['Ben']:
        return None  # Winner cannot be determined
    return max(players, key=players.get)  # Return player with max wins
