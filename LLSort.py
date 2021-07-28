class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list = None
        temp = None
        s1 = []
        while l1 is not None and l2 is not None:
            if l1 is not None:
                s1.append(l1.val)
                l1 = l1.next

            if l2 is not None:
                s1.append(l1.val)
                l2 = l2.next

        s1.sort()

        for i in range(1, len(s1) + 1, 1):
            if temp is None:
                temp = list = ListNode(int(s1[-i]))
            else:
                temp.next = ListNode(int(s1[-i]))
                temp = temp.next

        return list
