import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = 0;
            
        long n = sc.nextLong();
        long a = sc.nextLong();
        long b = sc.nextLong();
        long c = sc.nextLong();
        long d = sc.nextLong();
        long e = sc.nextLong();
        
        if(n==a) {
            num += 1;
        }
        if(n==b) {
            num += 1;
        }
        if(n==c) {
            num += 1;
        }        
        if(n==d) {
            num += 1;
        }        
        if(n==e) {
            num += 1;
        }
        
        System.out.print(num);
    }
}