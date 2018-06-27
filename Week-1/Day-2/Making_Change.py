#5 Making Change

def change_possibilities(amount, denominations):
    """
    Computes the number of ways to make amount of money with coins of the available denominations.
    Dynamic space efficient programming solution
    """
    if (len(denominations) == 0) or (amount < 0):
        return 0

    results = [0 for x in range(amount+1)]

    # Fill the entries for 0 value case (amount = 0)
    results[0] = 1

    for coin in denominations:
        for next_amount in range(coin, amount + 1):
            remainder = next_amount - coin
            results[next_amount] += results[remainder]

    return results[amount]
