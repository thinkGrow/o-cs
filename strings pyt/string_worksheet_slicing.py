# Predict the output of slicing a string from index 2 to 5.

# string = "abcdefg"
# Predict the output
# prints : cdef
# print(string[2:5])

# 21. Given a string, extract and print the last three characters.
# input : Rahim
# output : him
# string = input("Enter a string: ")
# print(string[-3:])

# 24. Modify the slicing so that it removes the first and last characters from the string.

# input : Rahim
# output : ahi
# string = "Rahim"
# print(string[1:-1])

# 26. Write a program that checks if the word 'data' is found within a sentence entered by the user.

# string = 'Computer Science'
# check_string = 'data'
# if check_string in string:
#     print('Found')
# else:
#     print('Not Found')

# Bonus Challenge:
# 36. Write a program that takes a paragraph as input, converts it to lowercase, and verifies if the word 'python' appears in it.

string = "Lorem ipsum dolor sit amet consectetur adipisicing elit. python Officiis itaque veritatis et omnis enim voluptatum pariatur quae doloribus eveniet ipsum dolores inventore, maxime veniam reiciendis."

check_string = 'python'
if check_string in string:
    print('Found')
else:
    print('Not Found')
