class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteNode(head, x):
    if x == 1:
        return head.next
    temp = head
    for _ in range(x - 2):
        if temp is None:
            return head
        temp = temp.next
    if temp and temp.next:
        temp.next = temp.next.next
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

    pos = int(input("Enter position to delete: "))
    head = deleteNode(head, pos)

    printList(head)

if __name__ == "__main__":
    main()