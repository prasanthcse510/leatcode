# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()  # Initialize dummy node
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            new_digit = total % 10
            current.next = ListNode(new_digit)
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

# Helper function to convert a list into a linked list
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for number in lst:
        current.next = ListNode(number)
        current = current.next
    return dummy.next

# Helper function to print the linked list
def print_linked_list(node):
    numbers = []
    while node:
        numbers.append(node.val)
        node = node.next
    print("->".join(map(str, numbers)))

# Test case 1:
l1 = create_linked_list([2, 4, 3])  # Represents number 342
l2 = create_linked_list([5, 6, 4])  # Represents number 465

# Create solution object
sol = Solution()

# Call the function and get the result linked list
result = sol.addTwoNumbers(l1, l2)

# Print the result
print("Output Linked List:")
print_linked_list(result)  # Expected output: 7->0->8, represents 807
