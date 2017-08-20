import java.util.Scanner;

/**
 * Created by anhbui on 1/25/16.
 */
class BigMod {
    public static int bigMod(int b, int p, int m) {
        if (p == 0) {
            return 1;
        }
        if (p == 1) {
            return b % m;
        }

        if (p % 2 == 1) {
            return ((b % m) * bigMod(b, p - 1, m)) % m;
        }

        return (bigMod(b, p / 2, m) * bigMod(b, p / 2, m)) % m;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
	while (sc.hasNextLine()) {
		int b = sc.nextInt();
		int p = sc.nextInt();
		int m = sc.nextInt();
		System.out.println(bigMod(b, p, m));
	}
    }
}
