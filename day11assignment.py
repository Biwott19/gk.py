#Print numbers from 1 to 50 with conditions
for number in range(1, 51):
    #Stop the progam completely when the number reaches 37
    if number == 37:
        break

    #Skip every multiple of 5
    if number % 5 == 0:
        continue

    print(number)
    
