def distinctSubstring(P, N):
       S=dict()
       max=dict()
       l=1
       key_list=[]
       val_list=[]
       position=0
    # Hashmap to store all substrings

 
    # Iterate over all the substrings
       for i in range(N):
 
        # Boolean array to maintain all
        # characters encountered so far
           freq = [False]*26
 
        # Variable to maintain the
        # subtill current position
           s = ""
 
           for j in range(i,N):
 
            # Get the position of the
            # character in the string
               pos = ord(P[j]) - ord('a')
 
            # Check if the character is
            # encountred
               if (freq[pos] == True):
                   break
 
               freq[pos] = True
 
            # Add the current character
            # to the substring
               s += P[j]
            #print(s)
            #print(len(s))
               max.update({s:len(s)})
               if len(s) > l:
                   l=len(s)
 
            # Insert subin Hashmap
               S[s] = 1
    #To find out the substring, next 4 lines
    #key_list= list(max.keys())
    #val_list= list(max.values())
    #position= val_list.index(l)
    #return key_list,val_list,key_list[position]
       return l
    #len(S)

 
# Driver code
S = input("Enter a String:")
N = len(S)
#solution=Solution()
print(distinctSubstring(S,N))

