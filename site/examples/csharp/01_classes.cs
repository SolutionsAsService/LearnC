using System;

class Account {
    public string Owner { get; private set; }   // a property: read anywhere, set inside
    public decimal Balance { get; private set; }

    public Account(string owner) { Owner = owner; }

    public void Deposit(decimal amount) {
        if (amount <= 0) throw new ArgumentException("amount must be positive");
        Balance += amount;
    }
}

class Program {
    static void Main() {
        var a = new Account("Ada");
        a.Deposit(10.50m);
        try { a.Deposit(-1); }
        catch (ArgumentException e) { Console.WriteLine("refused: " + e.Message); }
        Console.WriteLine(a.Owner + " has " + a.Balance);
    }
}
