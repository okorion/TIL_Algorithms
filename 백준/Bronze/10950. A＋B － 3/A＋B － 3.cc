#include <stdio.h>

int main(void) {
    int num, i;
    int a, b;
    
    scanf("%d", &num);
        
    for (i=0; i<num; i++) {
        scanf("%d %d", &a, &b);
        printf("%d\n", a+b);
    } return 0;
}