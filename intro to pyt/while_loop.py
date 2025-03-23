# number = 1

# while number <=20:
#     number = int(input('Please enter a number: '))

# print("You entered a number greater than 20 ")


# Number Calculation Game
answer = 1
count = 0
result = True

while answer != 4:
    answer = int(input('What is 3 + 1? '))
    print("Wrong Answer. Try again!")
    count = count + 1
    print(f"You only have {3 - count} tries left")

    if count == 3: 
        result = False
        break

if result == True:
    print("Congrats! You've beaten the game ")