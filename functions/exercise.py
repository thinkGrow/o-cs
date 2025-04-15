# 1. Greet Someone
# Write a function called greet that takes a name as an argument and prints:
# "Hello, <name>!"

# 2. Add Two Numbers
# Write a function called add_numbers that takes two numbers and returns their sum.

# 4. Find the Square
# Write a function called square that takes a number and returns its square.

# 5. Repeat a Word
# Write a function called repeat_word that takes a word and a number n, and returns the word repeated n times (as a single string).

# 1. 
# def greet(name):
#     return "Hi, " + name + "!"

# name = input("Enter your name: ")
# print(greet(name))

# # 2. 
# def add_numbers(num1, num2):
#     return num1 + num2

# x = int(input("Enter your first number: "))
# y = int(input("Enter your secound number: "))

# print(add_numbers(x,y))

# 3. Even or Odd
# Write a function called is_even that takes a number and returns True if it's even, False otherwise

# 3.
# def is_even(num):
#     if(num%2 == 0):
#         print("Even")
#     else:
#         print("Odd")

# x = int(input("Enter a number: "))
# is_even(x)

# def is_even(num): 
#     even = False
#     if(num%2 == 0):
#         even = True
#     return even

# x = int(input("Enter a number: "))
# print(is_even(x))

# 4. 
# def square(num):
#     num_squared = num * num
#     return num_squared

# x = int(input("Enter your number: "))
# print(square(x))

# 5. Repeat a Word
# Write a function called repeat_word that takes a word and a number n, and returns the word repeated n times (as a single string).

def repeat_word(word, n):
    word = word + "\n"
    return word * n

a = repeat_word("Messi", 10)

print(a)