import java.util.*;

public class Fibonacci_series {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Choose the options:-\n1. Iteration\n2. Recursion");
        int key = sc.nextInt();
        System.out.print("fib(n), n = ");
        int n = sc.nextInt(), a = 0, b = 1;

        switch (key) {
            case 1:
                for (int i = 0; i < n; i++) {
                    if (i == n - 1) {
                        System.out.print("fib(n) = " + a + " ");
                    }
                    int sum = a + b;
                    a = b;
                    b = sum;
                }
                break;

            default:
                if (n == 1) {
                    System.out.print(a + " ");
                } else if (n == 2) {
                    System.out.print(b + " ");
                } else {
                    recursionseries(a, b, n - 2);
                }
                break;
        }
    }

    private static void recursionseries(int a, int b, int n) {
        if (n == 0) {
            return;
        }
        int c = a + b;
        if (n == 1) {
            System.out.print("fib(n) = " + c + " ");
        }
        recursionseries(b, c, n - 1);
    }
}
