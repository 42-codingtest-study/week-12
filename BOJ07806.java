import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * n 이 10 억이 될 수 있으므로 정상적인 팩토리얼의 경우 시간초과 발생
 *
 * 최대 공약수를 다시 한번 생각해보면 GCD(a, b) = c 일 때 a % c = 0, b % c = 0
 * n! 은 1~n까지 숫자들의 곱이므로 1~n의 숫자들 중 아무 숫자나 하나씩 랜덤으로 뽑은 뒤 곱해도 n!의 약수임
 *
 * [소인수 분해 특징]
 * n과 m이 있을 때 n!과 m의 gcd 를 찾아야하는데
 * 이때 m을 소인수 분해를 할 때 root(m)까지만 찾아주면 된다
 *
 * 1. m 를 소인수 분해 하고 지수를 카운팅한다
 *
 * 2. 나누어진 수의 1제곱 ~ 이 몇개 있는지 확인한다
 *
 */
public class BOJ07806 {

    public void solution() throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        String string;
        while ((string= br.readLine()) != null){
            st = new StringTokenizer(string);
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            int answer = 1;
            for (int i = 2; i * i <= m; i++){
                int factorization_K_Count = 0;

                while (m % i == 0) {
                    m /= i;
                    factorization_K_Count++;
                }
                if (factorization_K_Count != 0){
                    int factorization_N_Count = 0;
                    factorization_N_Count = getFactorization_n_count(n, i, factorization_N_Count);
                    for (int j = 0; j < Math.min(factorization_N_Count, factorization_K_Count); j++)
                        answer *= i;
                }
                if(m < i)
                    break;
            }
            if (m > 1 && m <= n)
                answer *= m;
            System.out.println(answer);
        }
    }

    private static int getFactorization_n_count(int n, int i, int factorization_N_Count) {
        for (int j = i; j <= n; j *= i)
            factorization_N_Count += n / j; // 2^1 2^2 2^3 ...
        return factorization_N_Count;
    }

    public static void main(String[] args) throws IOException{
        new BOJ07806().solution();
    }
}
