# python3


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    all_parents = [None] * (n + 1)
    all_min_ops = [0] + [None] * n
    print("=========")
    print("n = " + str(n))
    print("all_parents " + str(all_parents))
    print("all_min_ops " + str(all_min_ops))

    for k in range(1, n + 1):
        print("__ k = " + str(k))
        curr_parent = k - 1
        curr_min_ops = all_min_ops[curr_parent] + 1

        if k % 3 == 0:
            parent = k // 3
            print("mod 3 parent " + str(parent))
            num_ops = all_min_ops[parent] + 1
            if num_ops < curr_min_ops:
                print("more optimal")
                curr_parent, curr_min_ops = parent, num_ops

        if k % 2 == 0:
            parent = k // 2
            print("mod 2 parent " + str(parent))
            num_ops = all_min_ops[parent] + 1
            if num_ops < curr_min_ops:
                print("more optimal")
                curr_parent, curr_min_ops = parent, num_ops
        print("current min ops " + str(curr_min_ops))
        print("parent min ops " + str(curr_parent))

        print("all_parents " + str(all_parents))
        print("all_min_ops " + str(all_min_ops))

        all_parents[k], all_min_ops[k] = curr_parent, curr_min_ops

        print("\nall_parents " + str(all_parents))
        print("all_min_ops " + str(all_min_ops))

    numbers = []
    k = n
    while k > 0:
        numbers.append(k)
        k = all_parents[k]
    numbers.reverse()
    print("numbers: " + str(numbers))
    for i in range(5):
        print()

    return numbers


def button_value(value, button):
    if button == 1:
        return 1
    elif button == 2:
        return value
    elif button == 3:
        return  value * 2


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
