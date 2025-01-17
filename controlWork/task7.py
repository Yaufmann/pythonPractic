#Задание 7

n = int(input("Введите число: "))
summ = 1
current = 1
print(f"Факториал числа 1! равен {current}")
for i in range(2,n+1):
   current *= i
   summ += current
   print(f"Факториал числа {i}! равен {current}")   
print(f"Общая сумма факториалов: {summ}")   


     
   

      
      
      


