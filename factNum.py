class Solution:
    def factNum(self, num):
        #fact= num * factNum(num-1)
        fact=1
        for i in range(1, num+1):
            fact=fact*(i)
        return fact
    def factRec(self, num):
        while num>1:
            fact= num * factRec(num-1)

        return fact

    def recur_factorial(self, num):
       if num == 1 or num == 0:
           return 1
       else:
           return num*self.recur_factorial(num-1)
            

num=5
sol= Solution()
print(sol.factNum(num))
print(sol.recur_factorial(num))
