#
# appt_manager - Application program that:
#     Creates an empty calendar for the week.
#     Allows the user to add/remove appointments
#     Prints out the calendar for a specific day
# All appointments are between 9 AM - 4 PM daily. All appointments are one hour long.
# This appointment Manager is for a six day week (Monday-Saturday).
#
# Author: Zi Liang, Jaimin Chavda, Aman Sharma
# Version/Date: 2023-12-04
#
import appointment as ap
# import file functions
from apptFile import *
# import management functions
from apptMgmt import *
# import reporting functions
from apptReports import *
MENU = """Jojo's Hair Salon Appointment Manager
=====================================
 1) Schedule an appointment
 2) Find appointment by name
 3) Print calendar for a specific day
 4) Cancel an appointment
 9) Exit the system"""
DAYS_OF_WEEK = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
FIRST_HOUR_OF_DAY = 9
LAST_HOUR_OF_DAY = 16

def main():
    appt_calendar = []
    selection = 0
    print("Starting the Appointment Manager System")

    # Create an empty appointment calendar for the week
    create_weekly_calendar(appt_calendar)
    print("Weekly calendar created")

    load_flag = input("Would you like to load previously scheduled appointments from a file (Y/N)? ")
    while not load_flag.lower() in "yn":
        load_flag = input("Would you like to load previously scheduled appointments from a file (Y/N)? ")

    if load_flag.lower() == "y":
        load_scheduled_appointments(appt_calendar)

    # Display the menu and input user selections (loop)
    selection = print_menu()
    while selection != 9:

        # Evaluate user selection:
        #  1. Schedule an appointment
        if selection == 1:
            print("\n** Schedule an appointment **")
            schedule_appointment(appt_calendar)
        #  2. Find appointment by name
        elif selection == 2:
            print("\n** Find appointment by name **")
            name = input("Enter Client Name: ")
            print(f"Appointments for {name}\n")
            show_appointments_by_name(appt_calendar, name)
        #  3. Show all appointments for a specific day
        elif selection == 3:
            print("\n** Print calendar for a specific day **")
            day = input("What day: ")
            print(f"Appointments for {day.title()}\n")
            show_appointments_by_day(appt_calendar, day)
        #  4. Cancel an appointment
        elif selection == 4:
            print("\n** Cancel an appointment **")
            day = input("What day: ")
            hour = int(input("Enter start hour: "))
            appt = find_appointment_by_time(appt_calendar, day.title(), int(hour))
            if appt is not None:
                if appt.get_appt_type() != 0:
                    print(f"Appointment: {appt.get_day_of_week()} {appt.get_start_time_hour()}:00 - {appt.get_end_time_hour()}:00 for {appt.get_client_name()} has been cancelled!")
                    appt.cancel()
                else:
                    print("That time slot isn't booked and doesn't need to be cancelled")
            else:
                print("Sorry that time slot is not in the weekly calendar!")
        #  ?. Invalid selection
        elif selection != 9:
            print("\nInvalid option")

        # Pause, then get user selection for the next loop iteration
        selection = print_menu()

    print("\n** Exit the system **")
    save_flag = input("Would you like to save all scheduled appointments to a file (Y/N)? ")
    # save the appointments if the user requests it, call save_scheduled_appointments
    while not save_flag.lower() in "yn":
        save_flag = input("Would you like to save all scheduled appointments to a file (Y/N)? ")

    if save_flag.lower() == "y":
        save_scheduled_appointments(appt_calendar)

    print("Good Bye!")

def create_weekly_calendar(appt_cal):
    # clear out existing list
    appt_cal.clear()
    for index in range(len(DAYS_OF_WEEK)):
        # Add a calendar appointment entry for every hour of the day that the salon is open
        for time in range(FIRST_HOUR_OF_DAY, LAST_HOUR_OF_DAY+1):
            appt = ap.Appointment(DAYS_OF_WEEK[index], time)
            appt_cal.append(appt)


def print_menu():
    print("\n")
    
    print(MENU)
    opt = int(input("Enter your selection: "))
    return opt

if __name__ == "__main__":
    main()