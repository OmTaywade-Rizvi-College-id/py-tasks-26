import math

hypo = float(input("Enter the hypotenuse: "))
angel = float(input("Enter the angle in degrees: "))

adjacent = hypo * math.cos(math.radians(angel))
opposite = hypo * math.sin(math.radians(angel))

print(f"The length of the adjacent side is: {adjacent}")
print(f"The length of the opposite side is: {opposite}")