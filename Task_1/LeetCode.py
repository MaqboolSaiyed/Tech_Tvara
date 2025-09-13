# Floyd's Algorithm Method
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: If the list is empty or has only one node, no cycle can exist.
        if not head or not head.next:
            return None

        # --- Phase 1: Detect if a cycle exists ---
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next      # Move slow pointer by 1
            fast = fast.next.next  # Move fast pointer by 2
            
            # If the pointers meet, a cycle is confirmed.
            if slow == fast:
                break
        else:
            # If the loop completes without meeting, there is no cycle.
            return None

        # --- Phase 2: Find the start of the cycle ---
        # Reset one pointer (e.g., slow) to the head.
        # The other pointer (fast) stays at the meeting point.
        slow = head
        
        # Move both pointers one step at a time until they meet again.
        # The new meeting point is the start of the cycle.
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow # or fast, they are the same node   