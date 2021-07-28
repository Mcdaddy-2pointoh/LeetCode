class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ptr = head
        lens = 1
        while ptr.next != None:
            lens += 1
            ptr = ptr.next

        ptr1 = head
        ptr2 = head
        n = lens - n
        if n == 0:
            return ptr1.next

        while n != -1:

            if n == 1:
                ptr2 = ptr1

            if n == 0:
                ptr2.next = ptr1.next
                break

            n -= 1
            ptr1 = ptr1.next

        return head