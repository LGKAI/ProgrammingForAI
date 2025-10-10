import numpy as np

# Viết hàm sắp xếp các phần tử trong hàng của ma trận vuông M x M (M <= 100) theo quy tắc:
# Hàng chỉ toàn số chẵn: sắp xếp giảm dần
# Hàng chỉ toàn số lẻ: sắp xếp tăng dần
# Hàng có số chẵn lẫn số lẻ: thay thế các số âm thành trị tuyệt đối của nó
# Được sử dụng hàm sort của numpy

def custom_sort(matrix):
    for i in range(matrix.shape[0]):
        row = matrix[i]
        if np.all(row % 2 == 0):
            matrix[i] = np.sort(row)[::-1]
        elif np.all(row % 2 != 0):
            matrix[i] = np.sort(row)
        else:
            matrix[i] = np.abs(row)
    return matrix


if __name__ == "__main__":
    # A = np.array([
    #         [2, -4, 8],
    #         [7, 3, 11],
    #         [-1, 6, -10]
    #     ])

    # print(custom_sort(A))

    N = 120
    arr = np.arange(N)
    arr = arr.reshape(8, -1)
    arr = arr.transpose()
    arr = arr.reshape(2, 4, -1)
    # print(arr)
    transposed = arr.transpose((1, 0, 2))
    print(transposed)
    print(transposed[0, 1, 2])