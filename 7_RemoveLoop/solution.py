class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeLoop(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if slow == fast:
        slow = head
        if slow == fast:
            while fast.next != slow:
                fast = fast.next
        else:
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next
        fast.next = None


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