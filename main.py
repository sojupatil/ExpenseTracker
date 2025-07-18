import os
if os.path.exists("main.txt"):
    amount = int(input("Enter amount of item : "))
    category = input("Enter category of item : ")
    description = input("Enter description of item : ")
    date = input(f"Enter date on which you brought {description} : ")

    full_des = f"Brought {description} of Category {category} of {amount}$ on {date}\n"
    print(full_des)
    with open("main.txt","a") as file:
        file.write(full_des)

else:
    file = open("main.txt",'x')