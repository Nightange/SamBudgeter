import classes as c
import aid_functions as f
import os
import time 
#Function that gets the user information
def get_user_info():
    print("Welcome to Sam's Budgeting Aid!")
    print("DISCLAIMER!!!: THIS WON'T HELP WITH TAXES OR ANYTHING OF THE SORT, IT IS JUST FOR ROUGH GUIDANCE!!")
    #figures out job type, creates an instance/object for that job type, while filtering user input 
    while True:
            job_type = input("Are you a wage worker($ per hour), salary worker($ per year), or contract worker($ per job)? Type in the first word ").lower()
            global user
            
            if job_type == "wage":
                dp = f.number_filter("What is your hourly pay? ")
                ot = f.number_filter("What is your overtime rate? ")
                user = c.wage(dp, ot)
                break
            elif job_type == "salary":
                dp = f.number_filter("What is your yearly salary(number only)? ")
                user = c.salary(dp)
                break
            elif job_type == "contract":
                dp = f.number_filter("How much do you make per contract(number only)? ")
                user = c.contract(dp)
                break
            else:
                print("\nPlease input the kind of worker you are \n")
    time.sleep(1)
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

# Menu function to display features and get user selection, runs the selected feature within the user object
def menu(person):
    print("Welcome to Sam's Budgeting Aid!")
    print("DISCLAIMER!!!: THIS WON'T HELP WITH TAXES OR ANYTHING OF THE SORT, IT IS JUST FOR ROUGH GUIDANCE!!\n")
    print("These are the features of this program:\n")
    print("1. Calculate your income 2. Calculate how much you should save 3. Calculate your expenses.")
    print("4. Calculate leftover income, post savings and expenses 5. Display previous information 6. Exit Program\n ")
    ft = f.get_number("Which feature would you like to use? (Type number of the feature you want) ")
    feature_selection = {
            1: person.income,
            2: person.savings,
            3: person.expenses,
            4: person.leftover_income,
            5: person.display_info,
            6: exit
        }
    feature_selection[ft]()
    

def main():
    #gets user info first
    get_user_info()            
    #begins next step, provides the menu for the features of this program
    menu(user)
    
                
if __name__ == "__main__":
    main()
