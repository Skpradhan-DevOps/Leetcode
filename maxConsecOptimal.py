class Solution:
    def findMaxConsecutiveOnes(self, nums):
        numMax=0
        p1=0

        for p2, num in enumerate(nums):
            if num == 0:
                p1 = p2+1
            numMax = max(numMax, p2-p1+1)
        return numMax

nums=[0,0]
sol= Solution()
print(sol.findMaxConsecutiveOnes(nums))
