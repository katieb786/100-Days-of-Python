# import random
# import my_module
#
# # imports the random "Module"
#
# random_integer = random.randint(1, 10)
# # This will choose a random number between the two.
# print(random_integer)
#
# # You can create your own modules too by adding another python file - in this case the my_module file
# print(my_module.pi)
#
# # random.random() will give a float between 0.000000 - 0.999999999
# random_float = random.random()
# print(random_float)
#
# # to get a float between 0 and 5:
# random_float = random.random() * 5
#
# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")
#
# # Coin flip:
# coin = random.randint(0, 1)
# if coin == 0:
#     print("Tails")
# else:
#     print("Heads")
#
# ---------------------------------------------------------------------------------------------------------

# # Lists:
#
# # Store group pieces of data
# # list = [item1, item2]
states_of_america = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland',
                     'South Carolina', 'New Hampshire', 'Virginia', 'New York', 'North Carolina', 'Rhode Island',
                     'Vermont', 'Kentucky',
                     'Tennessee', 'Ohio', 'Louisiana', 'Indiana', 'Mississippi', 'Illinois', 'Alabama', 'Maine',
                     'Missouri', 'Arkansas',
                     'Michigan', 'Florida', 'Texas', 'Iowa', 'Wisconsin', 'California', 'Minnesota', 'Oregon', 'Kansas',
                     'West Virginia',
                     'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 'South Dakota', 'Montana', 'Washington', 'Idaho',
                     'Wyoming', 'Utah',
                     'Oklahoma', 'New Mexico', 'Arizona', 'Alaska', 'Hawaii']
# # The order you put items in is saved
# print(states_of_america[0])
# # Delaware
# # the first item in a list is 0 not 1
# # [] is related to lists
# # you can also use a negative index to count from the end of the list
# print(states_of_america[-1])
# # Hawaii
# # To change the spelling of an item:
# states_of_america[1] = "Pencilvania"
# print(states_of_america)
# # To add an item to the end of the list:
# states_of_america.append("Angelaland")
# print(states_of_america)
# # To add more items at once:
# states_of_america.extend(["Jack Bauer", "Katie Bondville"])
# print(states_of_america)
#
# import random
#
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
#
# number_of_names = len(names) - 1
# number = random.randint(0, number_of_names)
# payer = names[number]
# print(f"{payer} is going to buy the meal today!")

# ------------------------------------------------------------------------------------

# Index out of range error: Trying to get a position out of the total number of items.

# print(states_of_america[50]
num_of_states = len(states_of_america)
# print(states_of_america[num_of_states])

print(states_of_america[num_of_states - 1])

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches",
#                "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# Nested lists:

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

# ------------------------------------------------------------------------------------------------------------

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column = int(position[0]) - 1
row = int(position[1]) - 1

map[row][column] = "X"
print(f"{row1}\n{row2}\n{row3}")
