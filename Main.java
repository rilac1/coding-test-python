public class Main {
    static int d(int n) {
        int sum = n;
        while (n>0) {
            sum += n%10;
            n /= 10;
        }
        if (sum<=10000) return sum;
        return 0;
    }
    public static void main(String args[]) {
        boolean[] result = new boolean[10001];
        for (int i=1; i<10001; i++) {
            result[d(i)] = true;
            if (!result[i]) System.out.println(i);
        }
    }
}