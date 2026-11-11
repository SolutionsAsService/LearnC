U8 s[16];                 // U8: an unsigned byte
StrCpy(s, "pointer");
I64 i = 0, j = StrLen(s) - 1;
U8 t;
while (i < j) {
  t = s[i]; s[i] = s[j]; s[j] = t;
  i++; j--;
}
"%s\n", s;
