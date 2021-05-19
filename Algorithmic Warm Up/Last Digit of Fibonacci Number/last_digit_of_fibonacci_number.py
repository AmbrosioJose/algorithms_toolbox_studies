# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7
    if n <= 1:
        return n
    else:
        fib_nums = [None] * (n + 1)
        fib_nums[0], fib_nums[1] = 0, 1
        for i in range(2, n + 1):
            fib_nums[i] = (fib_nums[i - 1] + fib_nums[i - 2]) % 10
    return fib_nums[-1]


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
