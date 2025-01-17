#2
length = int(input('Введите длину массива: '))
arr = [int(input('Введите целое число: ')) for i in range(length)]

def zeroSummArr(array):

   summ = 0
   
   for i in range(len(array)):
      summ += array[i]
  
   avgSumm = summ / len(array)

   for i in range(len(array)):
      if array[i] == 0:
         array[i] = avgSumm

   return print(f'Среднее арифметическое: {avgSumm}. Новый массив: {array}')

zeroSummArr(arr)
