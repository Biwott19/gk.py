print('hello, world')
print('today is day 5 of learning python')
print('-----------------------------------------')
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
#printing greetings using string concatenation
print('whats up' + first_name )
#reading integer input and calculating age dynamically
birth_year = int(input('where were you born ? '))
caclculated_age =2026 - birth_year
print (f'You are {caclculated_age} years old')
#reading float input and calculating height dynamically
height = float(input('wthat is your height in meters? '))
print(f'Your height is {height} meters')
#Demonstrating type casting(converting integer age to a float decimal)
(f'age converted to a float decimal is {float(caclculated_age)}')
print('-----------------------------------------\n')
#---part 2: stringsand inexing ---
print('==========STRINGS AND INDEXING=========')
county = 'Nairobi'
print(county[0]) #first character -> 'N'
print(county[1]) #second character -> 'a'
print(county[-1]) #last character -> 'i'
print(county[:4]) #slicces first four characters -> 'Nair'
print('-----------------------------------------\n')
#---part 3: ADVANCED STRINGS METHODS ---
print('========== STRING TRANSFORMS=========')
full_name = f' {first_name} {last_name}' # Text with intentional spaces 
print(f'uppercase name : {full_name.upper()}') 
print(f'lowercase name : {full_name.lower()}')
print(f'original name with spaces : {full_name}')
print(f'cleaned name (with strip) : {full_name.strip()}') 
#Splitting text into a list of words
sample_phrase = 'computer science student'
split_words = sample_phrase.split()
print(f'original phrase: {sample_phrase}')
print(f'split list:     {split_words}')
print('-----------------------------------------\n')
#---part 4:DATA TYPE INSPECTION ---
print('==========DATA TYPE INSPECTION=========')
print(f'first name: {type(first_name)}')
print(f'birth year: {type(birth_year)}')
print(f'height: {type(height)}')
print(f'split words: {type(split_words)}')
print('=========================================')

