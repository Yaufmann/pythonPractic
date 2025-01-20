def recursivelyFunc(arr, l):                 

    if l == 1:                               
        return arr[l-1]                                                          
    else:                                                                      
        previous = recursivelyFunc(arr, l-1)                                
        current = arr[l-1]                                                       
        if previous > current:                                                 
            return previous                                                    
        else:                                                                  
            return current           

print(recursivelyFunc([10,20,30,0,15,10],6))                      