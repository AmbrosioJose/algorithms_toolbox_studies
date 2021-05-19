# python3

from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    matrix = [[0 for i in range(capacity + 1)] for j in range(len(weights) + 1)]
    print("capacity " + str(capacity) + " weights " + str(weights) + " length " + str(len(weights)) + " at 0 " + str(weights[0]))
    for row in matrix:
        print(row)
    for i in range(1, len(weights) + 1):
        print("---------------")
        for row in matrix:
            print(row)
        for j in range(1, capacity + 1):
            matrix[i][j] = matrix[i - 1][j]
            print("i " + str(i) + " weights[i - 1] " + str(weights[i - 1]) + " j " + str(j) + " weights[i - 1] <= j " + str(weights[i - 1] <= j))
            if weights[i - 1] <= j:
                val = matrix[i - 1][j - weights[i - 1]] + weights[i - 1]
                print("val: " + str(val))
                if matrix[i][j] < val:
                    matrix[i][j] = val
    for row in matrix:
        print(row)
    return matrix[-1][-1]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
