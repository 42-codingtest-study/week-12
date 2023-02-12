#include <iostream>
#include <vector>
#include <math.h>
#include <stdlib.h>
#include <cstring>


using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int n, k;
    
    while(!cin.eof() && cin >> n >> k)
    {
        long long int ans = 1;
        //cin>>n>>k;
        int rootk = sqrt(1000000000);
        
        for (int i = 2; i <= rootk; i++)
        {
            int num_of_i_in_k = 0;
            while (k % i == 0)
            {
                k/=i;
                num_of_i_in_k++;
            }
            //k에 i 가 몇개 있는지
            
            int num_of_i_in_n = 0;
            
            if (num_of_i_in_k > 0)
            {
                for (int j = i; j <= n; j *= i)
                {
                    num_of_i_in_n += n/j;       //이게 되는 이유 -> 2, 4, 6, 8, 10
                }
            }
            //n! 에 i 가 몇개 있는지
            
            ans *= pow(i, min(num_of_i_in_k, num_of_i_in_n));
            if(k < i) break;
        }
        if (k > 1 &&  k < n)
        {
            ans *= k;
        }
        cout<<ans<<"\n";
    }
    return 0;
}
