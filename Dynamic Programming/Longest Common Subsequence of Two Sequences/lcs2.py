# python3


def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100

    return lcs(first_sequence, second_sequence)


def lcs(first_sequence, second_sequence):
    shared_numbers = get_shared_numbers(first_sequence, second_sequence)
    if len(shared_numbers) == 0 or len(shared_numbers) == 1:
        return len(shared_numbers)
    return len(shared_numbers)


def get_shared_numbers(first_sequence, second_sequence):
    first_length = len(first_sequence)
    second_length = len(second_sequence)
    if first_length == 0 or second_length == 0:
        return []
    matrix = [[0 for i in range(second_length + 1)] for j in range(first_length + 1)]
    count = 0
    shared = []
    for i in range(1, first_length + 1):
        for j in range(1, second_length + 1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif first_sequence[i - 1] == second_sequence[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                if count < matrix[i][j]:
                    count = matrix[i][j]
                    shared.append(second_sequence[j - 1])

            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
    return shared


def lis(sequence):
    subsequence_count = [1] * len(sequence)
    max_subsequence = 0
    for i in range(1, len(sequence)):
        for j in range(0, i):
            if sequence[i] >= sequence[j] and (subsequence_count[i] < subsequence_count[j] + 1):
                subsequence_count[i] = subsequence_count[j] + 1
                if subsequence_count[i] >= max_subsequence:
                    max_subsequence = subsequence_count[i]
    i = len(sequence)
    current_max_amount = float('inf')
    subsequence = []
    while max_subsequence != 0:
        i -= 1
        if subsequence_count[i] == max_subsequence and sequence[i] <= current_max_amount:
            max_subsequence -= 1
            # print("max sub " + str(max_subsequence) + " i " + str(i) + " num " + str(sequence[i]) + " current max " + str(current_max_amount))
            subsequence.append(sequence[i])
            current_max_amount = sequence[i]
    # print("subsequence count " + str(subsequence_count))
    subsequence.reverse()
    # print("subsequence " + str(subsequence))
    return subsequence


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
