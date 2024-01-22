n=int(input("Enter a range for nums list:"))
nums=[]
for i in range(0,n):
    num=int(input("enter numbers:"))
    nums.append(num)
print(nums)
target=int(input("Enter a target: "))

class Solution:
   def __init__(self, nums, target):
       self.nums=nums
       self.target=target
   
   
   def twoSum(self):
       l=[]
       output=[]
       for i in self.nums:
           for j in self.nums:
               if i!=j and i+j==self.target:
                   l.append(i)
                   l.append(j)
                    
       values=list(set(l))
       for i in values:
           ind=self.nums.index(i)
           output.append(ind)
       print(sorted(output)) 



solution= Solution(nums,target)
solution.twoSum()
