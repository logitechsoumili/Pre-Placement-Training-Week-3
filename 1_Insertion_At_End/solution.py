class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtEnd(head, x):
    new_node = Node(x)
    if not head:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head

def printList(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))
    head = None
    for val in values:
        head = insertAtEnd(head, val)
    printList(head)