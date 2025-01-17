#1
arr = [int(input('Введите целое число: ')) for i in range(4)]

def reversArray(array):
   maxNum = 0

   for i in range(0,len(array)):
      
      if array[0]:
         maxNum = array[0]

      if array[i] > maxNum:
         maxNum = array[i]

   return print(f'Максимальный элемент: {maxNum}. Массив: {array.reverse()}')

reversArray(arr)

