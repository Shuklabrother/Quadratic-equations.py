import cmath

print("Comparing the given Quadratic equation with their standard form \n")
a = int(input("Write a value of a:\n"))
b = int(input("Write a value of b:\n"))
c = int(input("Write a value of c:\n"))
d = (b**2)-(4*a*c)
p = (-b-cmath.sqrt(d))/(2*a) 
n = (-b+cmath.sqrt(d))/(2*a)
print("Solution of given quadratic equations is",p,n)