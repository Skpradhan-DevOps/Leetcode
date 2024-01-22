class Solution:
    def reverse(self, x):
        strdigit=str(x)
        revdigit=""
        if strdigit[0]=="-":
            revdigit="-"+strdigit[:0:-1]
        else:
            revdigit=(strdigit[::-1])
            
        revdigit=revdigit.lstrip("0")
        print("Reverse digit is:",revdigit)





digit=int(input("Enter a number to be reversed:"))
sol=Solution()
sol.reverse(digit)
          
