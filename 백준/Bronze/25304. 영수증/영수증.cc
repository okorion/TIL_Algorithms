#include <stdio.h>

int main(void) {
    int sum, num, i;
    int a, b, temp = 0;
    
    scanf("%d", &sum);
    scanf("%d", &num);
    
    for (i=0; i<num; i++) {
    scanf("%d %d", &a, &b);
    temp += a * b;
    }
    
    if (sum == temp) {
        printf("%s", "Yes");
    } else {
        printf("%s", "No");
    }
}