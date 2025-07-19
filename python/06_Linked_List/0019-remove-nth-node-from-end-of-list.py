"""

19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list 
and return its head.



Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

"""

# Solution 4: Two Pointers [✔️]
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode: # type: ignore
        dummy = ListNode(0, head) # type: ignore
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # delete
        left.next = left.next.next
        return dummy.next