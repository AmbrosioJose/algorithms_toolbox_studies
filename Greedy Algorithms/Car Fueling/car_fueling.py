# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    num_refill = 0
    current_refill = 0
    stops.insert(0, 0)
    if d < m:
        return 0
    while current_refill <= len(stops) - 1 and (d - stops[current_refill]) > m:
        print("\n====")
        last_refill = current_refill
        while current_refill < (len(stops) - 1) and (stops[current_refill + 1] - stops[last_refill] <= m):
            current_refill = current_refill + 1
            print("+ 1  index = " + str(current_refill) + " " + str(stops[current_refill]))
        print("current refill index " + str(current_refill) + " " + str(stops[current_refill]))
        if current_refill == last_refill:
            print("difference : " + str(d - stops[current_refill]))
            if (d - stops[current_refill]) <= m:
                return num_refill
            return -1
        if stops[current_refill] - stops[last_refill] <= m:
            num_refill = num_refill + 1
            print("•current # of stops " + str(num_refill))
    return num_refill


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
