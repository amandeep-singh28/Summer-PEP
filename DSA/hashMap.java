import java.util.HashMap;

public class hashMap {
    public static void main(String[] args) {
        HashMap<String, Integer> mp = new HashMap<>();
        mp.put("Amandeep", 101);
        mp.put("Bunty", 150);
        mp.put("Ravi", 160);
        mp.put("Ram", 250);
        System.out.println(mp);

        for (var e : mp.entrySet()) {
            System.out.println(e.getKey());
            System.out.println(e.getValue());
        }
        
    }
}
