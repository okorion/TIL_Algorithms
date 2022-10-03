#include <stdio.h>

int main(void) {
    int max=0, num;
    int list[9];
    
    for (int i=0; i<9; i++) {
        scanf("%d", &list[i]);
        if (list[i] > max) {
            max = list[i];
            num = i;
        }
    }
    
    printf("%d\n%d", max, num+1);
        
}