class BankAccount {

    String holderName;
    double balance;

    void deposit(double amount) {
        balance = balance + amount;
    }

    void withdraw(double amount) {
        balance = balance - amount;
    }

    void display() {
        System.out.println("Name: " + holderName);
        System.out.println("Balance: " + balance);
    }


    public static void main(String[] args) {

        BankAccount b1 = new BankAccount();

        b1.holderName = "Tanuja";
        b1.balance = 10000;

        b1.deposit(5000);
        b1.withdraw(2000);

        b1.display();
    }
}