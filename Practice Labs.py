# Lab-conditional 2-1
# Written by Gabe Mohs
# gabemohs12@gmail.com

#all y/n questions have the answer set to lower case as to check values against only one case
first_name = input("Please enter your first name: ").capitalize()
beach_q = input(f"Hi {first_name}, do you want to go to the beach? (y/n): ").lower()
if beach_q == "y":
    current_temp = int(input("Please tell me the current temperature: "))
    min_temp = int(input("What is the minimum temperature for going to the beach? "))
    if current_temp >= min_temp:
        print(f"You can go to the beach because it is {current_temp} degrees.")
        ice_cream_q = input("Do you want to buy an ice cream? (y/n): ").lower()
        if ice_cream_q == "y":
            user_cash = float(input("How much cash do you have? "))
            if user_cash > 0:
                ice_cream_cost = float(input("How much is an ice cream? "))
                if user_cash >= ice_cream_cost:
                    change = user_cash - ice_cream_cost
                    print(f"You can buy an ice cream and you will have ${change:.2f} left.")
                else:
                    print("Sorry, no ice cream today.")
            else:
                print("Please remember to bring cash next time.")
        #lack of else statement means this will print even if user does things with ice cream
        print("Enjoy your time at the beach.")
    else:
        print("It's not warm enough, stay at home.")
else:
    print("Ok, enjoy your time at home.")