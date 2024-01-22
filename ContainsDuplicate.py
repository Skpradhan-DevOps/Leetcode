class Solution:
    def containsDuplicate(nums):
        temp=set()
        for i in nums:
            if i in temp:
                return True
            else:
                temp.add(i)
            
        return False
