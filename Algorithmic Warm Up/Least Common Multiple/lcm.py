# python3


def lcm_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple


def lcm(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    larger = 0
    smaller = 0
    if a > b:
        smaller, larger = b, a
    else:
        smaller, larger = a, b
    least = 1
    is_lcm = False
    while not is_lcm:
        possible_lcm = least * larger
        if (possible_lcm % smaller) == 0:
            is_lcm = True
        least += 1
    return least * larger



if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))
