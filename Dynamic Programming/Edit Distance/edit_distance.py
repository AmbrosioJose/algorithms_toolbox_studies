# python3


def edit_distance(first_string, second_string):
    # print("\nfirst: " + first_string + " second: " + second_string)
    firstLength = len(first_string)
    secondLength = len(second_string)
    matrix = [[0 for i in range(firstLength + 1)] for j in range(secondLength + 1)]
    for i in range(secondLength + 1):
        matrix[i][0] = i
    for i in range(firstLength + 1):
        # print(i)
        matrix[0][i] = i
    # print(matrix)
    for j in range(1, secondLength + 1):
        for i in range(1, firstLength + 1):
            insertion = matrix[j - 1][i] + 1
            deletion = matrix[j][i - 1] + 1
            match = matrix[j - 1][i - 1]
            mismatch = matrix[j - 1][i - 1] + 1
            if first_string[i - 1] == second_string[j - 1]:
                matrix[j][i] = min(insertion, deletion, match)
            else:
                matrix[j][i] = min(insertion, deletion, mismatch)
    # print("result: ")
    # for i in matrix:
    #     print(i)
    return matrix[secondLength][firstLength]



if __name__ == "__main__":
    print(edit_distance(input(), input()))
