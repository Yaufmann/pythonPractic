#Задание 9

def fibbonaci(n):

   if (n <= 1):
      return n
   else:
      return(fibbonaci(n-1)+fibbonaci(n-2))

n = int(input("Введите число: "))
sum = 0

print("Последовательность Фиббоначи:")

for i in range(n):
   
   sum += fibbonaci(i)
   print(fibbonaci(i))

print(f"Сумма чисел: {sum}")
