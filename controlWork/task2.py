#Задание 2

x = int(input("Введите число x: "))
y = int(input("Введите число y: "))

def numberLength(x,y):  

   if x > y:
      for i in range(x,y-1,-1):
         print('x =', i);
   elif x < y:
      for i in range(x,y+1):
         print('x =', i);

numberLength(x,y)