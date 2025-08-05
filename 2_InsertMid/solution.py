class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertInMid(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    new_node.next = slow.next
    slow.next = new_node
    return head


def build_list():
    head = None
    tail = None
    n = int(input("Enter number of elements: "))
    for _ in range(n):
        val = int(input("Enter value: "))
        new_node = Node(val)
        if not head:
            head = tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head

def main():
    head = build_list()

    printList(head)

if __name__ == "__main__":
    main()