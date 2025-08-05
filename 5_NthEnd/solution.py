class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getNthFromLast(head, n):
    first = head
    second = head
    for _ in range(n):
        if not first:
            return -1
        first = first.next
    while first:
        first = first.next
        second = second.next
    return second.data if second else -1


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

    n = int(input("Enter N (from end): "))
    print("Nth node from end:", getNthFromLast(head, n))

    printList(head)

if __name__ == "__main__":
    main()