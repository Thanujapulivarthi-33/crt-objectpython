class Car {

    String brand;
    String color;
    int speed;

    void drive() {
        System.out.println(brand + " car is running");
        System.out.println("Speed: " + speed);
    }

    public static void main(String[] args) {

        Car c1 = new Car();

        c1.brand = "BMW";
        c1.color = "Black";
        c1.speed = 200;

        c1.drive();
    }
}