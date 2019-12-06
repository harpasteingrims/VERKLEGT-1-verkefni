class GetIAAD():
    def __init__(self, ioapi):
        self.ioapi = ioapi

    def list_available_emp_by_date(self, user_input_date):
        employee_list = self.ioapi.get_list_of_all_employees()
        voyage_list = self.list_voyages_status_by_date(self, user_input_date)

        for employee in employee_list:
            available_emps_for_selected_day = []
            #if employee not in (hvernig á ég að athuga allt staff á öllum ferðunum í listanum af objectum?)
                available_emps_for_selected_day.append(employee)
        return available_emps_for_selected_day
        pass

    def list_unavailable_emp_by_date(self, user_input_date):
        employee_list = self.ioapi.get_list_of_all_employees()
        voyage_list = list_voyages_status_by_date(self, user_input_date)

        for employee in employee_list:
            available_emps_for_selected_day = []
            #if employee in (hvernig á ég að athuga allt staff á öllum ferðunum í listanum af objectum?)
                available_emps_for_selected_day.append(employee)
        return available_emps_for_selected_day
        pass

    def list_airplane_status_by_date(self, user_input_date):
        airplane_list = self.ioapi.get_airplane_list
        voyage_list = list_voyages_status_by_date(self, user_input_date)
        for airplane in airplane_list:
            available_planes_for_selected_day = []
            #if employee in (hvernig á ég að athuga allt staff á öllum ferðunum í listanum af objectum?)
                available_planes_for_selected_day.append(airplane)
        return available_planes_for_selected_day
        pass

        #Sennilega best að kalla bara á neðsta listann hérna fyrir og samræma employees við þann voyage lista

        pass #Líka pæling hérna hvar er best að geyma þessar upplýsingar og hvernig er best að ná í þær og vinna úr þeim

    def list_voyages_status_by_date(self, user_input_date):
        """Returns a list of voyages on that day sorted by complete, arrived, in air and not started"""
        voyage_list = self.ioapi.get_all_voyages_list
        for voyage in voyage_list:
            voyages_for selected_day = []
            if 
        #Þurfum að finna aðferð til þess að sortera þennan lista af voyages þessa dags eftir complete, arrived, in air og not started

    def list_of_all_voyages_for_selected_day(self, user_input_date):
        """Returns an unsorted list of voyages on that day that the other functions in this class wil be using. The outcome of this function will never appear in the interface"""
        voyage_list = self.ioapi.get_all_voyages_list()
        return voyage_list
