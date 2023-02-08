## Japanese Magic Squares

def verifysquare(given_matrix):
    sums = []
    rowsums = [sum(given_matrix[i]) for i in range(0, len(given_matrix))]
    sums.append(rowsums)
    colsums = [sum([row[i] for row in given_matrix]) for i in range(0, len(given_matrix))]
    sums.append(colsums)
    primary_diagonal = sum([given_matrix[i][i] for i in range(0,len(given_matrix))])
    sums.append([primary_diagonal])
    secondary_diagonal = sum([given_matrix[i][len(given_matrix) - 1 - i] for i in range(0,len(given_matrix))])
    sums.append([secondary_diagonal])
    flattened = [j for i in sums for j in i]

    return(len(list(set(flattened))) == 1)

if __name__ == "__main__":
    import numpy as np
    size_by = (3,3)
    square = np.arange(1, 10).reshape(size_by)
    luoshu = np.array([4,9,2,3,5,7,8,1,6]).reshape(3,3)

    print(verifysquare(luoshu))


