class Rational(object):
    """ A rational or fraction class. Has magic methods for most basic math, intended for use with other Rationals or with integers.
    
        Includes methods for gcd and simplification, and operations automatically return simplified results."""
    def __init__(self, int_1, int_2):
        if int_2 == 0:
            raise(Exception("Denominator must be nonzero"))
        self.numerator = int_1
        self.denominator = int_2
        
    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)
        
    def __repr__(self):
        return 'Rational(' + str(self.numerator) + ', ' + str(self.denominator) + ')'
        
    def __add__(self, other):
        return Rational(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator).simplified()
        
    def __radd__(self, other):
        return Rational(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator).simplified()
    
    def __sub__(self, other):
        return Rational(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator).simplified()
        
    def __rsub__(self, other):
        return Rational(other.numerator * self.denominator - self.numerator * other.denominator, other.denominator * self.denominator).simplified()
        
    def __mul__(self, other):
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator).simplified()
        
    def __rmul__(self, other):
        return Rational(other.numerator * self.numerator, other.denominator * self.denominator).simplified()
    
    def __div__(self, other):
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator).simplified()
        
    def __rdiv__(self, other):
        return Rational(other.numerator * self.denominator, other.denominator * self.numerator).simplified()
    
    def __neg__(self):
        return Rational(-self.numerator, self.denominator)
        
    def normalized(self):
        a = self.numerator
        b = self.denominator
        if self.numerator < 0 and self.denominator < 0:
            a = -self.numerator
            b = -self.denominator
        if self.numerator > 0 and self.denominator < 0:
            a = -self.numerator
            b = -self.denominator
        return Rational(a, b)
            
    def gcd(self):
        a = self.numerator
        b = self.denominator
        while b != 0:
            t = b
            b = a % b
            a = t
        return a
    
    def lowest_terms(self):
        gcd = self.gcd()
        a = self.numerator/gcd
        b = self.denominator/gcd
        return Rational(a, b)
        
    def reduced(self):
        return self.lowest_terms()
        
    def simplified(self):
        return self.normalized().reduced()