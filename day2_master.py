#===================================
#Day 2 master assignment :unified git walkthrough &list
#File name:day2_master.py
#---part 1:BASIC PRINTING (From Git walkthrough Guide)---
print('=========GIT WALKTHROUGH CHECK==========')
print('hello,world')
print("File 'day2_master.py' sucessfully created!")
print('-----------------------------------------\n')
#---PART 2:CHALLENGE MISSION (from about_me.py setup)---
print('==========ABOUT ME MISSION==========')
name = 'Gilion Biwott'
course = 'Computer science'
dream_career = 'AI Engineer'
print(f'Hi,I am {name}')
print(f'I dream of becoming a {dream_career}')
print('--------------------------------------\n')
#---PART 3: HOMEWORK CHALLENGE (From favorite_things.py list loop)---
print('==========MY FAVORITE THINGS ==========')
#storing your top 5 favorite tech choices in clean lists
favorite_languages =['python', 'javascript']
favorite_frameworks =['React', 'django']
favorite_tools = ['vs code', 'github' , 'git']
#iterating and printing individual items using a for loop 
print("Favorite langauges:")
for lang in favorite_languages:
    print(f"  -{lang}")
print("\nnFavorite Frameworks:") 
for framework in favorite_frameworks:
    print(f" -{framework}")
print("\nFavorite tools:")  
for tool in favorite_tools:
    print(f" -{tool}") 
print("------------------------------\n") 
#---PART 4: DATA TYPE INSPECTION---
print("========== DATA TYPE INSPECTION ==========")
print(f"name:                {type(name)}") 
print(f"favorite_languages: {type(favorite_languages)}")
print("===========================================")



