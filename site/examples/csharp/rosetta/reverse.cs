using System;

class Program {
    static void Main() {
        char[] s = "pointer".ToCharArray();
        Array.Reverse(s);
        Console.WriteLine(new string(s));
    }
}
