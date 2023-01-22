# # Data types:
#
# # Strings
#
# print("Hello"[4])
#
# # Subscripting is the position in a string you want.
#     # [0] is the first postition, and it goes up from there
# # Even putting numbers in "" will make it a string and not think of it as a number
#
# # Integer - whole numbers without decimal places
#
# print(123 + 345)
#
# # You can use underscores instead of commas for large numbers and it works the same
#
# print(123_456_789)
#
# # FLoat - floating point number - decimal places
#
# print(3.14159)
#
# # Boolean - True or false statement
#
# True
# False
#
# # Function - Does something
#
# # len() function only works for strings.
#     # It will give a type error if you put an int or float in it
# num_char = len(input("What is your name?"))
#
# new_num_char = str(num_char)
#
# print("Your name has " + new_num_char + " characters.")
#
# a = 123
# print(type(a))

# # Mathematical operations
#
# 3 + 5
# 7 - 4
# 3 * 2
# 6 / 3
# # / will always give float
# 2 ** 2
# # 2 to the power of 2
#
# # order of operations: PEMDAS
#     # ()
#     # **
#     # * == /
#     # + == -
#     # goes left to right
#
# print(3 * 3 + 3 / 3 - 3)
# 9 + 1 - 3
# 7
#
# # Rounding:
#     # 8 / 2.666, 2 the 2 is which place you want it rounded to
#
# print(round(8 / 2.66666, 2))
#
# # floor division with // will get rid of all decimals
#
# print(8 // 3)
#
# # math with a variable
#
# score = 0
#
# # User scores:
#
# score += 1
#
# print(score)
#
# # f strings - put f in front of string then use {} to put variables
#
# score = 0
# height = 1.8
# isWinning = True
#
# print(f"your score is {score}, your height is {height}, your are winning is {isWinning}")
