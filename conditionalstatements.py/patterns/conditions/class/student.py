class Student {

    String name;
    int rollNo;
    int marks;

    void display() {
        System.out.println("Name: " + name);
        System.out.println("Roll No: " + rollNo);
        System.out.println("Marks: " + marks);
    }

    public static void main(String[] args) {

        Student s1 = new Student(); // Object creation

        s1.name = "Tanuja";
        s1.rollNo = 101;
        s1.marks = 90;

        s1.display();
    }
}