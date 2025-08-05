#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

int search(struct Node* head, int x) {
    while (head) {
        if (head->data == x) return 1;
        head = head->next;
    }
    return 0;
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

    printf("Enter value to search: ");
    scanf("%d", &val);
    int found = search(head, val);
    printf("Found: %s\n", found ? "Yes" : "No");

    printList(head);
    return 0;
}