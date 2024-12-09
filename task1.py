#Задание 1 
x = int(input("Введите число x: "))
y = int(input("Введите число y: "))

def numberLength(x,y):
   if x > y:
      return print(f'Число {x} больше числа {y}')

   for i in range(x,y+1):
      print('x =', i);

numberLength(x,y)