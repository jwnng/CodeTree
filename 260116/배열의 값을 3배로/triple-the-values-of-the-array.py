matrix = []
rows = 3
cols = 3

matrix = [list(map(int,input().split())) for _ in range(rows)]


new_matrix = [
    [i * 3 for i in row]
    for row in matrix
]

# new_matrix = []
# for i in range(rows):
#   new_row = []
#   for j in range(cols):
#       new_row.append(matrix[i][j] * 3)
#   new_matrix.append(new_row)

for i in range(rows):
    for j in range(cols):
        print(new_matrix[i][j],end=" ")
    print()