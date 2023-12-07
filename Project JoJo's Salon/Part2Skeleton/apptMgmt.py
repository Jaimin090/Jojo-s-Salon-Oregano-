# Import appointment module
import appointment as ap

# method to schedule appointment
def schedule_appointment (appt_calendar):
    day = input("What day: ").title()       # Input day for appointment
    hour = int(input("Enter start hour (24 hour clock): "))         # input starting hour for appointment
    appt = find_appointment_by_time(appt_calendar, day, hour)       # find specific appointment slot

    # Return false if appointment cannot be scheduled due to slot being non-existent
    if appt == None:
        print("Sorry that time slot is not in the weekly calendar!")
        return False 
    
    # Return false as appointment cannot be booked due to slot being already booked
    if appt.get_appt_type_desc() != "Available":
        print("Sorry that time slot is booked already!")
        return False

    # input client details, appt type
    name = input("Client Name: ")
    phone = input("Client Phone: ")

    print("Appointment types\n1: Mens Cut $50, 2: Ladies Cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120")
    type = int(input("Type of Appointment: "))
    
    # validate appointment type and return false if its invalid
    if not type in (1, 2, 3, 4):
        print("Sorry that is not a valid appointment type!")
        return False 

    # Schedule appointment with details provided
    appt.schedule(name, phone, type)

    print(f"OK, {name}'s appointment is scheduled!")
    return True

def find_appointment_by_time(appt_cal: list[ap.Appointment], day_of_week, start_hour):
    # find_appointment_by_time - given a list of appointments and a specific day and time,
    # this function finds and returns the corresponding appointment. If no appointment
    # is found, returns None
    for appt in appt_cal:
        if appt.get_day_of_week() == day_of_week and appt.get_start_time_hour() == start_hour:
            return appt
        
    return None # return none if no appointment is found
