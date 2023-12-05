class Appointment:
    # write your appointment class here!!!

    APPT_TYPE_DESCS = ("Available", "Mens Cut", "Ladies Cut", "Mens Colouring", "Ladies Colouring")
    APPT_TYPE_PRICES = (0, 50, 80, 50, 120)
    
    # constructor for the Appointment class
    def __init__(self, day_of_week, start_time_hour):
        self.__day_of_week = day_of_week
        self.__start_time_hour = start_time_hour
        # getter and setters for the attributes of an Appointment object

    def get_client_name(self):
        return self.__client_name

    def set_client_name(self, client_name):
        self.__client_name = client_name

    def get_client_phone(self):
         return self.__client_phone   # ssc
    
    def set_client_phone(self, client_phone):
        self.__client_phone = client_phone

    def get_appt_type(self):
        return self._appt_type
    
    def set_appt_type(self, appt_type):
        self._appt_type = appt_type

    def get_day_of_week(self):
        pass

    def get_start_time_hour(self):
        pass
    
    def get_end_time_hour(self):
        pass

    def schedule(self, client_name, client_phone, appt_type):
        pass

    def cancel(self):
        pass

    def get_appt_type_desc(self):
        pass
    
    def format_record(self):
        pass
    
    def __str__(self):
        return ''