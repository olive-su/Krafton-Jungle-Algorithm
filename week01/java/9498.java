import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(br.readLine());
        if (a > 89)
            System.out.println('A');
        else if (a > 79)
            System.out.println('B');
        else if (a > 69)
            System.out.println('c');
        else if (a > 59)
            System.out.println('D');
        else
            System.out.println('F');
    }
}