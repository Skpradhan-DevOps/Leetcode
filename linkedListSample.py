class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

node1 = ListNode(15)
node2 = ListNode(8.2)
item3 = "Berlin"
node4 = ListNode(15)

track = ListNode(15)
print("track node1:",track.node1)

#for current_item in [node1, node2, item3, node4]:
#    track.add_list_item(current_item)
#    print("track length: %i" % track.list_length())
#    track.output_list()
