#include <stdio.h>

int main(void) {
    int k, q, r, b, n, p;
    
    scanf("%d %d %d %d %d %d", &k, &q, &r, &b, &n, &p);
    
    if (k != 1) {
        printf("%d ", 1-k);
    } else {
        printf("%d ", 0);
    }
    
    if (q != 1) {
        printf("%d ", 1-q);
    } else {
        printf("%d ", 0);
    }
    
    if (r != 2) {
        printf("%d ", 2-r);
    } else {
        printf("%d ", 0);
    } 
    
    if (b != 2) {
        printf("%d ", 2-b);
    } else {
        printf("%d ", 0);
    }
    
    if (n != 2) {
        printf("%d ", 2-n);
    } else {
        printf("%d ", 0);
    }
    
    if (p != 8) {
        printf("%d ", 8-p);
    } else {
        printf("%d ", 0);
    }
}