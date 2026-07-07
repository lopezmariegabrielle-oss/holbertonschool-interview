#!/usr/bin/python3
"""
Module pour la fonction makeChange
"""


def makeChange(coins, total):
    """
    Détermine le nombre minimum de pièces nécessaires pour atteindre le total
    """
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    return dp[total] if dp[total] != total + 1 else -1
