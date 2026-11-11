// Default arguments, and calling with no parentheses.
U0 Greet(U8 *name = "Terry", I64 times = 2)
{
  I64 i;
  for (i = 0; i < times; i++)
    "Hello, %s\n", name;
}

Greet;            // a call with no arguments needs no ()
Greet("World", 1);
Greet(, 3);       // skip the first argument, keep its default
