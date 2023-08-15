from Menu import *
from art import *



def compare(order, item):
    """This method compares the total price/amount left from the amount left in the resources to determine if there's enough."""
    total_price= MENU[order]["ingredients"][item]
    resource_amt= resources[item]
    if total_price > resource_amt:
        return False
    return True

def subtract(order, item):
    """This method subtracts the total price/amount left from the resources left in the coffee machine."""
    price= MENU[order]["ingredients"][item]
    reserve_amt= resources[item]
    subtraction= reserve_amt- price
    return subtraction

    
def money_check(quarters, dimes, nickels, pennies):
    """This method calculates the total money the user put in."""
    quarter= quarters*.25
    dime= dimes*.10
    nickel = nickels *.05
    pennie= pennies *0.01
    total= quarter+dime+nickel+pennie
    return total


def money_diff(order, total_added):
    """This method takes the difference between the total added by user and the cost of the item."""
    cost= MENU[order]["cost"]
    total= total_added- cost
    return total


def as_currency(amount):
    """This method converts numbers into currency."""
    if amount >= 0:
        return '${:,.2f}'.format(amount)
    else:
        return '-${:,.2f}'.format(-amount)
    
    

def coffee_art(item):
    """This prints coffee for the user."""
    print("\u2615")    # coffee emoji 
    return f"Here is your {item}! Have a great day!"


# Add money to resources. 
money= 0
resources['money']= 0


print("Welcome to the coffee shop!")
program_repeat= False


while not program_repeat:
    """This while loop takes user input and continues to show until user turns machine off."""
    user_choice= input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        program_repeat = True
    elif user_choice == "report":
        for key, value in resources.items():
            print(key, ':', value)    
    else:
        for item in MENU[user_choice]["ingredients"]:
            ingredient_check= compare(user_choice, item)
            if not ingredient_check:
                print(f"Sorry! We can't make this. There is not enough {item}.")
                game_play= True
            else:
                subtraction_amt= subtract(user_choice, item)
                resources[item] = subtraction_amt
        cost= MENU[user_choice]["cost"]
        cost_display = as_currency(cost)
        print(f"Your total is {cost_display}. Please insert money.")
        q_input= int(input("Quarters: "))
        d_input= int(input("Dimes: "))
        n_input= int(input("Nickels: "))
        p_input= int(input("Pennies: "))
        money_input= money_check(q_input, d_input, n_input, p_input)
        money_difference= money_diff(user_choice, money_input)
        money_display= as_currency(money_input)
        formatted_money_difference = as_currency(money_difference)  
        if money_difference < 0:
            print(f"This item costs {cost_display} and you have only added {money_display}. That is not enough, sorry!")  
            program_repeat= True
        else:
            resources['money'] += cost         
            print(f"You have entered {money_display}. Your change is {formatted_money_difference}")
            print_art= coffee_art(user_choice)
            print(print_art)
            