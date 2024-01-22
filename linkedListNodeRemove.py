class Solution:
    def removeNthFromEnd(self, head, n):
        prev = None
        slow = head
        cur = head
        
        i = 1
        # This loop is to reach 'n' node far from cur node
        while i < n:
            if cur is None:
                return head
            cur = cur.next
            i += 1
            
        # Now as we are 'n' node far from slow pointer, we can remove slow pointer node
        # when fast(cur) pointer reaches to end
        while cur:
            if cur.next is None:
                if prev:
                    prev.next = slow.next
                else:
                    head = head.next
                return head
            cur = cur.next
            prev = slow
            slow = slow.next

head = [1,2,3,4,5]
n=2
sol=Solution()
print(sol.removeNthFromEnd(head,n))
