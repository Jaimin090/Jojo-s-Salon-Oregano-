import appointment as ap
from apptMgmt import *
# import for path functions
from os import path
# import for system funciton
from os import system

# Function to load scheduled appointments from a file
def load_scheduled_appointments(appt_cal: list[ap.Appointment]):
    # Ask user for the appointment file name
    file_name = input("Enter appointment filename: ")
    # check if file exists, prompt re-entry if not found
    while not path.isfile(file_name): #path.isfile usage reference: https://stackoverfl  ow.com/questions/17658856/why-am-i-getting-a-filenotfounderror
        file_name = input("File not found. Re-enter appointment filename: ")

    # open file in read mode
    file = open(file_name, "r")

    num_imported = 0

    # Read each line in the file
    for line in file:
        line = line.rstrip() #remove whitespace
        line_items = line.split(",") #name, phone, type, day, hour
        # Find appointment by day and hour
        appt = find_appointment_by_time(appt_cal, line_items[3], int(line_items[4]))
        if appt is not None:
            # Schedule the appointment according to file
            appt.schedule(line_items[0], line_items[1], int(line_items[2]))
            num_imported += 1   # Increase the imported appointment counter

    print(f"{num_imported} previously scheduled appointments have been loaded")
    file.close()        # Close the file


# Method to save the scheduled appointments to file
def save_scheduled_appointments(appt_cal: list[ap.Appointment]):
    # get file name
    file_name = input("Enter appointment filename: ")
    overwrite = False       # check if file overwrite is needed
    # check if file exists and prompt user for overwrite choice
    while path.isfile(file_name) and not overwrite:
        overwrite_choice = input("File already exists. Do you want to overwrite it (Y/N)? ").lower()
        if overwrite_choice == "y":
            overwrite = True
        elif overwrite_choice == "n":
            overwrite = False
        file_name = input("Enter appointment filename: ")
        overwrite = False

    # open file in write mode
    file = open(file_name, "w")

    num_exported = 0

    # Write scheduled appointments to file
    for appt in appt_cal:
        if appt.get_appt_type() != 0:       # check if slot is booked
            file.write(f"{appt.format_record()}\n")     # write details in given format
            num_exported += 1       # increase the exported appointment counter

    print(f"{num_exported} scheduled appointments have been successfully saved")
    file.close()        # close the file