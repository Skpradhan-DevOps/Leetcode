class Solution:
    
    def sortChars(self, arr):
        arr.sort()
        return arr

    def sortAscii(self,start, end, arr):
        res=[]
        for c in arr:
            if type(c) == str:
                c=ord(c)
                res.append(c)
                

        #return res
        if start < end:
            partition_pos=self.partition(start, end, res)
            self.sortAscii(start, partition_pos - 1, res)
            self.sortAscii(partition_pos + 1, end, res)

        arr=[]
        for i in res:
            arr.append(char(i))

        return arr


    def partition(self,start, end, arr):
        i= start
        j= end-1
        pivot= arr[end]

        while i < j:
            while i < end and arr[i] < pivot:
                i += 1
            while j > start and arr[j] >= pivot:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        if arr[i] > pivot:
            arr[i], arr[end] = arr[end], arr[i]

        return i

arr= ["a", "s", "d", "f", "g", "*", "&", "!", "z", "y"]
sol=Solution()
#print(sol.sortChars(arr))
print(sol.sortAscii(0, len(arr) -1, arr))
