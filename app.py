import math

class Complex(object):

    def __init__(self, real, imag = 0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        return Complex((self.real * other.real) - (self.imag * other.imag),
            (self.imag * other.real) + (self.real * other.imag))

    def __truediv__(self, other):
        m = other.real ** 2 + other.imag ** 2
        return Complex((self.real * other.real + self.imag * other.imag) / m, 
            (self.imag * other.real - self.real * other.imag) / m)

    def __pow__(self, n):
        r = pow(math.hypot(self.real, self.imag), n)
        phi = n * ((math.pi / 2 - math.atan2(self.real, self.imag)) % (math.pi * 2))
        return Complex(math.cos(phi) * r, math.sin(phi) * r)


numbers = []
try:
    file = open("in.txt", "r")
    for line in file.readlines():
        try:
            numbers.append(float(line))
        except ValueError:
            numbers.append(1)
    file.close()
    try:
        x1 = numbers[0]
    except IndexError:
        x1 = 1
    try:
        i1 = numbers[1]
    except IndexError:
        i1 = 1
    try:
        x2 = numbers[2]
    except IndexError:
        x2 = 1
    try:
        i2 = numbers[3]
    except IndexError:
        i2 = 1
    try:
        n = numbers[4]
    except IndexError:
        n = 1

    a = Complex(x1, i1)
    b = Complex(x2, i2)
    sum = a + b
    dif = a - b
    prod = a * b
    quo = a / b
    pow = Complex(3, 2)**3

except IOError:
    print("Blad otwierania pliku")

file = open("out.txt", "w")
data = str(sum.real) + "\n" + str(sum.imag) + "\n" + str(dif.real) + "\n" + str(dif.imag) + "\n" + str(prod.real) + "\n" + str(prod.imag) + "\n" + str(quo.real) + "\n" + str(quo.imag) + "\n" + str(pow.real) + "\n" + str(pow.imag)
file.write(data)
file.close()