coins = [10, 5, 2, 1]

amount = 28

for coin in coins:
    while amount >= coin:
        print(coin, end=" ")
        amount -= coin
