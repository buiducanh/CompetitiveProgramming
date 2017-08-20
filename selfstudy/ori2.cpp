#include <iostream>

void swap(int *a, int *b) {
    int c = *a;
    *a = *b;
    *b = c;
}

int main() {
    int a = 3, b = 0;
    swap(&a, &b);
    printf("%d %d", a, b);
}
