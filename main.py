# A simple ATM implementation using Python

# Sample dictionary of registered users and their passwords
registered_users = {
    "Tayo": "tayo123",
    "Sharon": "sholly555",
    "Ahmed": "mypassword8"
}

registered_users_cash = {
    "Tayo": 60000,
    "Sharon": 300,
    "Ahmed": 24500
}

while True:
    print("Welcome")
    print("")
    print("Please make a selection:")
    print("Press 1 to Create an account")
    print("Press 2 to Log into an existing account")
    print("Press 3 to Cancel")
    print("")
    user_input = input()

    while (user_input != "1" and user_input != "2" and user_input != "3"):
        print("")
        print("Invalid input\n")
        user_input = input("Please enter either 1, 2 or 3 ")

    if user_input == "1":
        new_name = input("Enter your name: ")
        while (new_name in registered_users):
            print("Name already exist. Enter another name\n")
            new_name = input("Enter your name: ")

        new_password = input("Enter your password: ")
        while (len(new_password) < 5):
            print("Password should have more than 5 characters\n")
            new_password = input("Enter your password: ")

        confirm_password = input("Confirm password: ")
        while (new_password != confirm_password):
            print("Passwords don't match!\n")
            new_password = input("Enter your password: ")
            confirm_password = input("Confirm password: ")

        registered_users[new_name] = new_password
        registered_users_cash[new_name] = 0
        print("")
        print("Hello {}, you have been successfully registered!".format(new_name))
        print("")
        quest = input("Would you like to make another transaction: Y/n? ")

        while (quest != "Y" and quest != "N" and quest != "y" and quest != "n"):
            print("")
            quest = input("Would you like to make another transaction: Y/n? ")
        
        if quest == "N" or quest == "n":
            break

        else:
            pass


    if user_input == "2":
        user_name = input("Enter your name: ")
        while (user_name not in registered_users):
            print("Name does not exist\n")
            user_name = input("Enter your name: ")
            print("")

        user_password = input("Enter your password: ")
        while (user_password != registered_users[user_name]):
            print("Incorrect password\n")
            user_password = input("Enter your password: ")

        print("")
        print("Welcome {}. Please make a selection:".format(user_name))
        while True:
            print("Press 1 to Check account balance")
            print("Press 2 to Deposit")
            print("Press 3 to Withdraw")
            print("Press 4 to End\n")
            user_choice = input()

            while (user_choice != "1" and user_choice != "2" and user_choice != "3" and user_choice != "4"):
                print("Invalid choice.\n")
                user_choice = input("Please, select either 1, 2, 3, or 4" )

            if user_choice == "1":
                print("Your account balance is {}".format(registered_users_cash[user_name]))
                print("")
                quest = input("Would you like to make another transaction: Y/n? ")

            if user_choice == "2":
                dep_amount = int(input("How much wold you like to deposit? "))
                registered_users_cash[user_name] += dep_amount
                print("An amount of {} has been successfully deposited into your account".format(dep_amount))
                print("Acount balance: {}.".format(registered_users_cash[user_name]))
                print("")
                quest = input("Would you like to make another transaction: Y/n? ")

            if user_choice == "3":
                withdrawal_amount = int(input("How much woukd you like to withdraw? "))
                if withdrawal_amount > registered_users_cash[user_name]:
                    print("Insufficient funds")
                    print("")
                    quest = input("Would you like to make another transaction: Y/n? ")
                
                else:
                    registered_users_cash[user_name] -= withdrawal_amount
                    print("Withdrawal of {} was successful".format(withdrawal_amount))
                    print("Account balance: {}".format(registered_users_cash[user_name]))
                    print("")
                    quest = input("Would you like to make another transaction: Y/n? ")

            if user_choice == "4":
                break

            while (quest != "Y" and quest != "N" and quest != "y" and quest != "n"):
                print("")
                quest = input("Would you like to make another transaction: Y/n? ")
                        
            if quest == "N" or quest == "n":
                break
                    
            else:
                pass
        
        break

    if user_input == "3":
        break

print("Thank you for bankimg with us!")