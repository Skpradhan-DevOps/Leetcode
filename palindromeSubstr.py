class Solution:
    def longestPalindrome(self, s):
        
        
# printing original string 
        print("The original string is : " + str(test_str))
  
# Get all substrings of string
# Using list comprehension + string slicing
        res = [test_str[i: j] for i in range(len(test_str))
                 for j in range(i + 1, len(test_str) + 1)]
  
# printing result 
        print("All substrings of string are : ",res)

        l=1
        size=[]
        palindrome={}
        for i in res:
            if i==i[::-1]:
                palindrome.update({i:len(i)})
                size.append(len(i))


#keys=palindrome.keys()
#values=palindrome.values()


        for a in size:
            if a>l:
                l=a
        print(l)
        for i in palindrome:
            if palindrome[i]==l:
                print("The Longest Palindrome is:",i)


test_str=input("Enter a Strng to find longest palindrome substring:")
sol=Solution()
sol.longestPalindrome(test_str)



    

