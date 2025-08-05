class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def search(head, x):
    while head:
        if head.data == x:
            return True
        head = head.next
    return False


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

    x = int(input("Enter value to search: "))
    found = search(head, x)
    print("Found:", "Yes" if found else "No")

    printList(head)

if __name__ == "__main__":
    main()