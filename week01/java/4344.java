import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int len = Integer.parseInt(st.nextToken());
            int[] arr = new int[len];
            int sum = 0;
            for (int j = 0; j < len; j++) {
                arr[j] = Integer.parseInt(st.nextToken());
                sum += arr[j];
            }
            double ever = sum / len;
            int cnt = 0;

            for (int j = 0; j < len; j++) {
                if (arr[j] > ever)
                    cnt++;
            }

            System.out.println(String.format("%.3f%%",(cnt / (double)len) * 100));
        }
    }
}