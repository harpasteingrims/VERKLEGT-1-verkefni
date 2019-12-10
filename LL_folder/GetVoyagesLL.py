import datetime
import dateutil.parser
from models.VoyagesModel import VoyagesModel
class GetVoyagesLL():
    def __init__(self, ioapi):
        self.ioapi = ioapi
        self.voyages_list = []

    def list_all_voyages(self):
        return self.ioapi.get_all_voyages_list()

    def list_all_voyages_overview(self):
        pass

    def list_not_staffed_voyages(self):

        voyages_list = self.list_all_voyages()
        unmanned_list = []
        for voyage_ob in voyages_list:
            if voyage_ob.crew_list == []:
                unmanned_list.append(voyage_ob)
        
        return unmanned_list

    def list_all_common_voyages(self):

        voyages_list = self.list_all_voyages()
        counter = 0
        common_voyages_list = []
        for voyage_ob in voyages_list:
            destination = voyage_ob.destination
            parsed_date = dateutil.parser.parse(voyage_ob.departure_time)
            for voyage_object in voyages_list:
                parsed_date_voyage = dateutil.parser.parse(voyage_object.departure_time)
                if [voyage_object.destination, parsed_date_voyage.hour, parsed_date_voyage.minute] == [destination, parsed_date.hour, parsed_date.minute]:
                    counter += 1
            if counter > 1:
                departure_time = str(parsed_date.hour) + ":" + str(parsed_date.minute) + ":00"
                if [destination, departure_time] not in common_voyages_list:
                    common_voyages_list.append([destination, departure_time])
            counter = 0

        return common_voyages_list

    def list_unavailable_voyage_time(self, voyage_year, voyage_month, voyage_day):

        voyages_list = self.list_all_voyages()
        unavailable_voyage_time_list = []
        for voyage_ob in voyages_list:
            parsed_date = dateutil.parser.parse(voyage_ob.departure_time)
            if int(voyage_year) == parsed_date.year and int(voyage_month) == parsed_date.month and int(voyage_day) == parsed_date.day:
                time_str = str(parsed_date.hour) + ":" + str(parsed_date.minute) + ":00"
                unavailable_voyage_time_list.append(time_str)
        
        return unavailable_voyage_time_list

    def list_schedule_employee_by_date(self, employee_ob, date_from, date_to):
        voyages_list = self.list_all_voyages()
        
        all_flights_of_employee = []
        
        for voyage_ob in voyages_list:
            if employee_ob.ssn in voyage_ob.crew_list:
                all_flights_of_employee.append(voyage_ob)

        flights_on_asked_time = []
        for voyage_ob in all_flights_of_employee:
            if date_from <= voyage_ob.departure_time >= date_to:
                flights_on_asked_time.append(voyage_ob)

        
        return flights_on_asked_time

            
        
    