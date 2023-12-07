class Appointment:
    # write your appointment class here!!!

    APPT_TYPE_DESCS = ("Available", "Mens Cut", "Ladies Cut", "Mens Colouring", "Ladies Colouring")
    APPT_TYPE_PRICES = (0, 50, 80, 50, 120)
    
    # constructor for the Appointment class
    def __init__(self, day_of_week, start_time_hour):
        self.__name = ""        #initializing empty string for client name
        self.__phone = ""       #intializing empty string for client phone
        self.__type = 0         #intializing integer 0 for appointment type
        self.__day = day_of_week    # Day of the week when the appointment is scheduled
        self.__hour = start_time_hour   # Hour when the appointment starts

    # Methods to get clients name, phone, and appointment
    def get_client_name(self):
        return self.__name

    def set_client_name(self, client_name):
        self.__name = client_name

    def get_client_phone(self):
        return self.__phone
    
    def set_client_phone(self, client_phone):
        self.__phone = client_phone

    def get_appt_type(self):
        return self.__type
    
    def set_appt_type(self, appt_type):
        self.__type = appt_type

    # Methods to get the appointment day and time
    def get_day_of_week(self):
        return self.__day

    def get_start_time_hour(self):
        return self.__hour
    
    def get_end_time_hour(self):
        return self.__hour + 1

    # Methods to schedule and cancel the appointment
    def schedule(self, client_name, client_phone, appt_type):
        self.set_client_name(client_name)
        self.set_client_phone(client_phone)
        self.set_appt_type(appt_type)

    def cancel(self):
        self.set_client_name("")
        self.set_client_phone("")
        self.set_appt_type(0)

    # Method to get the appointment type description
    def get_appt_type_desc(self):
        return Appointment.APPT_TYPE_DESCS[self.__type]
    
    # Method to format the appointment record as string
    def format_record(self):
        return f"{self.__name},{self.__phone},{self.__type},{self.__day},{self.__hour:02d}"
    
    # Method to format the appointment details as a string
    def __str__(self):
        return f"{self.__name:<20}{self.__phone:<15}{self.__day:<10}{self.__hour:02d}:00  -  {self.get_end_time_hour():02d}:00     {self.get_appt_type_desc()}"