# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers( l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy = ListNode()
        res = dummy

        total = carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            num = total % 10
            carry = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next
        
        return res.next.next.next.val

list1 = ListNode(2)
list1.next = ListNode(5)

list2 = ListNode(5)
list2.next = ListNode(7)

a = Solution
print(a.addTwoNumbers(list1, list2))

