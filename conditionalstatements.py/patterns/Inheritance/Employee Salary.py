class Employee {

    String name;
    double salary;

    void showEmployee() {
        System.out.println(name);
        System.out.println(salary);
    }
}


class Developer extends Employee {

    String language;

    void showDeveloper() {
        System.out.println(language);
    }


    public static void main(String[] args) {

        Developer d = new Developer();

        d.name = "Ravi";
        d.salary = 50000;
        d.language = "Java";

        d.showEmployee();
        d.showDeveloper();
    }
}