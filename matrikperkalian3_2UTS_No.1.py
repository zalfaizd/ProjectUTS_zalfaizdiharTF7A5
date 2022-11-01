# ordo 3x2
mat1 = [
    [1, 0, 1],
    [1, 1, 0],
]

mat2 = [
    [1, 0, 1],
    [0, 1, 1],
    [1, 0, 1],
]

mat3 = []

print("Perkalian Matrik A * Matrik B")
for b in range(0,len(mat1)):
    row = []
    for k in range(0, len(mat1[0])):
        total = 0
        for z in range(0, len(mat1[1])):
            total = total + (mat1[b][z] * mat2[z][k] )
        row.append(total)
    mat3.append(row)

for b in range(0,len(mat3)):
    for k in range(0,len(mat3[0])):
        print (mat3[b][k], end='  ')
    print()















