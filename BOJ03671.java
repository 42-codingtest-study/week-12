import java.io.*;
import java.util.LinkedList;

class BOJ03671 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int c;
    static boolean[] decimal;
    static int[] number;
    static final int LIMIT_NUM = 10000000;
    static LinkedList<Integer> list;
    static int ans = 0;

    public void solution() throws IOException {
        set();
        solve();

        bw.flush();
        bw.close();
        br.close();
    }

    static void set() throws IOException {
        getDecimal();
        c = Integer.parseInt(br.readLine());
        for(int i=0; i<c; i++){
            ans = 0;
            list = new LinkedList<>();
            String str = br.readLine();
            number = new int[str.length()];
            for(int k=0; k<str.length(); k++){
                number[k] = Integer.parseInt(String.valueOf(str.charAt(k)));
            }
            solve();
            while(!list.isEmpty()){
                int num = list.remove();
                decimal[num] = false;
                ans++;
            }

            bw.write(ans + "\n");
        }
    }
    static void sort_array(int[] sort_arr, int depth, int r){
        if(r == 0){
            int k=1;
            int newValue = 0;
            for(int i=0; i<depth; i++){
                newValue += sort_arr[i] * k ;
                k *= 10;
            }
            if (!decimal[newValue]) {
                list.add(newValue);
                decimal[newValue] = true;
            }
            return;
        }
        for(int i=depth; i<number.length; i++){
            swap(sort_arr, depth, i);
            sort_array(sort_arr, depth+1, r-1);
            swap(sort_arr, depth, i);
        }
    }
    static void swap(int[] arr, int depth, int i) {
        int temp = arr[depth];
        arr[depth] = arr[i];
        arr[i] = temp;
    }

    static void getDecimal(){
        decimal = new boolean[LIMIT_NUM];
        decimal[0] = true;
        decimal[1] = true;
        for(int i=2; i*i<LIMIT_NUM; i++){
            for(int k=i*i; k<LIMIT_NUM; k+=i){
                decimal[k] = true;
            }
        }
    }

    static void solve() throws IOException {
        for(int k=1; k<=number.length; k++){
            sort_array(number,0,k);
        }
    }

    public static void main(String[] args) throws IOException {
        new BOJ03671().solution();
    }
}