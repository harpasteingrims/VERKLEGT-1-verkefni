
class DestinationUI():
    Length_Star = 20
    def __init__(self):
        pass
    
    def show_destination_menu(self):
        """ This prints out the menu for destinations """
        print("*"*self.Length_Star)
        print("DESTINATIONS\n")
        print("1 Print overview of destinations \n2 Create a new destination \n3 Get emergency contact ")
        print("B back\n")
        action = input("Choose action: ") 

        if action == "1":
            DestinationUI.show_destination_overview()
        elif action == "2":
            DestinationUI.show_create_des_form()
        elif action == "3":
            DestinationUI.show_emerg_country_menu()

    def show_destination_overview(self):
        """ This prints out all the destination """
        print("*"*self.Length_Star)
        PRINT("OVERVIEW OF DESTINATIONS\n")
        #print(destinations)
        #HÉR ÞARF ÉG AÐ SÆKJA SKRÁ 

        print("B back\n")
        action = input("Choose action: ") 
        if action == "b" or action == "B":
            DestinationUI.show_destination_menu()

    def show_create_des_form(self):
        """ This prints the create destination form"""
        print("*"*self.Length_Star)
        print("CREATE A NEW DESTINATION\n")
        country = input("Enter country: ")
        airport = input("Enter airport: ")
        flight_duration = input("Enter flight duration from Iceland: ")
        distance = input("Enter distance from Iceland: ")
        contact = input("Enter name of contact: ")
        contact_phone = input("Enter emergency contact")

        new_dest = {}
        new_dest[country] = [airport, flight_duration, distance, contact, contact_phone]

        action = input("Choose action: ") 
        #if action == "s" or action == "S":
            #from UI-layer import FALL SEM VINNUR MEÐ ÞETTA
        if action == "b" or "B": #Á AÐ VERA ELIF HÉR 
            DestinationUI.show_destination_menu()

    def show_emerg_country_menu(self):
        """ This prints out the emergency contact menu """
        print("*"*self.Length_Star)
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
        action = input("Choose action: ")
        
        if action == "b" or action == "B":
            DestinationUI.show_destination_menu()

    def show_emergency_contact(self):
        """ This prints out the emergency contact for a specific country """
        print("*"*self.Length_Star)
        print("EMERGENCY CONTACT OF", country,"\n")
        #ÞARF AÐ FINNA LANDIÐ MEÐ ÞVÍ AÐ SÆKJA LISTA AF CONTACTS Í LL-LAYER
        #CONTACTS ERU GEYMDIR Í DICT MEÐ LAND SEM KEY, FINN NAFN SEM 
        #ER SAMA NAFN OG VALUE 
        # info_of_contact = # Calls the class that holds the information of contact and prints it
        # Name:
        # Phone:
        print("1 Edit contact \n2 B Back")
        action = input("Choose action: ")

        if action == "1":
            DestinationUI.show_emerg_country_menu()
        elif action == "2":
            DestinationUI.show_emergency_cont_form()

    def show_emergency_cont_form(self):
        """ This prints out the emergency contact form """
        #ÞARF AÐ FINNA LANDIÐ MEÐ ÞVÍ AÐ SÆKJA LISTA AF CONTACTS Í LL-LAYER
        #CONTACTS ERU GEYMDIR Í DICT MEÐ LAND SEM KEY, FINN NAFN SEM 
        #ER SAMA NAFN OG VALUE 
        print("*"*self.Length_Star)
        print("EDIT CONTACT \n")
        name = input("Name: ")
        phone = input("Phone: ")
        #ÉG HLÝT AÐ FÁ INN DICT HÉR ÚR LL-LAYER. ÉG ÞARF ÞÁ AÐ BREYTA HENNI EFTIR ÞVÍ HVAÐ NOTANDINN GERÐI
        #nafniðádict[land] = [name, phone]
        print("S save \nB Back")
        action = input("Choose action: ")
        
        #if action == "s" or "S":
            #sendi dict í listann af dict contacts í LL-layer
        if action == "b" or "B": #Á AÐ VERA ELIF HÉR
            DestinationUI.show_emergency_contact()





