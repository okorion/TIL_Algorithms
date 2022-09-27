#include <stdio.h>

int main(void) {
    int num1, num2, a, b, c, d;
        
    scanf("%d", &num1);
    scanf("%d", &num2);
    
    a = num1 * (num2%10);
    b = num1 * (num2/10 - (num2/100)*10);
    c = num1 * (num2/100);
	d = a+10*b+100*c;
    
    printf("%d\n", a);
    printf("%d\n", b);
    printf("%d\n", c);
    printf("%d", d);
}