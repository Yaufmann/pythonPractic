A = int(input('Введите количество строк: '))
B = int(input('Введите количество столбцов: '))

def matrixElement(A,B):
    C = []
    for i in range(A):
        D = []
        for j in range(B):
            D.append(int(input('Введите число: ')))
        C.append(D)

    for i in range(A):
        maxElementString = max(C[i])
        minElementString = min(C[i])

        indexMax = C[i].index(maxElementString)
        C[i][indexMax] = C[i][0]
        C[i][0] = maxElementString

        indexMin = C[i].index(minElementString)
        C[i][indexMin] = C[i][-1]
        C[i][-1] = minElementString

    for i in range(A):
        for j in range(B):
            print(C[i][j], end=' ')
        print()
    
    return C

print(matrixElement(A,B))