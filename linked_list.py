## Reverse a Linked List
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1


def reverseLinkedList(head):
    # base case: empty or single-node list
    if head is None or head.next is None:
        return head

    prev = None
    curr = head

    while curr is not None:
        nextNode = curr.next   # store next node
        curr.next = prev       # reverse current node's pointer
        prev = curr            # move prev one step forward
        curr = nextNode        # move curr one step forward

    return prev  # prev is now the new head


# ---- helper functions to test ----
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
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")


# ---- driver code ----
arr = [1, 3, 2, 4]
head = convertArr2LL(arr)

print("Original List: ", end="")
printLL(head)

head = reverseLinkedList(head)

print("Reversed List: ", end="")
printLL(head)


## Find middle element in a Linked List
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1


def findMiddle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next        # moves 1 step
        fast = fast.next.next   # moves 2 steps

    return slow  # slow is now at the middle


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
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")


# ---- driver code ----
arr1 = [1, 2, 3, 4, 5]
head1 = convertArr2LL(arr1)
print("Middle of odd list:", findMiddle(head1).data)  # 3

arr2 = [1, 2, 3, 4, 5, 6]
head2 = convertArr2LL(arr2)
print("Middle of even list:", findMiddle(head2).data)  # 4