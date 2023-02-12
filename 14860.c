//GCD의 곱
#include <stdio.h>
#include <stdbool.h>
#define mod 1000000007

bool composite[15000001];

long long power_modular (long long x, long long y) 
{
	x %= mod;
	long long result = 1;
	while (y) 
    {
		if (y % 2) 
			result = (result * x) % mod;
		x = (x * x) % mod;
		y /= 2;
	}
	return result;
}

int main()
{
	long long N, M;
	scanf("%lld % lld", &N, &M);
	long long min = (M > N) ? N : M;
	
	long long cnt = 0;
	for (int i = 2; i <= min; i *= 2)
		cnt += ((N/i) * (M/i));

	long long answer = power_modular(2, cnt);
	
	for (long long i = 3; i <= min; i += 2)
    {
		if (!composite[i]) 
        {
			cnt = 0;
			for (long long j = i; j <= min; j *= i) 
				cnt += ((N / j) * (M / j));

			answer = (answer * power_modular(i, cnt)) % mod;
			
			for (long long j = 3 * i; j <= min; j += 2 * i)
            {
				if (!composite[j])
                    composite[j] = true;
			}
		}
	}
	printf("%lld", answer % mod);
	return 0;
}