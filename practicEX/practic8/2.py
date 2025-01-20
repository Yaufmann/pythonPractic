A = int(input('Введите количество строк: '))
B = int(input('Введите количество столбцов: '))

C = []
for i in range(A):
    D = []
    for j in range(B):
        D.append(int(input('Введите число: ')))
    C.append(D)

print(type(C[i]))
print(max(C[0]))
for i in range(A):
    maxElementString = max(C[i])
    minElementString = min(C[i])

    for j in range(B):
        if C[i][j] == C[i][0]:
            index = C[i].index(maxElementString)
            #C[i].insert(index,C[i][0])
            C[i][index] = C[i][0]
            C[i][0] = maxElementString
        if C[i][j] == C[i][-1]:
            index = C[i].index(minElementString)
            #C[i].insert(index,C[i][-1])
            C[i][index] = C[i][-1]
            C[i][0] = minElementString

for i in range(A):
    for j in range(B):
        print(C[i][j], end=' ')
    print()