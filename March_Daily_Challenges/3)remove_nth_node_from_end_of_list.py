# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n):
    
        '''removable_node = len(head) - n
        head.remove(head[removable_node])
        return head'''
        linked_list_len = self.findLength(head)
        print(linked_list_len)

        i, traverseTill = 0, linked_list_len - n - 1
        if traverseTill == -1:
            return head.next
        curr = head
        while i < traverseTill:
            curr = curr.next
            i += 1
        curr.next = curr.next.next
        return head

        

    def findLength(self, head):
        count = 0 
        if head is None:
            return count
        curr = head
        while curr is not None:
            count += 1
            curr = curr.next
        return count
        
        
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
sol_obj = Solution()
print(sol_obj.removeNthFromEnd(ListNode(1, node2), 2))
