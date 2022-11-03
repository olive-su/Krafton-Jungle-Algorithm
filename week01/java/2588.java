import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(br.readLine());
        int b = Integer.parseInt(br.readLine());
        int answer = 0;

        for (int i = 0; i < 3; i++) {
            int num = (b % 10) * a;
            b /= 10;
            answer += num * Math.pow(10, i);
            System.out.println(num);
        }
        System.out.println(answer);
    }
}