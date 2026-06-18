'''
Given the head of a sorted linked list,
delete all duplicates such that each element appears only once.
Return the linked list sorted as well.
'''

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class createLinkedList:
    def __init__(self):
        self.head = ListNode(1)
        self.tail = self.head

    def insert(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def removeDuplicatesFromSortedList(self) -> ListNode:
        current = self.head
        while current != None and current.next != None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

    def printList(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next



c = createLinkedList()
c.insert(1)
c.insert(2)
c.insert(3)
c.insert(3)
c.insert(4)
c.insert(5)
c.removeDuplicatesFromSortedList()
c.printList()