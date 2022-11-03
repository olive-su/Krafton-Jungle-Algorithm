import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int multi = 1;
        for (int i = 0; i < 3; i++) {
            multi *= Integer.parseInt(br.readLine());
        }

        String sMulti = Integer.toString(multi);
        for (int i = 0; i < 10; i++) {
            System.out.println(countChar(sMulti, Integer.toString(i)));
        }
    }

    static int countChar(String str, String s) {
        return str.length() - str.replace(String.valueOf(s), "").length();
    }
}