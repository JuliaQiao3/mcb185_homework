def tm(a, c, g, t):
    len = a + c + g + t
    if len <= 13:
        Tm = (a + t) * 2 + (c + g) * 4
    else:
        Tm = 64.9 + 41 * (g + c - 16.4) / len
    return Tm

print(tm(5, 7, 3, 4))