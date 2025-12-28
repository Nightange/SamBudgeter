import time
import os
import main as m

# Helper functions for filtering user input 

#filters the user input to ensure it's a number/float
def number_filter(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("\nPlease make sure you only provide the number\n")
            

#filters the user input to ensure its one of the menu options
def get_number(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num < 1 or num > 6:
                print("\nPlease provide a number between 1 and 6.\n")
            else:
                return num
        except ValueError:
            print("\nPlease make sure you provide the number\n")
            

#calculator for wage workers, accounts for overtime that contract and salary workers don't have
def calculator(user, number):
    number *= user.dph
    number += (user.ot * user.dph) * number_filter("How many overtime hours did you work?(number only) ")
    return number


#compact function to calculate leftover income, determining on the term provided
def leftover_income_calculator(user, term):
    values = {
        "weekly": (user.wi, user.ws, user.wex),
        "monthly": (user.mi, user.ms, user.mex),
        "yearly": (user.yi, user.ys, user.yex)
    }
    income, savings, expenses = values[term]
    if income is None or savings is None or expenses is None:
        print("Please calculate your income, expenses, and savings for this term first")
        time.sleep(1.5)
        m.menu(user)
    else:
        li = income - (savings + expenses)
        return li
    

#filters out the term input from the user, making sure its weekly/monthly/yearly
def term_filter():
    while True:
        term = input("Which time period would you like to calculate for? (weekly, monthly, yearly) ").lower()
        if term == "weekly" or term == "monthly" or term == "yearly":
            return term
        else:
            print("\nPlease input a valid term\n")
            

#determines how much the user should save using their income and wanted saving percent
def savings_calculator(user, term):
        if user.wi == None and user.mi == None and user.yi == None:
            print("Please calculate your income for any time period first")
            time.sleep(1.5)
            m.menu(user)
        else:
            while True:
                saving_term = {
                    "weekly": user.wi,
                    "monthly": user.mi,
                    "yearly": user.yi
                }
                income = saving_term[term]
                if income != None:
                    sv = number_filter("What percentage of your income would you like to save?(number only) ")
                    sv = (sv / 100) * income
                    return sv
                print("\nPlease calculate your income for that time period first\n")
                m.menu(user)
                
                
#loops in order to get all expenses from the user and return the total
def expense_calculator():
    while True:
            ex_number = number_filter("How many expenses would you like to input?(number only) ")
            try:
                ex_number = int(ex_number)
                break
            except ValueError:
                print("\nPlease make sure you provide a whole number \n")
    expenses = []
    for i in range(ex_number):
        ex = number_filter("Please input your expense cost(number only) ")
        expenses.append(ex)
    return sum(expenses)


#returns all of the previous info the program has found
def get_user_info(user):
        print("Your information: \n")
        info_checker = {
            0: user.wi,
            1: user.mi,
            2: user.yi,
            3: user.ws,
            4: user.ms,
            5: user.ys,
            6: user.wex,
            7: user.mex,
            8: user.yex,
            9: user.wli,
            10: user.mli,
            11: user.yli
        }
        info_label = {
            0: "Weekly Income: $",
            1: "Monthly Income: $",
            2: "Yearly Income: $",
            3: "Weekly amount to save: $",
            4: "Monthly amount to save: $",
            5: "Yearly amount to save: $",
            6: "Weekly expenses: $",
            7: "Monthly expenses: $",
            8: "Yearly expenses: $",
            9: "Weekly leftover income: $",
            10: "Monthly leftover income: $",
            11: "Yearly leftover income: $"
        }
        for i in range(12):
            if info_checker[i] != None:
                print(info_label[i] + str(info_checker[i]))
                
                
#clears the screen just to make it look nicer
def clear_screen():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    

  