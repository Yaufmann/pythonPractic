#2
oneArr = []
twoArr = []
threeArr = []

for i in range(3):
   length = int(input('Введите длину массива до 15 включительно: '))
   arr = [int(input('Введите целое число: ')) for i in range(length)]
   if i == 0:
      oneArr = arr
   if i == 1:
      twoArr = arr
   if i == 2:
      threeArr = arr   

def summThreeArr(arr1,arr2,arr3):

   summArray = []
   summArray.append(arr1)
   summArray.append(arr2)
   summArray.append(arr3)
  
   summArr1 = 0
   summArr2 = 0
   summArr3 = 0
   avgSumm1 = 0
   avgSumm2 = 0
   avgSumm3 = 0

   for i in range(len(summArray)):
      
      if i == 0:
         for j in range(len(summArray[i])):   
            summArr1 += summArray[0][j]
         
         avgSumm1 = summArr1 / len(summArray[i])
         
      if i == 1:
         for j in range(len(summArray[i])):   
            summArr2 += summArray[1][j]

         avgSumm2 = summArr2 / len(summArray[i])
         
      if i == 2:
         for j in range(len(summArray[i])):
            summArr3 += summArray[2][j]

         avgSumm3 = summArr3 / len(summArray[i])


   return print(f'Сумма массива1: {summArr1}. Среднее арифметическое массива1: {avgSumm1}.\nСумма массива2: {summArr2}. Среднее арифметическое массива2: {avgSumm2}.\nСумма массива3: {summArr3}. Среднее арифметическое массива3: {avgSumm3}.')

summThreeArr(oneArr,twoArr,threeArr)