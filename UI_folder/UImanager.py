import sys
sys.path.insert(1, '~/VERKLEGT-1-verkefni/')

from LL_folder.LLAPI import LLAPI
from UI_folder.EmployeesUI import EmployeesUI
from UI_folder.VoyagesUI import VoyagesUI
from UI_folder.DestinationsUI import DestinationsUI
from UI_folder.AirplanesUI import AirplanesUI
from UI_folder.IAADUI import IAADUI

class UImanager():
    
    def __init__(self):
        self.llapi = LLAPI()
        self.employee = EmployeesUI()
        self.voyages = VoyagesUI()
        self.destination = DestinationsUI()
        self.airplanes = AirplanesUI()

    def MainmenuUI(self):
        #Just to start things up
        run = True
        
        while run is True:
            print("*" * self.LENGTH_STAR)
            print("MAIN MENU\n\n1 Employees\n2 Voyages\n3 Destinations\n4 Airplanes\n5 Search a date\n")
        
            #Hérna vantar input check, break ef >5 og setja run í false
            action = input("Choose action: ").lower()
            print()
            if action == "1":
                EmployeesUI.show_employee_menu(self)

            elif action == "2":
                VoyagesUI.show_voyage_menu(self)

            elif action == "3":
                DestinationsUI.show_destination_menu(self)

            elif action == "4":
                AirplanesUI.show_airplane_menu(self)

            elif action == "5":
                IAADUI.show_enter_date(self)
            
            elif action == "q" or action > 5:
                run = False
                break
    

#def main():
#    menu = MainmenuUI()
#    menu.show_main_menu()

#main()