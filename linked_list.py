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

## Merge two sorted Linked Lists
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1


def mergeTwoLists(list1, list2):
    dummyNode = Node(-1)   # placeholder to simplify edge cases
    temp = dummyNode

    while list1 is not None and list2 is not None:
        if list1.data <= list2.data:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        temp = temp.next

    # attach whichever list still has leftover nodes
    if list1 is not None:
        temp.next = list1
    else:
        temp.next = list2

    return dummyNode.next  # skip the dummy, real head starts here


# ---- helper functions ----
def convertArr2LL(arr):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = Node(arr[i])
        curr = curr.next
    return head


##Remove N-th node from the end of a Linked List
def printLL(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")


# ---- driver code ----
list1 = convertArr2LL([2, 4, 8, 10])
list2 = convertArr2LL([1, 3, 3, 6, 11, 14])

merged = mergeTwoLists(list1, list2)
print("Merged List: ", end="")
printLL(merged)

##
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1


def removeNthFromEnd(head, n):
    dummyNode = Node(-1)
    dummyNode.next = head
    fast = dummyNode
    slow = dummyNode

    # move fast n steps ahead
    for _ in range(n):
        fast = fast.next

    # move both until fast hits the last node
    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    # slow is now right before the node to delete
    slow.next = slow.next.next

    return dummyNode.next


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
head = convertArr2LL([5, 1, 2])
result = removeNthFromEnd(head, 2)
printLL(result)   # 5->2

head2 = convertArr2LL([1, 2, 3, 4, 5])
result2 = removeNthFromEnd(head2, 3)
printLL(result2)  # 1->2->4->5
