import appointment as ap
def show_appointments_by_name(appt_cal: list[ap.Appointment], client_name):
    found_appts = []
    for appt in appt_cal:
        if appt.get_client_name().lower().startswith(client_name.lower()):
            found_appts.append(appt)

    print("{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name",
        "Phone", "Day", "Start", "End", "Type"))
    print("-" * 85)
    
    if len(found_appts) == 0:
        print("No appointments found.")
        return False
    
    for appt in found_appts:
        print(appt)

    return True

def show_appointments_by_day(appt_cal: list[ap.Appointment], day_of_week):
    # show_appointments_by_day - prints a report of all appointments for a specific day of the week
    found_appts = []
    for appt in appt_cal:
        if appt.get_day_of_week().lower() == day_of_week.lower():
            found_appts.append(appt)

    print("{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name",
        "Phone", "Day", "Start", "End", "Type"))
    print("-" * 85)
    
    for appt in found_appts:
        print(appt)

    return True