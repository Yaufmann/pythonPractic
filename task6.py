#Задание 6

x = int(input("Введите число x: "))

def numberLength(x):  
      pow = 1

      for i in range(0,x+1):
         if i == 1 or i == 0:
           continue   
         pow *= i

      print(f'Факториал числа: {x}!, является = {pow}')

numberLength(x)