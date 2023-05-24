MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
inserted_money = float

another_coffe = True
while another_coffe:
    # 1 Prompt user by asking What would you like? (espresso/latte/cappuccino)
    choose = input("What would you like? (espresso/latte/cappuccino):")

    # 2 Turn off the Coffee Machine by entering “off” to the prompt.
    if choose == 'off':
        another_coffe = False
    # 3 Print report


    def report(current_money):
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        money = current_money
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")


    if choose == "report":
        report(inserted_money)

    # 4 Check resources sufficient?
    def check_resources(type_coffee):
        global milk, milk_needed
        water_needed = int(MENU[f"{type_coffee}"]["ingredients"]["water"])

        coffee_needed = int(MENU[f"{type_coffee}"]["ingredients"]["coffee"])

        water = int(resources["water"])

        coffee = int(resources["coffee"])

        if type_coffee != "espresso":
            milk_needed = int(MENU[f"{type_coffee}"]["ingredients"]["milk"])
            milk = int(resources["milk"])
            if milk_needed > milk:
                print("Sorry there is not enough milk.")
        elif water_needed > water:
            print("Sorry there is not enough water.")
        elif coffee_needed > coffee:
            print("Sorry there is not enough coffee.")

        new_amount_water = water - water_needed
        new_amount_coffee = coffee_needed - coffee

        resources["water"] = new_amount_water
        resources["coffee"] = new_amount_coffee
        if type_coffee != "espresso":
            new_amount_milk = milk_needed - milk
            resources["milk"] = new_amount_milk


    # 5 Process coins
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    inserted_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    print(inserted_money)

    print(f"Here is ${inserted_money} in change.")
    # 6 Check transaction successful?
    check_resources(choose)

    # 7 Make Coffee.
    print(f"Here is your {choose} ☕️. Enjoy!")