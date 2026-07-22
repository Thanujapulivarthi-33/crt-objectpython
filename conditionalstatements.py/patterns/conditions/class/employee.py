class Employee {

    int id;
    String name;
    double salary;

    void showDetails() {

        System.out.println("Employee ID: " + id);
        System.out.println("Name: " + name);
        System.out.println("Salary: " + salary);
    }


    public static void main(String[] args) {

        Employee emp = new Employee();

        emp.id = 1;
        emp.name = "Ravi";
        emp.salary = 50000;

        emp.showDetails();
    }
}