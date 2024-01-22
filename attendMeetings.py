class Solution:
    def can_attend_all_meetings(self,intervals):
    # Write your code here.
        intervals.sort()
        print(intervals)
    #nextstart = 0
        '''for i in range(len(intervals)):
        if i == len(intervals)-1:
            nextstart = float('inf')
        else:
            nextstart = intervals[i+1][0]
            
        if intervals[i][1] < nextstart:
            return 1'''
        if len(intervals) == 1:
            return 1

        print(len(intervals))
        
        for i in range(1,len(intervals)):
            print(intervals[i][0],intervals[i-1][1])
            if intervals[i][0] < intervals[i-1][1]:
                return 0

        return 1

intervals= [
[23, 50],
[56, 89],
[98, 100000000],
[10000, 12341243],
[34, 44],
[1, 10],
[22, 23]
]
sol=Solution()
print(sol.can_attend_all_meetings(intervals))
