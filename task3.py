#Задание 3

x = int(input("Введите число x: "))
y = int(input("Введите число y: "))

def numberLength(x,y):  

   if x > y:
      for i in range(x,y-1,-1):
         if i%2 !=0:
            print('x =', i)
         else:
            continue   

numberLength(x,y)