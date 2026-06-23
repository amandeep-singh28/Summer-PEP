// import java.util.*;

public class basic {
    public static void main(String[] args) {
        // int num1 = 1;
        // int num2 = 10;
        // for (int i = num1; i <= num2; i++) {
        //     int count = 0;
        //     for (int j = 1; j <= i; j++) {
        //         if (i % j == 0) {
        //             count++;
        //         }
        //     }
        //     if (count == 2) {
        //         System.out.println(i);
        //     }
        // }

        String str = "abcda";
        int[] freq = new int[26];
        for (int i = 0; i < str.length(); i++) {
            freq[(int)str.charAt(i) - 97]++;  // 97
        }
        for (int i = 0; i < 26; i++) {
            System.out.print(freq[i] + " ");
        }
        
    }
}