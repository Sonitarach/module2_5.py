import random
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for g in range(m):
            matrix[i].append(value)
    return matrix

result1 = get_matrix(6, 8, 10)
result2 = get_matrix(3, 5, 7)
result3 = get_matrix(8, 2, 13)
print(result1)
print(result2)
print(result3)