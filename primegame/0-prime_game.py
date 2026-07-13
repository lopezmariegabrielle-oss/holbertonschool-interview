#!/usr/bin/python3
"""
Module pour résoudre le problème du Prime Game.
"""


def isWinner(x, nums):
    """
    Détermine le gagnant d'un jeu de nombres premiers après x rounds.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)

    primes = [True] * (max_num + 1)
    if max_num >= 0:
        primes[0] = False
    if max_num >= 1:
        primes[1] = False

    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    prime_counts = [0] * (max_num + 1)
    current_count = 0
    for i in range(len(primes)):
        if primes[i]:
            current_count += 1
        prime_counts[i] = current_count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if x <= 0:
            break
        total_primes = prime_counts[n]
        if total_primes % 2 != 0:
            maria_wins += 1
        else:
            ben_wins += 1
        x -= 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
