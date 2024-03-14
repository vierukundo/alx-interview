#!/usr/bin/python3
"""
 Prime Game
"""


def determine_winner(n):
    """Return the player with more wins"""
    if n < 2:
        return 'Ben'
    players = {'Maria': 0, 'Ben': 0}
    prime = [True for i in range(n+1)]
    p = 2
    player = 'Maria'
    while (p <= n):
        if prime[p]:
            if player == 'Maria':
                players['Maria'] += 1
                last_player = player
                player = 'Ben'
            else:
                players['Ben'] += 1
                last_player = player
                player = 'Maria'
            prime[p] = False

            # Update all multiples of p
            if p * p <= n:
                for i in range(p * p, n+1, p):
                    prime[i] = False
        p += 1
    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Ben'] > players['Maria']:
        return 'Ben'
    else:
        return last_player  # last played player


def isWinner(x, nums):
    """Returns the winner of the game"""
    players = {'Maria': 0, 'Ben': 0}
    for i in range(x):
        winner_of_round = determine_winner(nums[i])
        players[winner_of_round] += 1
    if players['Maria'] == players['Ben']:
        return None  # Winner cannot be determined
    return max(players, key=players.get)  # Return player with max wins
