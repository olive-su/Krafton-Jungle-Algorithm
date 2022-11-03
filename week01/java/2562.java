import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = new int[9];
        int answer = Integer.MIN_VALUE;
        int idx = 0;

        for (int i = 0; i < 9; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        for (int i = 0; i < 9; i++) {
            if (answer < arr[i]) {
                answer = arr[i];
                idx = i + 1;
            }
        }
        System.out.println(answer);
        System.out.println(idx);
    }
}