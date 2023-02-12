#include<iostream>
#include <vector>
#include <math.h>
#include <set>
#include <stdlib.h>
#include <cstring>

using namespace std;

bool visited[100002];
set<string> prime_str;
int main()
{
    
    //일단 소수들을 다 만들고, 걔네를 set에 문자열로 넣어놓고
    //입력으로 문자열 받아서 거기서 찾자.
    for (int i = 0; i <= 100000; i++)
    {
        visited[i] = true;
    }
    for (int i = 2; i <= sqrt(100000); i++)
    {
        for (int j = i*2; j <= 100000; j+=i)
        {
            visited[j] = false;
        }
    }
    for (int i = 2; i<= 100000; i++)
    {
        if(visited[i] == true)
        {
            prime_str.insert(to_string(i));
        }
    }
//    for(auto iter : prime_str)
//    {
//        cout<<iter<< " ";
//    }
    
    while(1)
    {
        string tmp;
        //string answer = "";
        int answer = 0;
        cin>>tmp;
        if (strcmp(tmp.c_str(), "0") == 0)
        {
            break;
        }
//        cout<<"!!   :  !   " << n<<"\n";
        
        for (auto iter: prime_str)
        {
            if (strstr(tmp.c_str(), iter.c_str())!= NULL)
            {
                int to_num = atoi(iter.c_str());
                if (answer < to_num)
                {
                    answer =to_num;
                }
//                if(strlen(answer.c_str()) < strlen(iter.c_str()))
//                {
//                    answer = iter.c_str();
//                }
            }
        }
//        if (strcmp(answer.c_str(), "") == 0)
//        {
//            cout<<"0\n";
//        } else
        cout<<answer<<"\n";
    }
    return 0;
}
