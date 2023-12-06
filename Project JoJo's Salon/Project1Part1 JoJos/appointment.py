class Appointment:
    # write your appointment class here!!!

    APPT_TYPE_DESCS = ("Available", "Mens Cut", "Ladies Cut", "Mens Colouring", "Ladies Colouring")
    APPT_TYPE_PRICES = (0, 50, 80, 50, 120)
    
    # constructor for the Appointment class
    def __init__(self, day_of_week, start_time_hour):
        self.__day = day_of_week
        self.__hour = start_time_hour

    # getter and setters for the attributes of an Appointment object

    def get_client_name(self):
        return self.__nameclient

    def set_client_name(self, client_name):
        self.__nameclient = client_name

    def get_client_phone(self):
        return self.__phoneclient  
    
    def set_client_phone(self, client_phone):
        self.__phoneclient = client_phone

    def get_appt_type(self):
        return self.__type
    
    def set_appt_type(self, appt_type):
        self.__type = appt_type

    def get_day_of_week(self):
        return self.__day

    def get_start_time_hour(self):
        return self.__hour
    
    def get_end_time_hour(self):
        return self.__hour + 1
        
    def schedule(self, client_name, client_phone, appt_type):
        self.set_client_name(client_name)
        self.set_client_phone(client_phone)
        self.set_appt_type(appt_type)

    def cancel(self):
        self.set_client_name("")
        self.set_client_phone("")
        self.set_appt_type(0)

    def get_appt_type_desc(self):
        return Appointment.APPT_TYPE_DESCS[self.__type]
    
    def format_record(self):
        return f"{self.__name},{self.__phone},{self.__type},{self.__day},{self.__hour:02d}"
    
    def __str__(self):
        return f"{self.__name:<20}{self.__phone:<15}{self.__day:<10}{self.__hour:02d}:00  -  {self.get_end_time_hour():02d}:00     {self.get_appt_type_desc()}"