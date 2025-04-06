# 8. Enhance the program to also verify if the password contains at least one uppercase letter.

# password = input("Enter your password: ")

# for character in password:
#     if character.isupper():
#         uppercase_found = True
#     else:
#         uppercase_found = False

# if uppercase_found:
#     print("Password has atleast one uppercase letter.")
# else:
#     print("Password must contain atleast one uppercase letter.")


# 12. Modify the loop so that it prints the letters in reverse order.

# string = input("Enter your string: ")

# reversed_string = ""

# for i in range(len(string) - 1, -1, -1):
#     reversed_string = reversed_string + string[i]

# print("the right answer is:", reversed_string)


# Alternatively,
# txt = "Hello World"
# txt = txt [::-1]
# print(txt)

# 14. Write a loop that prints only the vowels in a given word.

# vowels = ['a','e','i','o','u']

# word = input("Enter your word: ")

# vowels_in_word = ""

# for char in word:
#     if char.lower() in vowels:
#         vowels_in_word += char + ","

# print(vowels_in_word)