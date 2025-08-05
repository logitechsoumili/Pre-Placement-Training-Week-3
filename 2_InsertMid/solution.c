#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

void insertInMid(struct Node** head, int data) {
    struct Node* newNode = (struct Node*) malloc(sizeof(struct Node));
    newNode->data = data;
    if (!(*head)) {
        *head = newNode;
        newNode->next = NULL;
        return;
    }
    struct Node* slow = *head;
    struct Node* fast = *head->next;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    newNode->next = slow->next;
    slow->next = newNode;
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

    printList(head);
    return 0;
}