class Solution:
    def fourSum(self, nums, target):
        l1=len(nums)
        fourSum=[]
        for i in range(l1):
            for j in range(i+1,l1):
                for k in range(j+1,l1):
                    for l in range(k+1,l1):
                        if nums[i]+nums[j]+nums[k]+nums[l]==target:
                            l2=[nums[i],nums[j],nums[k],nums[l]]
                            l2.sort()
                            fourSum.append(l2)
        fourSum_set=set(map(tuple,fourSum))
        fourSum=list(map(list,fourSum_set))

        return fourSum
nums=[2,2,2,2,2]
target=8
sol=Solution()
print(sol.fourSum(nums,target))

        
                            
