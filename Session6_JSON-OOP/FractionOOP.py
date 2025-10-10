class Fraction:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def simplify(self):
        def gcd(a, b):
            a = abs(a)
            b = abs(b)
            while a != b:
                if a > b: a = a - b
                else: b = b - a
            return a
        gcd_tumau = gcd(self.tu, self.mau)
        self.tu = self.tu // gcd_tumau
        self.mau = self.mau // gcd_tumau
        # self.tu, self.mau = self.tu / gcd(self.tu, self.mau), self.mau / gcd(self.tu, self.mau)

    def print(self):
        print(self.tu, "/", self.mau, sep = "")

    def __add__(self, other):
        new_tu = self.tu * other.mau + self.mau * other.tu
        new_mau = self.mau * other.mau
        new_fraction = Fraction(new_tu, new_mau)
        new_fraction.simplify()
        return new_fraction


if __name__ == "__main__":
    a = Fraction(3, 6)
    b = Fraction(2, 4)
    a.simplify()
    a.print()
    c = a + b
    c.print()
