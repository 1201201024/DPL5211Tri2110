import math

radius = float(input("Please enter the radius : "))
volume = 4 * math.pi * pow(radius, 3) / 3
SurfaceArea = 4 * math.pi * pow(radius, 2)
print("Volume : {:.2f}".format(volume))
print("Surface Area : {:.2f}".format(SurfaceArea))
