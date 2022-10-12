#include <stdio.h>

int main (void) {
    int a, c;
    int maxN = -1000000;
    int minN = 1000000;
 
    scanf("%d", &a);
    
    for (int i=0; i<a; i++) {
        scanf("%d", &c);
        
        if (c > maxN) {
            maxN = c;
        }
        if (c < minN) {
            minN = c;
        }
    }
    printf("%d %d", minN, maxN);
    return 0;
}