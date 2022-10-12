import java.util.*;

public class Main {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int max = -1000000;
        int min = 1000000;
        int N = sc.nextInt();
        int[] a = new int[N];
            
        if (N!=1) {
            for (int i=0; i<N; i++) {
                a[i] = sc.nextInt();
                if (a[i] >= max) {
                    max = a[i];
                }
                if (a[i] <= min) {
                    min = a[i];
                }
            }
            System.out.print(min + " " + max);
        } else {
            a[0] = sc.nextInt();
            System.out.print(a[0] + " " + a[0]);
        }
    }
}
        
