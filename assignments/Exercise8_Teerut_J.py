# Input username and password
userName = input("Please input your username: ")
passWord = input("Please input your password:")


if userName == "admin" and passWord == "1234":
    # Menu
    print(" Welcome to  Ice coffee shop ")
    print("#################################")
    print("                                 ")
    print("      Menu         | price (Baht)")
    print("1. Americano            40       ")
    print("2. Cappuccino           45       ")
    print("3. Latte                45       ")
    print("4. Mocha                55       ")
    print("                                 ")
    print("#################################")

    selectMenu = input(" please select your Menu :")
    if selectMenu == "1":
        menu = "Americano"
        price = 40
    elif selectMenu == "2":
        menu = "Cappuccino"
        price = 45
    elif selectMenu == "3":
        menu = "Latte"
        price = 45
    elif selectMenu == "4":
        menu = "Mocha"
        price = 55
    else:
        print(" Incorrect Menu ")

    if menu != "":
        menuNum = int(input(" How many cup of"+" "+menu+":"))
        # calculate

        totalPrice = menuNum*price

        print(" ############ Ice coffee shop ############ ")
        print("  Quantity    |  Description   |  unit price  ")
        print("     ", menuNum, "     ", "|", " ", menu, " " "|",  price)
        print("   ", "total :", totalPrice, "Baht")
        print(" ######################################### ")
        print(" ############# Thank you ################# ")

    else:
        print(" Thank you ")

else:

    print(" Incorrect Username or Password")
    print(" Thank you")


