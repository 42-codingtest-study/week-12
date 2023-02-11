import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class BOJ23048 {

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        if (n <= 2) {
            if (n == 1) {
                System.out.println(1);
                System.out.println("1");
            } else if (n == 2) {
                System.out.println(2);
                System.out.println("1 2");
            }
            System.exit(0);
        }

        int[] color = new int[n + 1];
        boolean[] prime = new boolean[n + 1];
        Arrays.fill(prime, true);
        prime[0] = prime[1] = false;

        for (int i = 2; i * i <= n; i++) {
            if (!prime[i]) {
                continue;
            }
            for (int j = i * i; j <= n; j += i) {
                prime[j] = false;
            }
        }

        ArrayList<Integer> primeList = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            if (prime[i]) {
                primeList.add(i);
            }
        }

        color[1] = 1;
        int idx = 1;

        for (int p : primeList) {
            idx++;
            for (int i = p; i <= n; i += p) {
                color[i] = idx;
            }
        }

        sb.append(idx).append('\n');
        for (int i = 1; i <= n; i++) {
            sb.append(color[i]).append(" ");
        }
        System.out.println(sb);
    }

    public static void main(String[] args) throws IOException {
        new BOJ23048().solution();
    }

}
