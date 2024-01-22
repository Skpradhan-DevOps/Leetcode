class Solution:
    def medianTwoSortedArrays(self,a1,a2):
        a1=sorted(a1)
        a2=sorted(a2)
        a=[]
        a=sorted(a1+a2)
        median=1
        length=len(a)
        if length%2==0:
            length=int(length/2)
            median=float((a[length]+a[length-1])/2)
        else:
            length=int(length/2)
            median=a[length]
        
        return median 

m=int(input("Enter limit for l1:"))
n=int(input("Enter limit for l2:"))
l1=[]
l2=[]
for i in range(m):
    b=int(input())
    l1.append(b)
for i in range(n):
    b=int(input())
    l2.append(b)
sol=Solution()
print("The median is:", sol.medianTwoSortedArrays(l1,l2))
