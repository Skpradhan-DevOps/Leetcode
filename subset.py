def generate_all_subsets(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    result=[]
    def helper(s,i,slate):
        if i==len(s):
            result.append(slate[:])
            #print(result)
            return
            
        helper(s,i+1,slate)
        
        #print(result)
        

        #slate+s[i]
        for i in range(i,len(s)):
            helper(s,i+1,slate.append(s[i]))
            slate.pop(s[i])
            
        
        
    
    helper(s,0,[])


# Print the array
    print("Subsets are: ")
    print(result)
    '''for i in range(len(result)):
        print(result[i], end=" ")'''


if __name__ == '__main__':
    s= [2,4,8]

    generate_all_subsets(s)
