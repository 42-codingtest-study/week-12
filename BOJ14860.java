import java.io.*;
import java.util.*;

/** psvm / solution 으로 분리하니까 런타임 에러 (ArrayIndexOutOfBounds) 발생... 왜?
 *
 */

public class BOJ14860 {
    static final long mod=(long)1e9+7;
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        boolean[] tmp=new boolean[15000001];
        for(int i=2; i<=15000000; i++){
            if(tmp[i]) continue;
            for(int j=2; i*j<=15000000; j++) tmp[i*j]=true;
        }
        ArrayList<Integer> k=new ArrayList<>();
        ArrayList<Long> ka=new ArrayList<>();
        for(int i=2; i<=15000000; i++){
            if(!tmp[i]) k.add(i);
        }
        String[] s = bf.readLine().split(" ");
        int a = Integer.parseInt(s[0]), b = Integer.parseInt(s[1]);
        for(int i:k){
            int t=a,m=b;
            long sum=0;
            while(t!=0 && m!=0){
                t/=i; m/=i;
                sum+=(long)t*m;
            }
            ka.add(sum);
        }
        long sum=1;
        for(int i=0; i<k.size(); i++) sum=sum*pow(k.get(i),ka.get(i))%mod;
        System.out.print(sum);
    }
    static long pow(long x,long y){
        if(y==0) return 1;
        if(y==1) return x;
        long u=pow(x,y/2);
        u=u*u%mod;
        if(y%2==1) u=u*x%mod;
        return u;
    }
}