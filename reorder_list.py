# Definition for singly-linked list.
import collections

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        l = 0
        node = head
        while node != None:
            l += 1
            node = node.next
        if any([l == 0, l == 1, l == 2]):
            return head
        numOfInsert = l / 2
        numOfKeep = l - l/2
        cur = head
        ls_insert = []
        for i in range(numOfKeep):
                cur = cur.next
        while cur != None:
            ls_insert.append(cur)
            cur = cur.next
        cur = head
        for i in range(numOfInsert):
            node = ls_insert.pop()
            if i == numOfInsert-1:
                if l%2 == 0:
                    node.next = None
                    cur.next = node
                    return head
                else:
                    node.next = cur.next
                    cur.next = node
                    cur = cur.next.next
                    cur.next = None
                    return head
            node.next = cur.next
            cur.next = node
            cur = cur.next.next

    def printList(self,head):
        cur = head
        while cur!= None:
            print cur.val
            cur = cur.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d

q = Solution()
q.printList(a)
q.reorderList(a)
q.printList(a)
