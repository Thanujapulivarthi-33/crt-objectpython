class Person {

    String name;
    int age;

    void displayPerson() {
        System.out.println(name);
        System.out.println(age);
    }
}


class Student extends Person {

    int rollNo;
    int marks;

    void displayStudent() {
        System.out.println(rollNo);
        System.out.println(marks);
    }


    public static void main(String[] args) {

        Student s = new Student();

        s.name = "Tanuja";
        s.age = 21;
        s.rollNo = 101;
        s.marks = 90;

        s.displayPerson();
        s.displayStudent();
    }
}