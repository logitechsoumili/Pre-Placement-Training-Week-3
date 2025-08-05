#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* deleteNode(struct Node* head, int x) {
    if (x == 1) return head->next;
    struct Node* temp = head;
    for (int i = 1; i < x - 1 && temp; i++) temp = temp->next;
    if (temp && temp->next) temp->next = temp->next->next;
    return head;
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

    printf("Enter position to delete: ");
    scanf("%d", &pos);
    head = deleteNode(head, pos);

    printList(head);
    return 0;
}