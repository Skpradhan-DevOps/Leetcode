import heapq
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    def merge_k_lists(lists):
        """
        Args:
         lists(list_LinkedListNode_int32)
        Returns:
         LinkedListNode_int32
        """
        # Write your code here.
        if len(lists)==0:
            return None
        minh=[]
        heapq.heapify(minh)
        '''for i,l in enumerate(lists):
            if l:
                heapq.heappush(h,(l.value,i))
                
        dummy=curr=LinkedListNode(0)
        
        while h:
            value,i=heapq.heappop(h)
            curr.next=LinkedListNode(value)
            
            if lists[i].next:
                heapq.heappush(h,(lists[i].value,i))
                lists[i]=lists[i].next
            curr=curr.next'''
        
        #initialize o/p list
        #head = LinkedListNode(0)
        tail = head = None
        
        for i in range(len(lists)):
            if list[i]:
                heapq.heappush(minh, (lists[i].value, lists[i]))
                    

            #Repeatedly extract min element from heap and append to o/p list
        while minh:
            (value, p) = heapq.heappop(minh)
            tail.next = p
            tail = p
            p = p.next
            tail.next = None
            if p is not None:
                heapq.heappush(minh,(p.value, p))
            head = head.next
        return head
