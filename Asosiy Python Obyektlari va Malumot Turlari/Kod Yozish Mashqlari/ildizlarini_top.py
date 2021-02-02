"""
Kvadrat tenglamaning ildizlarini topish

Tenglama : ax^2 + bx + c

Diskriminantni topish:  b ** 2 -  4 * a * c

Birinchi ildiz : (-b - diskriminant ** 0.5) / (2*a)
Ikkinchi ildiz : (-b + diskriminant ** 0.5) / (2*a)

"""

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

diskriminant = b ** 2 - 4 * a *c

x1 = (-b - diskriminant ** 0.5 ) / (2 * a)
x2 = (-b + diskriminant ** 0.5 ) / (2 * a)

print("Birinchi ildiz: {}\nIkkinchi ildiz: {}\n".format(x1,x2))

