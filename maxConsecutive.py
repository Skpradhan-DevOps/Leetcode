class Solution:
    def findMaxConsecutiveOnes(self, nums):
        numMax=0
        p1=p2=0
        count = 0
        for p2 in range(len(nums)):
            if nums[p2] == 1:
                count += 1
        if count == len(nums):
            numMax = count
        elif count == 0:
            numMax = 0
            
        for p2 in range(len(nums)):
            if p2 == len(nums) -1:
                if nums[p1] != nums[p2]: 
                    p = p2-p1
                numMax= max(numMax, p)
                
            if nums[p2] == 0:
                if nums[p1] != nums[p2]:
                    p = p2-p1
                else:
                    p = p2-p1-1
                numMax= max(numMax, p)
                p1 = p2
        return numMax

nums=[0,0]
sol= Solution()
print(sol.findMaxConsecutiveOnes(nums))
