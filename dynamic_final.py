import math

def calculate_change(amount, coins):
    # init cache with the same number in indexes as the value of amount
    i = 0
    while i < amount+1:
        # if the amount is 0, set first index to 0
        if i == 0:
            cache.append(0)
        else:
            # set each index value as inf
            cache.append(math.inf)
        i += 1
    # loop through each value in the range of the target amount
    for n in range(1, amount + 1):
        # set a minimum amount of infinity
        minimum = math.inf
        # loop through the range of the length of the coins array
        for c in range(len(coins)):
            # if a coin value is <= n
            if coins[c] <= n:
                # set the minimum to the current value of n 
                # minus the value of the current coin
                minimum = min(minimum, cache[n - coins[c]])
        # Update cache
        cache[n] = 1 + minimum
                

    print(cache)
    return(cache[amount])

coins = [1,5,10,25]
amount = 6
cache =[]
expecting = 2



print(f'To return {amount} it would take {calculate_change(amount, coins)} coins')
