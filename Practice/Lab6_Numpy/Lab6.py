import numpy as np

def ex1(arr):
    arr[arr % 2 != 0] = -1
    return arr

def ex2(arr, n):
    arr = arr.reshape(n, n)
    return arr

def ex3(n, i, k):
    return np.random.randint(i, k + 1, n)

def ex4(arr, k):
    return arr[:, k - 1]

def ex5(arr):
    unique_rows = np.array([row for row in arr if len(set(row)) == len(row)])
    return unique_rows

def ex6(arr):
    num_rows = arr.shape[0]
    row_prods = np.zeros(num_rows)
    for i in range(num_rows):
        prod = 1
        for j in arr[i]:
            prod *= j
        row_prods[i] = prod
    return row_prods

def ex7(arr):
    condition = (arr >= 20) & (arr <= 50)
    return np.sum(arr[condition])

def ex8(arr):
    return arr[::-1]

def ex9(arr):
    row_sums = np.sum(arr, axis = 1)
    max_sum = row_sums[0]
    max_index = 0
    for i in range(1, len(row_sums)):
        if row_sums[i] > max_sum:
            max_sum = row_sums[i]
            max_index = i
    return max_index, max_sum

def ex10(arr):
    size = len(arr)
    diag_matrix = np.zeros((size, size))
    for i in range(size):
        diag_matrix[i, i] = arr[i]
    return diag_matrix


if __name__ == "__main__":
    m, n = 5, 6
    matrix = np.random.randint(10, 101, size=(m, n))
    print(matrix, end = '\n\n')
    print(ex5(matrix))
    print(ex7(matrix))