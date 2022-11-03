import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            int total = 0;
            String[] sArr = br.readLine().split("");
            int score = 0;
            for (int j = 0; j < sArr.length; j++) {
                if (sArr[j].equals("O")) {
                    total++;
                } else {
                    total= 0;
                }
                score += total;
            }
            System.out.println(score);
        }
    }
}