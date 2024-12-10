#Задание 5

N = int(input('Введите число: '))

sum = 0
for i in range(N+1):
  
  if i == 0: 
    continue
  
  print(f"Итерация {i}: {i}^3") 
  sum += i**3

print(f"Сумарная сумма: {sum}")
