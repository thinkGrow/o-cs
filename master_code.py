# 1. INPUT
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
hobby = input("Enter your favorite hobby: ")

# 2. OUTPUT
print("\n--- User Details ---")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Hobby:", hobby)

# 3. OPERATORS
years_to_100 = 100 - age
print("\nIn", years_to_100, "years, you will be 100 years old.")
print("Height in cm:", height * 100)
print("Age divided by 3 (float):", age / 3)
print("Age divided by 3 (floor):", age // 3)
print("Remainder when age divided by 5:", age % 5)
print("Age to the power of 2:", age ** 2)

# Comparison
print("Are you a teenager?", age >= 13 and age <= 19)
print("Are you below 10 or above 60?", age < 10 or age > 60)
print("Not an adult?", not (age >= 18))

# 4. FOR-LOOP
print("\nCounting up to your age:")
for i in range(1, age + 1):
    if i % 5 == 0:
        print("🎉 Age milestone:", i)
    else:
        print("Year:", i)

# 5. WHILE-LOOP
print("\nWhile loop fun! Let's countdown from your age to 1:")
temp_age = age
while temp_age > 0:
    print("Countdown:", temp_age)
    temp_age -= 1

# 6. STRING SLICING
print("\n--- String Slicing ---")
print("Your name sliced (first 3 letters):", name[:3])
print("Your hobby last 3 letters:", hobby[-3:])

# 7. STRING UPPER
print("Name in UPPERCASE:", name.upper())

# 8. STRING LOWER
print("Hobby in lowercase:", hobby.lower())

# 9. STRING LENGTH
print("Length of your name:", len(name))

# 10. LISTS
friends = []
print("\nLet's add 3 of your friends to a list!")
for i in range(3):
    friend = input("Enter friend #{} name: ".format(i+1))
    friends.append(friend)

print("Your Friends List:", friends)
remove_name = input("Enter one friend to remove: ")
if remove_name in friends:
    friends.remove(remove_name)
    print(remove_name, "has been removed.")
else:
    print(remove_name, "not found in the list.")

print("Updated Friends List:", friends)

# 11. IF-ELSE
print("\n--- Status Checker ---")
if age >= 18:
    print("You are an adult!")
elif age == 17:
    print("You're almost an adult.")
else:
    print("You're still a minor.")