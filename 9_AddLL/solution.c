#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* addTwoLists(struct Node* first, struct Node* second) {
    struct Node* res = NULL;
    struct Node** node = &res;
    int carry = 0;
    while (first || second || carry) {
        int sum = carry;
        if (first) { sum += first->data; first = first->next; }
        if (second) { sum += second->data; second = second->next; }
        carry = sum / 10;
        *node = (struct Node*) malloc(sizeof(struct Node));
        (*node)->data = sum % 10;
        node = &((*node)->next);
    }
    *node = NULL;
    return res;
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