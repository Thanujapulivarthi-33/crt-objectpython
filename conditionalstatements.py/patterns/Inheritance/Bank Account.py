class BankAccount {

    double balance = 10000;

    void deposit(double amount) {

        balance += amount;
    }
}


class SavingsAccount extends BankAccount {

    void display() {

        System.out.println("Balance: " + balance);
    }


    public static void main(String[] args) {

        SavingsAccount s = new SavingsAccount();

        s.deposit(5000);
        s.display();
    }
}