def searchLetter(string): 

   arr = string.split(' ')
   count = 0
   
   for element in range(0,len(arr)):
      
      if arr[element][0] == 'е':
         count += 1
   
   return print(f'Количество слов начинающихся с буквы - е: {count}')

searchLetter('Строка ео еловом екид е словом ехон!')