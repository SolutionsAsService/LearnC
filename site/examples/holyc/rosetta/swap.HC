U0 Swap(I64 *a, I64 *b)   // U0: returns nothing (void)
{
  I64 t = *a; *a = *b; *b = t;
}

I64 x = 1, y = 2;
Swap(&x, &y);
"x=%d y=%d\n", x, y;
