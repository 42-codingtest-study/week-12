#include <iostream>
#include <vector>
#include <math.h>
#include <set>


using namespace std;

int main()
{

    int n;
    cin>>n;

    vector<int> colors;
    for (int i = 0; i <= n; i++)
    {
        colors.push_back(0);
    }
    int color_cnt = 2;
    
    for (int i = 2; i <= n; i++)
    {
        int color_flag = 0;
        for (int j = i; j <= n; j+=i)
        {
            if(colors[j] == 0)
            {
                color_flag = 1;
                colors[j] = color_cnt;
            }
        }
        if (color_flag == 1)
        {
            color_cnt++;
        }
        
    }
    colors[1] = 1;
    set<int> numbers;

    for (int i = 1; i <= n; i++)
    {
        numbers.insert(colors[i]);
    }

    cout<<numbers.size()<<"\n";
    
    for (int i = 1; i <= n; i++)
    {
        cout<<colors[i]<<" ";
    }
    cout<<"\n";
    return 0;
}
