#include <stdio.h>

int main(void) {
    int a=0;
    int b=0;
    while(scanf("%d %d", &a, &b) != EOF) {
        printf("%d\n", a+b);
    }
}
