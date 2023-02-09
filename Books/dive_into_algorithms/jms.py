# Japanese Magic Squares

def parse_magic_square(given_matrix):
    row = []
    columns = []
    major_diagonal = []
    minor_diagonal = []

    for i, x in enumerate(given_matrix):
        row.append(sum(x))

        columns.append(sum([row[i] for row in given_matrix]))

        major_diagonal.append(given_matrix[i][i])

        minor_diagonal.append(given_matrix[i][len(given_matrix) - 1 - i])

    return row, columns, [sum(major_diagonal)], [sum(minor_diagonal)]


def verify_equality(sums_of_square):
    sums = []
    for i in sums_of_square:
       for j in i:
           sums.append(j)

    return len(list(set(sums))) == 1


def verify_square(given_matrix):
    sums = parse_magic_square(given_matrix)
    return verify_equality(sums)


if __name__ == "__main__":
    import numpy as np
    size_by = (3, 3)
    square = np.arange(1, 10).reshape(size_by)  # False
    luoshu = np.array([4, 9, 2, 3, 5, 7, 8, 1, 6]).reshape(3, 3)  # True

    print(verify_square(luoshu))
