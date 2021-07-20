class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        list = None
        temp = None
        s1 = ""
        s2 = ""
        while l1 is not None and l2 is not None:
            if l1 is not None:
                s1 = str(l1.val) + s1
                l1 = l1.next

            if l2 is not None:
                s2 = str(l2.val) + s2
                l2 = l2.next

        res = str(int(s1) + int(s2))

        for i in range(1, len(res) + 1, 1):
            if temp is None:
                temp = list = ListNode(int(res[-i]))
            else:
                temp.next = ListNode(int(res[-i]))
                temp = temp.next

        return list
