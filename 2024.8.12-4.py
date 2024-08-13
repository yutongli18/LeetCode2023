def arrange_coins(n):
    # Initialize the row count
    row = 0
    # Loop through the coins, increasing the row count until we run out of coins
    while n > row:
        row += 1
        n -= row
    # Return the total number of complete rows
    return row


if __name__ == '__main__':
    n = int(input())
    print(arrange_coins(n))
