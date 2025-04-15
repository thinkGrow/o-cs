arrayForm = ['7AXB', '7PDB', '7ARL', '7JEH']

form = input("Enter Form: ")

valid = False
index = 0
length = len(arrayForm)

while valid == False:
    if form == arrayForm[index]:
        valid = True
index = index + 1

print(valid)
