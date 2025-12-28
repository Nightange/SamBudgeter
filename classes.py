import main as m
import aid_functions as f
import time

#these classes are for the different worker types, wage/salary/contract

#the functions within each class use the aid functions to perform their calculations, and store the results within the user object

#each function is similar between classes, though there are slight differences on how the information is processed

#this is due to the different payment structures of each worker type, requiring different calculations

class wage:
    def __init__(self, dph, ot):
        self.dph = dph
        self.ot = ot
        
        self.wi = None
        self.mi = None
        self.yi = None
        
        self.ws = None
        self.ms = None
        self.ys = None
        
        self.wex = None
        self.mex = None
        self.yex = None
        
        self.wli = None
        self.mli = None
        self.yli = None
        
    
    def income(self):
        term = f.term_filter()
        if term == "weekly":
            wi = f.number_filter("How many hours did you work this week?(number only) ")
            self.wi = f.calculator(self, wi)
            print("Your weekly income is: $" + str(self.wi))
        elif term == "monthly":
            mi = f.number_filter("How many hours did you work this month?(number only) ")
            self.mi = f.calculator(self, mi)
            print("Your monthly income is: $" + str(self.mi))
        elif term == "yearly":
            yi = f.number_filter("How many hours did you work this year?(number only) ")
            self.yi = f.calculator(self, yi)
            print("Your yearly income is: $" + str(self.yi))
        time.sleep(1.5)
        f.clear_screen()
        m.menu(self)
       
        
    def savings(self):
        term = f.term_filter()
        if term == "weekly":
            self.ws = f.savings_calculator(self, "weekly")
            print("You should save: $" + str(self.ws))
        elif term == "monthly":
            self.ms = f.savings_calculator(self, "monthly")
            print("You should save: $" + str(self.ms))
        elif term == "yearly":
            self.ys = f.savings_calculator(self, "yearly")
            print("You should save: $" + str(self.ys))
        time.sleep(1.5)
        f.clear_screen()
        m.menu(self)
        
        
    def expenses(self):
        term = f.term_filter()
        if term == "weekly":
            self.wex = f.expense_calculator()
            print("Your total expenses are: $" + str(self.wex))
        elif term == "monthly":
            self.mex = f.expense_calculator()
            print("Your total expenses are: $" + str(self.mex))
        elif term == "yearly":
            self.yex = f.expense_calculator()
            print("Your total expenses are: $" + str(self.yex))
        time.sleep(1.5)
        f.clear_screen()
        m.menu(self)
        
    def leftover_income(self):
        term = f.term_filter()
        if term == "weekly":
            self.wli = f.leftover_income_calculator(self, "weekly")
            print("Your leftover income is: $" + str(self.wli))
        if term == "monthly":
            self.mli = f.leftover_income_calculator(self, "monthly")
            print("Your leftover income is: $" + str(self.mli))
        if term == "yearly":
            self.yli = f.leftover_income_calculator(self, "yearly")
            print("Your leftover income is: $" + str(self.yli))
        time.sleep(1.5)
        f.clear_screen()
        m.menu(self)

    def display_info(self):
        f.get_user_info(self)
        time.sleep(5)
        f.clear_screen()
        m.menu(self)
                
        
        
class salary:
    
    def __init__(self, dpy):
        self.dpy = dpy
        
        self.wi = None
        self.mi = None
        self.yi = None

        self.ws = None
        self.ms = None
        self.ys = None
        
        self.wex = None
        self.mex = None
        self.yex = None
        
        self.wli = None
        self.mli = None
        self.yli = None
        
    def income(self):
        term = f.term_filter()
        if term == "weekly":
            wi = self.dpy / 52
            wi += f.number_filter("How much did you receive in bonuses?(number only) ")
            self.wi = wi
            print("Your weekly income is: $" + str(self.wi))
        elif term == "monthly":
            mi = self.dpy / 12
            mi += f.number_filter("How much did you receive in bonuses?(number only) ")
            self.mi = mi
            print("Your monthly income is: $" + str(self.mi))
        elif term == "yearly":
            yi = self.dpy
            yi += f.number_filter("How much did you receive in bonuses?(number only) ")
            self.yi = yi
            print("Your yearly income is: $" + str(self.yi))
        time.sleep(1.5)
        f.clear_screen()
        m.menu(self)
    
    def savings(self):
        term = f.term_filter()
        if term == "weekly":
            self.ws = f.savings_calculator(self, "weekly")
            print("You should save: $" + str(self.ws))
        elif term == "monthly":
            self.ms = f.savings_calculator(self, "monthly")
            print("You should save: $" + str(self.ms))
        elif term == "yearly":
            self.ys = f.savings_calculator(self, "yearly")
            print("You should save: $" + str(self.ys))
        time.sleep(1.5)
        f.clear_screen()
        m.menu(self)
    
    def expenses(self):
        term = f.term_filter()
        if term == "weekly":
            self.wex = f.expense_calculator()
            print("Your total expenses are: $" + str(self.wex))
        elif term == "monthly":
            self.mex = f.expense_calculator()
            print("Your total expenses are: $" + str(self.mex))
        elif term == "yearly":
            self.yex = f.expense_calculator()
            print("Your total expenses are: $" + str(self.yex))
        time.sleep(1.5)
        f.clear_screen()
        m.menu(self)
    
    def leftover_income(self):
        term = f.term_filter()
        if term == "weekly":
            self.wli = f.leftover_income_calculator(self, "weekly")
            print("Your leftover income is: $" + str(self.wli))
        if term == "monthly":
            self.mli = f.leftover_income_calculator(self, "monthly")
            print("Your leftover income is: $" + str(self.mli))
        if term == "yearly":
            self.yli = f.leftover_income_calculator(self, "yearly")
            print("Your leftover income is: $" + str(self.yli))
        time.sleep(1.5)
        f.clear_screen()
        m.menu(self)
    
    def display_info(self):
        f.get_user_info(self)
        time.sleep(5)
        f.clear_screen()
        m.menu(self)
        
        
class contract:
    
    def __init__(self, dpc):
        self.dpc = dpc
        
        self.wi = None
        self.mi = None
        self.yi = None

        self.ws = None
        self.ms = None
        self.ys = None
        
        self.wex = None
        self.mex = None
        self.yex = None
        
        self.wli = None
        self.mli = None
        self.yli = None
        
    def income(self):
        term = f.term_filter()
        if term == "weekly":
            wi = f.number_filter("How many contracts did you complete this week?(number only) ")
            self.wi = wi * self.dpc
            print("Your weekly income is: $" + str(self.wi))
        elif term == "monthly":
            mi = f.number_filter("How many contracts did you complete this month?(number only) ")
            self.mi = mi * self.dpc
            print("Your monthly income is: $" + str(self.mi))
        elif term == "yearly":
            yi = f.number_filter("How many contracts did you complete this year?(number only) ")
            self.yi = yi * self.dpc
            print("Your yearly income is: $" + str(self.yi))
        time.sleep(1.5)
        f.clear_screen()
        m.menu(self)
    
    def savings(self):
        term = f.term_filter()
        if term == "weekly":
            self.ws = f.savings_calculator(self, "weekly")
            print("You should save: $" + str(self.ws))
        elif term == "monthly":
            self.ms = f.savings_calculator(self, "monthly")
            print("You should save: $" + str(self.ms))
        elif term == "yearly":
            self.ys = f.savings_calculator(self, "yearly")
            print("You should save: $" + str(self.ys))
        time.sleep(1.5)
        f.clear_screen()
        m.menu(self)
    
    def expenses(self):
        term = f.term_filter()
        if term == "weekly":
            self.wex = f.expense_calculator()
            print("Your total expenses are: $" + str(self.wex))
        elif term == "monthly":
            self.mex = f.expense_calculator()
            print("Your total expenses are: $" + str(self.mex))
        elif term == "yearly":
            self.yex = f.expense_calculator()
            print("Your total expenses are: $" + str(self.yex))
        time.sleep(1.5)
        f.clear_screen()
        m.menu(self)
        
    def leftover_income(self):
        term = f.term_filter()
        if term == "weekly":
            self.wli = f.leftover_income_calculator(self, "weekly")
            print("Your leftover income is: $" + str(self.wli))
        if term == "monthly":
            self.mli = f.leftover_income_calculator(self, "monthly")
            print("Your leftover income is: $" + str(self.mli))
        if term == "yearly":
            self.yli = f.leftover_income_calculator(self, "yearly")
            print("Your leftover income is: $" + str(self.yli))
        time.sleep(1.5)
        f.clear_screen()
        m.menu(self)
    
    def display_info(self):
        f.get_user_info(self)
        time.sleep(5)
        f.clear_screen()
        m.menu(self)