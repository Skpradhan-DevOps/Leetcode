class Solution:
    def threeSum(self, nums):
        l1=len(nums)
        threeSum=[]
        for i in range(l1):
            for j in range(i+1,l1):
                for k in range(j+1,l1):
                    if nums[i]+nums[j]+nums[k]==0:
                        l2=[nums[i],nums[j],nums[k]]
                        l2.sort()
                        threeSum.append(l2)
                        

        threeSum_set=set(map(tuple,threeSum))
        threeSum=list(map(list,threeSum_set))

        return threeSum

nums=[0]
sol=Solution()
print(sol.threeSum(nums))
                        
