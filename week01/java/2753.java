import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(br.readLine());
        int answer = 0;
        if (a % 4 == 0) {
            if ((a % 100) > 0 || (a % 400) == 0 )
                answer = 1;
        }
        System.out.println(answer);
    }
}