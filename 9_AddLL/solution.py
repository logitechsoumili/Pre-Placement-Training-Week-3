class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def addTwoLists(first, second):
    dummy = Node(0)
    curr = dummy
    carry = 0
    while first or second or carry:
        total = carry
        if first:
            total += first.data
            first = first.next
        if second:
            total += second.data
            second = second.next
        carry = total // 10
        curr.next = Node(total % 10)
        curr = curr.next
    return dummy.next


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