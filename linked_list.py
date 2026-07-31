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



## Add two numbers represented as Linked Lists
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1


def addTwoNumbers(l1, l2):
    dummyNode = Node(-1)
    temp = dummyNode
    carry = 0

    while l1 is not None or l2 is not None or carry:
        sum_val = carry
        if l1 is not None:
            sum_val += l1.data
            l1 = l1.next
        if l2 is not None:
            sum_val += l2.data
            l2 = l2.next

        carry = sum_val // 10
        digit = sum_val % 10

        temp.next = Node(digit)
        temp = temp.next

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
l1 = convertArr2LL([2, 4, 3])   # represents 342
l2 = convertArr2LL([5, 6, 4])   # represents 465
result = addTwoNumbers(l1, l2)
printLL(result)  # 7->0->8  (represents 807)

l1b = convertArr2LL([9, 9, 9, 9, 9, 9])
l2b = convertArr2LL([9, 9, 9, 9])
result2 = addTwoNumbers(l1b, l2b)
printLL(result2)  # 8->9->9->9->0->0->0->1


## Delete given node in a Linked List : O(1) approach
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1


def deleteNode(node):
    # node is NOT the tail (guaranteed), so node.next always exists
    node.data = node.next.data   # copy next node's value into this node
    node.next = node.next.next   # skip over the (now-duplicate) next node


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


def findNode(head, target):
    curr = head
    while curr.data != target:
        curr = curr.next
    return curr


# ---- driver code ----
head = convertArr2LL([1, 4, 2, 3])
nodeToDelete = findNode(head, 2)   # simulates "being given" node with value 2
deleteNode(nodeToDelete)
printLL(head)  # 1->4->3

head2 = convertArr2LL([1, 2, 3, 4])
nodeToDelete2 = findNode(head2, 1)
deleteNode(nodeToDelete2)
printLL(head2)  # 2->3->4