# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    # find period for m (note: each period starts with 01)
    period_length = 0
    i = 2
    period_list = [0, 1]
    while not period_length:
        period_list.append((period_list[i-1] + period_list[i-2]) % m)
        if period_list[i] == 1 and period_list[i-1] == 0:
            period_length = i - 1
        i += 1
    # # find remainder of (n / length of period)
    remainder = n % period_length
    # Fib for remainder mod m
    return period_list[remainder]


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
