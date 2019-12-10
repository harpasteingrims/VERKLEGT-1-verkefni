from LL_folder.LLAPI import LLAPI
import datetime

class IAADUI():
    LENGTH_STAR = 20
    
    def __init__(self, llapi):
        self.llapi = llapi

    def choose_action(self):
        action_str = input("Choose action: ").lower()
        print()
        return action_str

    def show_IAAD_menu(self, user_input_date, user_input_time=0):
        """This prints the employee menu"""
    
        action_str = ""

        while True:
            print()
            print(self.LENGTH_STAR * "*")
            print("1 Available employees")
            print("2 Unavailable employees")
            print("3 Status of voyages")
            print("4 Status of airplanes")
            print("B Back")
            print()
            
            action_str = self.choose_action()

            if action_str == "1":
                self.show_available_employees(user_input_date)

            elif action_str == "2":
                self.show_unavailable_employees(user_input_date)

            elif action_str == "3":
                self.show_enter_time_menu_voyage(user_input_date)

            elif action_str == "4":
                self.show_enter_time_menu_airplane(user_input_date)

            elif action_str == "b":
                return
                
            else:
                print("Invalid action!")

    def show_enter_date_menu(self):
        """This prints the menu for choosing date to get information about""" 

        print()
        print(self.LENGTH_STAR * "*")
        print("INFORMATION ABOUT A DAY")
        print()
        iaad_year = self.get_iaad_year()
        iaad_month = self.get_iaad_month(iaad_year)
        iaad_day = self.get_iaad_day(iaad_month, iaad_year)
        year, month, day = int(iaad_year), int(iaad_month), int(iaad_day)
        print()
        user_input_date = datetime.datetime(year, month, day, 0, 0, 1).isoformat()

        self.show_IAAD_menu(user_input_date)
        """ This prints out, input date """
        return user_input_date

    def show_enter_time_menu_voyage(self, user_input_date):
        iaad_hour = input("Enter hour (hh): ")
        iaad_minute = input("Enter minute(mm): ")
        print()
        list_user_input_date = list(user_input_date)
        list_user_input_date[11:13] = iaad_hour
        list_user_input_date[14:16] = iaad_minute
        user_input_time = "".join(list_user_input_date)
        self.show_voyages_status(user_input_time)

    def show_enter_time_menu_airplane(self, user_input_date):
        iaad_hour = input("Enter hour (hh): ")
        iaad_minute = input("Enter minute(mm): ")
        print()
        list_user_input_date = list(user_input_date)
        list_user_input_date[11:13] = iaad_hour
        list_user_input_date[14:16] = iaad_minute
        user_input_time = "".join(list_user_input_date)
        self.show_airplane_status(user_input_time)
    
    def show_available_employees(self, user_input_date):
        """This prints the available employees from a certain day"""

        print(self.LENGTH_STAR * "*")
        print("AVAILABLE EMPLOYEES")

        available_employess = self.llapi.get_available_emp_by_date(user_input_date)
        print(available_employess)

        print()
        print("B Back")
       
        action_str = self.choose_action()

        if action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()

    def show_unavailable_employees(self, user_input_date): #Hérna þurfa að fylgja til hvaða áfangastaði starfsmennirnar eru að fara
        """This prints the unavailable employees on a certain day"""

        print(self.LENGTH_STAR * "*")
        print("UNAVAILABLE EMPLOYEES")

        unavailable_employess = self.llapi.get_unavailable_emp_by_date(user_input_date)
        print(unavailable_employess)

        print()
        print("B Back")

        action_str = self.choose_action()

        if action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()

    def show_airplane_status(self, user_input_date):
        """This prints the status of airplanes on a certain day"""

        print(self.LENGTH_STAR * "*")
        print("AIRPLANE STATUS")

        airplane_status = self.llapi.get_airplane_status_by_date(user_input_date)
        if airplane_status != []:
            for airplane_elem in airplane_status:
                    print(f"{airplane_elem[0]}, {airplane_elem[1]}, {airplane_elem[2]}, {airplane_elem[3]}, {airplane_elem[4]}, {airplane_elem[5]}")

        else:
            print("\nThe airplane is not flying at this time")

        print()
        print("B Back")

        action_str = self.choose_action()

        if action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()
   
    def show_voyages_status(self, user_input_date):
        """This prints the status of a voyage on a certain day"""

        print(self.LENGTH_STAR * "*")
        print("VOYAGE STATUS")
        
        voyage_status = self.llapi.get_voyages_status_by_date(user_input_date)
        print(voyage_status)

        print()
        print("B Back")

        action_str = self.choose_action()

        if action_str == "b":
            return
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()

    def get_iaad_year(self):
        iaad_year = input("Enter year (yyyy): ")
        iaad_year_check = self.llapi.check_iaad_year(iaad_year)

        if iaad_year_check:
            return iaad_year_check
        else:
            print("\nInvalid year\n")
            self.get_iaad_year()

    def get_iaad_month(self, iaad_year):
        iaad_month = input("Enter month (mm): ")
        iaad_month_check = self.llapi.check_iaad_month(iaad_month, iaad_year)

        if iaad_month_check:
            return iaad_month_check
        else:
            print("\nInvalid month\n")
            self.get_iaad_month(iaad_year)

    def get_iaad_day(self, iaad_month, iaad_year):
        iaad_day = input("Enter day (dd): ")
        iaad_day_check = self.llapi.check_iaad_day(iaad_day, iaad_month, iaad_year)

        if iaad_day_check:
            return iaad_day_check
        else:
            print("\nInvalid day\n")
            self.get_iaad_day(iaad_month, iaad_year)