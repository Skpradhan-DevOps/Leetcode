def dutch_flag_sort(balls):
    if len(balls) > 1:
        
        mid=len(balls)//2
        L=balls[mid:]
        M=balls[:mid]
    
        dutch_flag_sort(L)
        dutch_flag_sort(M)
    
        i=j=k=0
    
        while i<len(L) and j<len(M):
            
            if ord(L[i])>ord(M[j]):
                
                balls[k]=L[i]
                i+=1
            else:
               
                balls[k]=M[j]
                j+=1
            k+=1
        
        while i<len(L):
           
            balls[k]=L[i]
            i+=1
            k+=1
        while j<len(M):
            balls[k]=M[j]
            j+=1
            k+=1
        
    """
    Args:
     balls(list_char)
    Returns:
     list_char
    """
    # Write your code here.
# Print the array
    print("Sorted array is: ")
    for i in range(len(balls)):
        print(balls[i], end=" ")
        


# Driver program
if __name__ == '__main__':
    a = ["R", "G", "B"]

    dutch_flag_sort(a)


    
    
