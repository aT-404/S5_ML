import math

r=int(input("Enter the radius of the cylinder: "))
h=int(input("Enter the height of the cylinder: "))

def surf_ar(r,h):
    sa=2*r*h*math.pi
    return sa

def volume(r,h):
    vol=math.pi*r**2*h
    return vol

sa=surf_ar(r,h)
vol=volume(r,h)

print("\nThe surface area of the cylinder is:",sa,"\nThe volume of the cylinder is:",vol)
