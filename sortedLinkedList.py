class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    def mergeKlist(lists):
        minheap = []

        for i in range(len(lists)-1):
            if lists[i] is not None:
                minheap.insert(lists[i].value, lists[i])

        #initialize output list

        head = new LinkedListNode("Sentinel")
        tail = head

        #repeatedly extract the min element from heap and append to o/p list

        while minheap:
            minheap.extractmin()
            #Append p to the end of the o/p list
            tail.next = p
            tail = p
            p = p.next
            tail.next = null
            if p is not None:
                minheap.insert((p.value,p))

            head = head.next
            return head
