using System;

class Program {
    static void Swap(ref int a, ref int b) { int t = a; a = b; b = t; }

    static void Main() {
        int x = 1, y = 2;
        Swap(ref x, ref y);            // ref: pass the variable, not a copy
        Console.WriteLine("x=" + x + " y=" + y);
    }
}
