# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    total_value = 0
    loot = []

    for i in range(len(prices)):
        loot.append((weights[i], prices[i]))
    loot.sort(key=lambda x: x[1] / x[0], reverse=True)
    # print(loot)
    # value_string = ""
    # for i in range(len(weights)):
    #     value_string = value_string + str(loot[i][1] / loot[i][0]) + ", "
    # print(value_string)
    # print()
    for i in range(len(weights)):
        if capacity == 0:
            return total_value
        adding_weight = min(loot[i][0], capacity)
        total_value = total_value + (adding_weight * (loot[i][1] / loot[i][0]))
        loot[i] = (loot[i][0] - adding_weight, loot[i][1])
        capacity = capacity - adding_weight
    return total_value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
