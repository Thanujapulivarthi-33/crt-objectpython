class Mobile {

    String brand;
    String model;
    int price;


    void display() {

        System.out.println(brand);
        System.out.println(model);
        System.out.println(price);
    }


    public static void main(String[] args) {

        Mobile m1 = new Mobile();

        m1.brand = "Samsung";
        m1.model = "S24";
        m1.price = 70000;

        m1.display();
    }
}