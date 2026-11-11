using System;
using System.Linq;

class Program {
    static void Main() {
        var born = new[] {
            new { Name = "C", Year = 1972 },
            new { Name = "Objective-C", Year = 1984 },
            new { Name = "C++", Year = 1985 },
            new { Name = "C#", Year = 2000 },
        };
        var after1980 = born.Where(l => l.Year > 1980)
                            .OrderByDescending(l => l.Year)
                            .Select(l => l.Name + " (" + l.Year + ")");
        Console.WriteLine(string.Join(", ", after1980));
    }
}
