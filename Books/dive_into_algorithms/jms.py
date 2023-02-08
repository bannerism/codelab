## Japanese Magic Squares

def row_sums(given_matrix):
    sums = []
    rowsums = [sum(given_matrix[i]) for i in range(0, len(given_matrix))]
    sums.append(rowsums)
    return sums
    
def col_sums(given_matrix):
    sums = []
    colsums = [sum([row[i] for row in given_matrix]) for i in range(0, len(given_matrix))]
    sums.append(colsums)
    return sums

def major_sums(given_matrix):
    sums = []
    major_diagonal = sum([given_matrix[i][i] for i in range(0, len(given_matrix))])
    sums.append([major_diagonal])
    return sums

def minor_sums(given_matrix):
    sums = []
    minor_diagonal = sum([given_matrix[i][len(given_matrix) - 1 - i] for i in range(0, len(given_matrix))])
    sums.append([minor_diagonal])
    return sums

def flatten(sums):
    flattened = [j for i in sums for j in i]
    return flattened

def verify_square(given_matrix):
    sums = []
    sums.append(row_sums(given_matrix))
    sums.append(col_sums(given_matrix))
    sums.append(major_sums(given_matrix))
    sums.append(minor_sums(given_matrix))    
    flattened = flatten(sums)[0]
    return (len(list(set(flattened))) == 1)

if __name__ == "__main__":
    import numpy as np
    size_by = (3,3)
    square = np.arange(1, 10).reshape(size_by)
    luoshu = np.array([4,9,2,3,5,7,8,1,6]).reshape(3,3)

    print(verify_square(luoshu))


