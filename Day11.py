# 1GRADE CALCULATION
# Write a code that accepts an input on grades scored in a test and then you will output them as A, B, C, D  E fail
# 80 - 100 A
# 70 - 79 B
# 60 -69 C
# 50 - 59 D
# 40-49 E
# Below 40 Fail

# 2 LOG IN SYSTEM
# Will accept the username and password
# USERNAME - THURSDAY
# PASSWORD - 90DAYS

# 3 MULTIPLICATION TABLE

grade = input("enter your grade: ")

if 80 <= grade <= 100:
    print("A")
elif 70 <= grade <= 79:
    print("B")
elif 60 <= grade <= 69:
    print("C")
elif 50 <= grade <= 59:
    print("D")
elif 40 <= grade <= 49:
    print("E")
elif 40 < grade:
    print("fail")
else:
    print("error")
