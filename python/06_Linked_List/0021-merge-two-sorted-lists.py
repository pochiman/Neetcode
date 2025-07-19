"""

21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing 
together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

"""

# Solution 2: Iteration [✔️]
# Time Complexity: O(n + m)
# Space Complexity: O(1)

# Where n is the length of list1 and m is the length of list2.

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode: # type: ignore
        dummy = ListNode() # type: ignore
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next