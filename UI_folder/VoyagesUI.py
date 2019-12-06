from models.VoyagesModel import VoyagesModel
from LL_folder.LLAPI import LLAPI

class VoyagesUI():
    LENGTH_STAR = 20
    def __init__(self, llapi):
        self.llapi = llapi
    
    def choose_action(self):
        action_str = input("Choose action: ").lower()
        print()
        return action_str
    
    def show_voyage_menu(self):
        """This prints the voyage menu"""
        
        print(self.LENGTH_STAR * "*")
        print("VOYAGE MENU")
        print("1 Print overview of voyages")
        print("2 Create a voyage")
        print("3 Assign crew to flights")
        print("B Back")
        print("Q Quit")
            
        action_str = self.choose_action()
        
        while action_str != "q":
            if action_str == "1":
                self.show_voyage_overview()
            elif action_str == "2":
                self.show_create_voyage_menu()
            elif action_str == "3":
                self.show_not_staffed_voyages()
            elif action_str == "b":
                return
            else:
                print("Invalid action!")
                action_str = self.choose_action()

    def show_voyage_overview(self):
        """This prints the overview of all voyages"""
        
        print(self.LENGTH_STAR*"*")
        print("OVERVIEW OF VOYAGES")

        voyages = self.llapi.get_voyages_overview() #Kallar á fall i llapanum sem returnar öllum vinnuferðum og prenta út flugnúmer beggja flugferða
        print(voyages)

        print("B Back\n")

        action_str = self.choose_action()

        if action_str == "b":
            self.show_voyage_menu
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()
    
    def show_create_voyage_menu(self):
        """This prints the menu for create a voyage"""
        
        print(self.LENGTH_STAR*"*")
        print("CREATE A VOYAGE \n\n1 See common voyages\n2 Create a voyage manually\nB Back")
        print()

        action_str = self.choose_action()

        if action_str == "1":
            self.show_see_common()
        elif action_str == "2":
            self.show_create_manually_form()
        elif action_str == "b":
            self.show_voyage_menu()
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()

    def show_see_common(self):
        """This prints all the common voyages"""
        
        print(self.LENGTH_STAR*"*")
        print("SEE COMMON VOYAGES")
        self.llapi.get_common_voyages() #Þessi listi þarf að vera númeraður
        common_voyage = input("Choose a common voyage: ") #Þetta fer inní create a common voyage fallið
        #Hér þarf að vera einhver counter kóði eins og í emergency contact destinations :/

    def show_create_a_common_voyage_form(self):
        """This creates a voyage from the common voyages but with a new date and a new id"""
        
        print(self.LENGTH_STAR*"*")
        print("INPUT DEPARTURE DATE AND ARIPLANE ID")
        departure_date = input("Enter outbound departure date: dd/mm/yy: ")
        airplane_id = input("Enter airplane ID: ")
        pass #Eftir að klára þetta :)

    def show_create_manually_form(self): #Lista upp alla áfangastaði allar tímasetningar sem eru uppteknar allar flugvélar sem eru lausar
        """This prints the create a voyage manually form"""
        
        print(self.LENGTH_STAR*"*")
        print("CREATE A VOYAGE MANUALLY")
        print("\nDate")
        voyage_date = input("Enter outbound departure date(dd/mm/yy): ")
        print("\nTime")
        unavailable_time = self.llapi.get_unavailable_time_for_voyage() #Þetta prentar alla tímasetningar sem eru ekki í boði
        print(unavailable_time)
        voyage_time = input("Enter outbound departure time(hh:mm): ")
        print("\nDestination")
        destinations = self.llapi.get_destination_overview() #Þetta prentar alla áfangastaði, þetta þarf að vera númerað
        print(destinations)
        voyage_destination = input("Choose number of destination: ")
        print("\nAirplane")
        available_airplanes = self.llapi.get_available_airplanes_by_date(voyage_date)
        print(available_airplanes)
        voyage_airplane = input("Choose number of airplane: ")

        print("\n1 Assign crew to voyage\nS Save\nB Back\n")

        action_str = self.choose_action()

        if action_str == "1":
            #Takes the info and adds it to the voyage list
            print("\n*Voyage successfully created*")
            new_voyage = VoyagesModel(voyage_date, voyage_time, voyage_destination, voyage_airplane)
            #self.voyage.create_voyage(new_voyage)
            #Hérna þurfum við að skella þessu í lista/dictionary og svo fara einn til baka eða lenda aftur á þessum skjá
            self.show_assign_staff_form()

        elif action_str == "s":
            #Takes the info and adds it to the voyage list
            print("\n*Voyage successfully created*")
            new_voyage = VoyagesModel(voyage_date, voyage_time, voyage_destination, voyage_airplane)
            #self.voyage.create_voyage(new_voyage)
            #Hérna þurfum við að skella þessu í lista/dictionary og svo fara einn til baka eða lenda aftur á þessum skjá
            self.show_create_voyage_menu()

        elif action_str == "b":
            self.show_create_voyage_menu()
        
        else:
            print("Invalid action!")
            action_str = self.choose_action()

    def show_assign_staff_form(self):
        """This prints the form to assign a staff to a voyage"""
        
        print(self.LENGTH_STAR*"*")
        print("ASSIGN CREW TO VOYAGES")
        print("\nB Back") #Kannski sleppa
        #Listi yfir alla lausa pilots og þar þarf IO og fá date til að sjá hverjir eru lausar þennan dag
        pilot = input("Enter a pilot: ")
        #Listi yfir alla lausa cabincrew
        cabincrew = input("Enter a cabin crew member: ")
        
        print()
        
        #Þurfum meira hér til að klára þetta fall

    def show_not_staffed_voyages(self):
        """This prints all the not fully staffed voyages that are available"""
        
        print(self.LENGTH_STAR*"*")
        print("NOT FULLY STAFFED VOYAGES")
        not_staffed = self.llapi.get_not_staffed_voyages() #Þessi listi þarf að vera númeraður
        print(not_staffed)
        voyage_str = input("Choose a voyage")
        self.show_assign_staff_form() #Hérna fer ég með voyage_str í fallið
        