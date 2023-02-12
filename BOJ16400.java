import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 시간제한 1초 -> 에라토스테네스의 체 사용
 * 화폐 -> 동전문제에서 사용하는 DP 알고리즘 적용
 *
 * [틀린 이유]
 * DP[j] += (DP[j - i] % MOD)
 * 나머지가 들어가는게 아니라 나머지들의 합이 들어가게 된다
 */
public class BOJ16400 {

    public static int MAX = 40001;
    public static boolean[] isPrimeCoin = new boolean[MAX];
    public static long[] DP = new long[MAX]; //int -> overflow
    public static final long MOD = 123_456_789L;

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int value = Integer.parseInt(br.readLine());

        eratos();
        dp(value);
        int num = 0;
        print_answer(value);
    }

    private static void print_answer(int value) {
        System.out.println(DP[value]);
    }

    public static void dp(int value) {
        DP[0] = 1;
        for (int i = 2; i <= value; i++) {
            if (!isPrimeCoin[i]) {
                for (int j = i; j <= value; j++) {
                        DP[j] += (DP[j - i]); // DP[j] += (DP[j - i] % MOD) 로 착각하지말자...
                        DP[j] %= MOD;
                }
            }
        }
    }

    public static void eratos() {
        isPrimeCoin[0] = isPrimeCoin[1] = true;

        for (int i = 2; i * i < MAX; i++) {
            if (!isPrimeCoin[i]) {
                for (int j = i * i; j < MAX; j += i) {
                    isPrimeCoin[j] = true;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        new BOJ16400().solution();
    }
}
