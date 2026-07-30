import math
print("Hello world")

x = 1
Y = 2

course = "Python programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])


# \"
# \'
# \\
# \n


course = "Python  \nProgramming"
print(course)


first = "Gilion"
last = "Biwott"
full = first + " " + last
print(full)


first = "Gilion"
last = "Biwott"
full = f"{len(first)} {2 + 2}"
print(full)


# strings methods
course = "  python programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.rstrip())
print(course.find("Pro"))
print(course.replace("p", "j"))
print("pro" in course)
print("swift" not in course)


# numbers
# integers
x = 1
# floats
x = 1.1
# complex numbers
x = 1 + 2j  # a + bi

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)

x = 10
x = x + 3
x += 3


print(round(2.9))
print(abs(-2.9))

print(math.ceil(2.2))

x = input("x: ")
print(type(x))
# y = x + 1

# int(x)
# float(x)
# bool(x)
# str(x)

x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")

fruit = "Apple"
print(fruit[1])

print(bool("False"))


temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")

print("Done")
