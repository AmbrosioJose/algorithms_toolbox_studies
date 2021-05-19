# python3


def change_naive(money):
    min_coins = float("inf")
    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    print(min(min_coins, num1 + num3 + num4))
                    min_coins = min(min_coins, num1 + num3 + num4)
    return min_coins


def change(money):
    coins = [1, 3, 4]
    return dynamic_change(money, coins,)


def dynamic_change(money, coins,):
    min_array = [float("inf")] * (money + 1)
    min_array[0] = 0
    if money == 0:
        return 0
    for m in range(1, money + 1):
        for coin in coins:
            if m >= coin:
                num_coins = min_array[m - coin] + 1
                if num_coins < min_array[m]:
                    min_array[m] = num_coins
    # print("money " + str(money) + " min_num_coins " + str(min_array))
    return min_array[money]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
