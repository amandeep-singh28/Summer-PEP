class Student {
    String name;
    int[] marks;
    float percentage;
    Student(String name, int[] marks) {
        this.name = name;
        this.marks = marks;
    }

    void get_stats() {
        int sum = 0;
        for (Integer var : marks) {
            sum += var;
        }
        percentage = (sum / 300.0f) * 100;
        System.out.println("Percentage:" + percentage);
    }
    void result() {
        if (percentage > 40) System.out.println("Pass");
        else System.out.println("Fail");
    }
    
}
public class main {
    public static void main(String[] args) {
        String name = "Amandeep";
        int marks[] = {70, 80 , 90};
        Student obj = new Student(name, marks);
        obj.get_stats();
        obj.result();
    }
}
