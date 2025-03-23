
a = False

while a==False:
    age = int(input("Enter your age: "))
    if(age>=18):
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")
    a = int(input("Do you want to continue? 1 for yes, 0 for no: "))
    if (a==0): a=True
    elif(a==1): a=False



