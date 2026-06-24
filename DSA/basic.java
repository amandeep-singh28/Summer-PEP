// import java.util.*;

import java.util.ArrayList;
import java.util.List;

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

        // String str = "abcda";
        // int[] freq = new int[26];
        // for (int i = 0; i < str.length(); i++) {
        //     freq[(int)str.charAt(i) - 97]++;  // 97
        // }
        // for (int i = 0; i < 26; i++) {
        //     System.out.print(freq[i] + " ");
        // }

        int arr[] = {6, 7, 4, 5, 3, 1};
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            boolean flag = false;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] > arr[i]) {
                    flag = true;
                }
                // else if (arr[j] > arr[i]) flag = false;
            }
            if (flag == false) list.add(arr[i]);
        }
        System.out.println(list);
        
    }
}