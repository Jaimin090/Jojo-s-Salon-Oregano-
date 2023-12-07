import appointment as ap
from apptMgmt import *
# import for path functions
from os import path
from os import system

def load_scheduled_appointments(appt_cal: list[ap.Appointment]):
    file_name = input("Enter appointment filename: ")
    while not path.isfile(file_name): #path.isfile usage reference: https://stackoverflow.com/questions/17658856/why-am-i-getting-a-filenotfounderror
        file_name = input("File not found. Re-enter appointment filename: ")

    file = open(file_name, "r")

    num_imported = 0

    for line in file:
        line = line.rstrip()
        line_items = line.split(",") #name, phone, type, day, hour
        appt = find_appointment_by_time(appt_cal, line_items[3], int(line_items[4]))
        if appt is not None:
            appt.schedule(line_items[0], line_items[1], int(line_items[2]))
            num_imported += 1

    print(f"{num_imported} previously scheduled appointments have been loaded")
    file.close()



def save_scheduled_appointments(appt_cal: list[ap.Appointment]):
    file_name = input("Enter appointment filename: ")
    overwrite = False
    while path.isfile(file_name) and not overwrite:
        overwrite_choice = input("File already exists. Do you want to overwrite it (Y/N)? ").lower()
        if overwrite_choice == "y":
            overwrite = True
        elif overwrite_choice == "n":
            overwrite = False
        file_name = input("Enter appointment filename: ")
        overwrite = False

    file = open(file_name, "w")

    num_exported = 0

    for appt in appt_cal:
        if appt.get_appt_type() != 0:
            file.write(f"{appt.format_record()}\n")
            num_exported += 1
    
    print(f"{num_exported} scheduled appointments have been successfully saved")
    file.close()