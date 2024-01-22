class Solution:
    def strToInteger(self,x):
        x=x.strip('\"')
        x=x.strip()
        digit=1
        l=len(x)
        l1=str([0,1,2,3,4,5,6,7,8,9])
        if x[0]=="-":
            for i in range(1,l):
                if x[i] not in l1:
                    x=int(x[1:i])
                    break
            digit="-"+x[1:]
        else:
            for i in range(l):
                if x[i] in l1:
                    digit=x[::]
                else:
                    digit=int(x[:i])
                    break
            
        digit=int(digit)
        print(digit)

a=str(input("Enter the input:"))
sol=Solution()
sol.strToInteger(a)
