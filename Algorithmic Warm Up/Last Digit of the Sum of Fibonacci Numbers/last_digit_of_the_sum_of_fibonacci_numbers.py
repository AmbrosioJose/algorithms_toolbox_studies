# python3


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n
    else:
        # last digits will be in between 0 and 10
        return fibonacci_number_again(n, 10)


def fibonacci_number_again(n, m):
    # find period for m (note: each period starts with 01)
    period_length = 0
    i = 2
    period_list = [0, 1]
    while not period_length:
        # save
        period_list.append((period_list[i - 1] + period_list[i - 2]) % m)
        # check if a iterate through first period
        if period_list[i] == 1 and period_list[i - 1] == 0:
            period_length = i - 1
        # return if fib mod number is found before period
        if not period_length and i == n:
            return period_list[n]
        i += 1
    print(period_length)
    # find remainder of (n / length of period)
    remainder = n % period_length
    # Fib for remainder mod m
    return period_list[remainder]


def multiple_2x2_matrices_mod10(a, b):
    c = [[None] * 2 for _ in range(2)]
    c[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % 10
    c[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % 10
    c[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % 10
    c[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % 10
    return c


def matrix_exponent_mod10(d, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    elif (n % 2) == 0:
        z = matrix_exponent_mod10(d, n//2)
        a = multiple_2x2_matrices_mod10(z, z)
        print("a: =")
        print(a)
        print("")
        return a
    else:
        z = matrix_exponent_mod10(d, n//2)
        y = multiple_2x2_matrices_mod10(z, z)
        a = multiple_2x2_matrices_mod10(y, d)
        print("a: =")
        print(a)
        print("")
        return a


def fib_number_matrix(n):
    m = [[0, 1], [1, 1]]
    p = matrix_exponent_mod10(m, n + 2)
    return (p[1][0] + 9) % 10


if __name__ == '__main__':
    input_n = int(input())
    print(fib_number_matrix(input_n))
