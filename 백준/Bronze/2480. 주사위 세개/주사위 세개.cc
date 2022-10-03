#include <stdio.h>

int main(void) {
	int a, b, c;
    int temp;
    
    temp=0;
    scanf("%d %d %d", &a, &b, &c);
        
    for (int i=0; i<3; i++) {
        if (temp <= a) {
            temp = a;
        }
        if (temp <= b) {
            temp = b;
        }
        if (temp <= c) {
            temp = c;
        }
    }
    
    if (a==b && b==c) {
        printf("%d", a*1000 + 10000);
    } else if (a==b) {
        printf("%d", a*100 + 1000);
    } else if (b==c) {
        printf("%d", b*100 + 1000);
    } else if (c==a) {
        printf("%d", c*100 + 1000);
    } else {
        printf("%d", temp*100);
    }
}