using System;

struct Point {                         // a value type, like a C struct
    public double X, Y;
    public Point(double x, double y) { X = x; Y = y; }
    public double Length() { return Math.Sqrt(X * X + Y * Y); }
}

class Program {
    static void Main() {
        var p = new Point(3, 4);
        Console.WriteLine(p.Length().ToString("F1"));
    }
}
