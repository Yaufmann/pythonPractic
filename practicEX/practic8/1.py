A = []
n = 4
for i in range(n):
    B = []
    for j in range(n):
        if j == 0 or j == n - 1:
            B.append(-2)
        else:
            B.append(int(input('Введите положительное число: ')))
    A.append(B)

for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()

sum = 0
count = 0
countMin = 0

for i in range(n):
     for j in range(n):
        if i < j:
            if A[i][j] > 0:
                count += 1
                sum += A[i][j]
            else:
                countMin += 1
    

print(f'Сумма чисел выше диагонали: {sum}.')
print(f'Счетчик отрицательных чисел: {count}.')
print(f'Счетчик положительных чисел: {countMin}.')