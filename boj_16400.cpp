#include <iostream>
#include <math.h>
#include <vector>
#include <set>

using namespace std;

bool visited[40002];
vector<int> prime_list;
int dp[40002] = {0,};


int main()
{

    //점화식을 이용해서
    // n 을 a, n-a 로 나누면 arr[a] x arr[n-a] 가 가능한 가짓수가 될테니, a 를 소수인 애들만 으로해서 계산해보자.
    int n;

    for (int i = 0; i<= 40000; i++)
    {
        visited[i] = true;
    }
    for (int i = 2; i <= 200; i++)
    {
        for (int j = i*2; j <= 40000; j+=i)
        {
            visited[j] = false;
        }
    }
    for (int i = 2; i<= 40000; i++)
    {
        if(visited[i] == true)
        {
            prime_list.push_back(i);
        }
    }

    dp[0] =1;

    cin>>n;    
    for (int i = 0 ; i< prime_list.size(); i++)
    {
        for (int j = prime_list[i]; j <=n; j++)
        {
            dp[j] = (dp[j] + dp[j- prime_list[i]])%123456789;
            dp[j]%= 123456789;
        }
    }
    
    cout << dp[n]<<"\n";
    return 0;
}