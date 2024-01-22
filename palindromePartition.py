def generate_palindromic_decompositions(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    result=[]
    def partition(s,i,partSlate):
        if i==len(s):
            result.append("|".join(partSlate.copy()))
            return
        for j in range(i,len(s)):
            if isPalindrome(s,i,j):
                partSlate.append(s[i:j+1])
                partition(s,j+1,partSlate)
                partSlate.pop()
                

                
    def isPalindrome(s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            else:
                l+=1
                r-=1
        return True

    partition(s,0,[])

    #result="|".join(result)

    print("Subsets are: ")
    print(result)

    '''for a in result:
        a="|".join(a)
        print(a)'''

    #print(result)
    
if __name__ == '__main__':
    s= "abracadabra"

    generate_palindromic_decompositions(s)
