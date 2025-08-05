#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

int getNthFromLast(struct Node* head, int n) {
    struct Node* first = head;
    struct Node* second = head;
    for (int i = 0; i < n; i++) {
        if (!first) return -1;
        first = first->next;
    }
    while (first) {
        first = first->next;
        second = second->next;
    }
    return second ? second->data : -1;
}


int main() {
    struct Node* head = NULL;
    int n, val, pos;
    printf("Enter number of elements: ");
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        printf("Enter value: ");
        scanf("%d", &val);
        head = insertEnd(head, val);
    }

    printf("Enter N (from end): ");
    scanf("%d", &pos);
    int result = getNthFromLast(head, pos);
    printf("Nth node from end: %d\n", result);

    printList(head);
    return 0;
}