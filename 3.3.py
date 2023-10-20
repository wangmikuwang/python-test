def gcd_lcm(a, b):
    if a == 0 or b == 0:
        return None
    x = abs(a)
    y = abs(b)
    while y != 0:
        r = x % y
        x = y
        y = r
    gcd = x
    lcm = abs(a * b) // gcd
    return (gcd, lcm)
print(gcd_lcm(12, 18))
print(gcd_lcm(-15, 20))
print(gcd_lcm(0, 10))