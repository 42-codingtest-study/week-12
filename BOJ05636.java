import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 *
 */

public class BOJ05636 {

    boolean[] prime;
    int max = 100000;

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        prime = eratos();

        while (true) {
            String string = br.readLine();

            if (string.equals("0"))
                break;
            for (int i = max; i >= 2; i--) {
                if (prime[i])
                    continue;
                if (solve(string, i) == 1)
                    break;
            }
        }
    }

    private int solve(String string, int i) {
        String tmp = Long.toString(i);
        if (string.contains(tmp)) {
            System.out.println(tmp);
            return 1;
        }
        return 0;
    }

    private boolean[] eratos() {
        boolean[] prime = new boolean[max + 1];

        for (int i = 2; i <= max; i++) {
            for (int j = i * 2; j < max; j += i) {
                prime[j] = true;
            }
        }
        return prime;
    }

    public static void main(String[] args) throws IOException{
        new BOJ05636().solution();
    }

}
