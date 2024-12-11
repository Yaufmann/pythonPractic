n = int(input('Введите число: '))

def functionNum(n):

   if n >= 9:
      return print('Число больше 9') 

   number = ''  
   
   for i in range(1,n+1):

      number += str(i) 
      resultString = number.strip()
      numberList = list(resultString)
      
      for i in numberList:
         if i != 9:
            numberList.remove(i)
            numberList.insert(int(i)-1,9)   
      
      convertedList = map(str,numberList)
      result = ''.join(convertedList)

      print(result)

functionNum(n)