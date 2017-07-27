"""
a class that can represent a rational number i.e a fraction 
"""


class Rational:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def __repr__(self):
        """gives a string of the fraction"""
        return "%d/%d" % (self.numerator, self.denominator)

    def simplify(self):
        """simplify a fraction 10/20 = 1/2"""
        for n in range(2, self.numerator + 1):
            if self.numerator % n == 0 and self.denominator % n == 0:
                self.numerator = int(self.numerator / n)
                self.denominator = int(self.denominator / n)

    def __add__(self, other):
        """adds the num and den accordingly"""
        top = self.numerator * other.denominator + other.numerator * self.denominator
        bot = self.denominator * other.denominator
        return Rational(top, bot)

    def __sub__(self, other):
        """subtracts the num and den accordingly"""
        top = self.numerator * other.denominator - other.numerator * self.denominator
        bot = self.denominator * other.denominator
        return Rational(top, bot)

    def __mul__(self, other):
        """multiply the two fractions"""
        top = self.numerator * other.numerator
        bot = self.denominator * other.denominator
        return Rational(top, bot)

    def __truediv__(self, other):
        """dividing two fractions"""
        top = self.numerator * other.denominator
        bot = self.denominator * other.numerator
        return Rational(top, bot)
    
    def equal(self, other):
        """checks if two fractions are equal"""
        return self.numerator == other.numerator and self.denominator == self.denominator

    def __float__(self):
        """returns the rational as a float"""
        return self.numerator / self.denominator


num = Rational(10, 20)
print(num)
#
# num2 = Rational(5, 8)
# print(num2)
# c = num + num2
# print(c)
# num3 = Rational(1, 2)
# print(num.equal(num2))
# print(num.equal(num3))
# print(num2.equal(c))
# print(num.__float__())
# print(c.__float__())


