class Solution:
    def removeNthFromEnd(self,head,n):
        l1=len(head)
        index=l1-n
        value=head[index]
        head.remove(value)
        return head

head=[1,2]
n=1
sol=Solution()
print(sol.removeNthFromEnd(head,n))


#        temp=head
#       count=0
#       while (temp):
#           count+=1
#           temp=temp.next
#       print(count)
#       l1=count
