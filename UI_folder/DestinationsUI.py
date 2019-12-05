from models.DestinationsModel import DestinationsModel
from LL_folder.LLAPI import LLAPI

class DestinationsUI():
    LENGTH_STAR = 20
    def __init__(self, llapi):
        #self.destination = LLAPI()
        self.llapi = llapi
    
    def show_destination_menu(self):
        """This prints the destination menu"""

        print("*"*self.LENGTH_STAR)
        print("DESTINATIONS\n")
        print("1 Print overview of destinations \n2 Create a new destination \n3 Get emergency contact ")
        print("B back\n")
        action_str = input("Choose action: ").lower()

        if action_str == "1":
            self.show_destination_overview()
        elif action_str == "2":
            self.show_create_des_form()
        elif action_str == "3":
            self.show_emerg_country_menu()
        elif action_str == "b":
            return

    def show_destination_overview(self):
        """This prints the overview of all destinations"""

        print("*"*self.LENGTH_STAR)
        print("OVERVIEW OF DESTINATIONS\n")
        
        destinations = self.llapi.get_destinations_overwiew() #Hérna kallar hann í fall í llapanum sem heitir get_destinations_overview sem returnar lista yfir alla áfangastaði
        print(destinations)
        
        print("B back\n")
        action_str = input("Choose action: ").lower() 
        if action_str == "b":
            return
            #self.show_destination_menu()

    def show_create_des_form(self):
        """ This prints the create a destination form"""

        print("*"*self.LENGTH_STAR)
        print("CREATE A NEW DESTINATION\n")
        country = input("Enter country: ")
        airport = input("Enter airport: ")
        flight_duration = input("Enter flight duration from Iceland: ")
        distance = input("Enter distance from Iceland: ")
        contact = input("Enter name of contact: ")
        contact_phone = input("Enter emergency contact")
        new_destination = DestinationsModel(country, airport, flight_duration, distance, contact, contact_phone)
        #self.destination.create_destination(new_destination)

        action_str = input("Choose action: ").lower() 
        #if action_str == "s"
            #from UI-layer import FALL SEM VINNUR MEÐ ÞETTA
        if action_str == "b": #Á AÐ VERA ELIF HÉR 
            return

    def show_emerg_country_menu(self):
        """This prints the emergency contact menu"""

        print("*"*self.LENGTH_STAR)
        print("GET EMERGENCY CONTACT\n")
        #tekur inn countries_list
        #counter = 1
        #find_country = {}
        #finc_country_list = []
        #for country in countries_list:
            #print(counter," ",country)
            #find_country[counter] = country
            #find_country_list.append(find_country)
            #country += 1

        print("B back")
        action_str = input("Choose action: ").lower()
        
        if action_str == "b":
            return 

    def show_emergency_contact(self):
        """This prints the emergency contact for a specific country"""

        print("*"*self.LENGTH_STAR)
        print("EMERGENCY CONTACT OF\n") #Hérna vantar að setja inn country
        #ÞARF AÐ FINNA LANDIÐ MEÐ ÞVÍ AÐ SÆKJA LISTA AF CONTACTS Í LL-LAYER
        #CONTACTS ERU GEYMDIR Í DICT MEÐ LAND SEM KEY, FINN NAFN SEM 
        #ER SAMA NAFN OG VALUE 
        # info_of_contact = # Calls the class that holds the information of contact and prints it
        # Name:
        # Phone:
        print("1 Edit contact \n2 B Back")
        action_str = input("Choose action: ").lower()

        if action_str == "1":
            self.show_emerg_country_menu()
        elif action_str == "2":
            self.show_emergency_cont_form()
        elif action_str == "b":
            return
            
    def show_emergency_cont_form(self):
        """This prints the edit form for an emergency contact"""

        #ÞARF AÐ FINNA LANDIÐ MEÐ ÞVÍ AÐ SÆKJA LISTA AF CONTACTS Í LL-LAYER
        #CONTACTS ERU GEYMDIR Í DICT MEÐ LAND SEM KEY, FINN NAFN SEM 
        #ER SAMA NAFN OG VALUE 
        print("*"*self.LENGTH_STAR)
        print("EDIT CONTACT \n")
        name = input("Name: ")
        phone = input("Phone: ")
        #ÉG HLÝT AÐ FÁ INN DICT HÉR ÚR LL-LAYER. ÉG ÞARF ÞÁ AÐ BREYTA HENNI EFTIR ÞVÍ HVAÐ NOTANDINN GERÐI
        #nafniðádict[land] = [name, phone]
        print("S save \nB Back")
        action_str = input("Choose action: ").lower()
        
        #if action_str == "s":
            #sendi dict í listann af dict contacts í LL-layer
        if action_str == "b": #Á AÐ VERA ELIF HÉR
            return