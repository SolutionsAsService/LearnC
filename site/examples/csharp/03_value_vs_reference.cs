using System;

struct PointS { public int X; }   // value type: copied on assignment
class  PointC { public int X; }   // reference type: assignment copies the reference

class Program {
    static void Main() {
        var s1 = new PointS { X = 1 };
        var s2 = s1;  s2.X = 99;
        var c1 = new PointC { X = 1 };
        var c2 = c1;  c2.X = 99;
        Console.WriteLine("struct: s1.X = " + s1.X);
        Console.WriteLine("class:  c1.X = " + c1.X);
    }
}
