class Solution:
    def threeSumClosest(self, nums, target):
        diffDict={}
        l1=len(nums)
        threeSum=[]
        for i in range(l1):
            for j in range(i+1,l1):
                for k in range(j+1,l1):
                    threeSum=nums[i]+nums[j]+nums[k]
                    diff=abs(target-threeSum)
                    diffDict.update({threeSum:diff})

        print(diffDict)
        value=list(diffDict.values())
        print(value)
        key=list(diffDict.keys())
        print(key)
        miniDiff=min(value)
        print(miniDiff)
        pos=value.index(miniDiff)
        sumClose=key[pos]
        return sumClose


nums=[0,0,0]
target=1
sol=Solution()
print(sol.threeSumClosest(nums,target))
