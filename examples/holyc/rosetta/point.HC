class CPoint         // class is a struct; there are no methods
{
  F64 x, y;
};

F64 Length(CPoint *p)
{
  return Sqrt(p->x * p->x + p->y * p->y);
}

CPoint pt;
pt.x = 3; pt.y = 4;
"%.1f\n", Length(&pt);
