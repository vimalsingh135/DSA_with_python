## Check if the given Linked List is Palindrome
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1


def isPalindrome(head):
    if head is None or head.next is None:
        return True

    # Step 1: find the middle using slow/fast pointers
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    # Step 2: reverse the second half (starting right after slow)
    newHead = reverseLinkedList(slow.next)

    # Step 3: compare first half with reversed second half
    first = head
    second = newHead
    isPalin = True
    while second is not None:
        if first.data != second.data:
            isPalin = False
            break
        first = first.next
        second = second.next

    # Step 4: restore the list back to original (good practice)
    slow.next = reverseLinkedList(newHead)

    return isPalin


def reverseLinkedList(head):
    prev = None
    curr = head
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


# ---- helper functions ----
def convertArr2LL(arr):
    head = Node(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = Node(arr[i])
        curr = curr.next
    return head


def printLL(head):
    curr = head
    while curr is not None:
        print(curr.data, end="->" if curr.next else "")
        curr = curr.next
    print()


# ---- driver code ----
head1 = convertArr2LL([3, 7, 5, 7, 3])
print(isPalindrome(head1))   # True
printLL(head1)                # confirms list is restored: 3->7->5->7->3

head2 = convertArr2LL([1, 1, 2, 1])
print(isPalindrome(head2))   # False

## Floyd's Cycle Detection (Tortoise and Hare) problem
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

## Reverse Linked List in groups of Size K
class listNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
        node=head
        count=0
        while node and count<k:
            node=node.next
            count+=1
        if count<k:
            return head

        prev,curr=None,head
        for _ in range(k):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt

        head.next = reverseKGroup(curr, k)
        return prev

def printList(head):
    node = head
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

# ---- Driver code ----
# Build list: 1 -> 2 -> 3 -> 4 -> 5
head = listNode(1)
head.next = listNode(2)
head.next.next = listNode(3)
head.next.next.next = listNode(4)
head.next.next.next.next = listNode(5)

print("Original list:")
printList(head)

k = 2
new_head = reverseKGroup(head, k)

print(f"Reversed in groups of {k}:")
printList(new_head)