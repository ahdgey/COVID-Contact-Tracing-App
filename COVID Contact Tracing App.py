#Alexza Jean R. Catanoy
#BSCPE 1-4
#COVID Contact Tracing App

import csv

#Initialize ContactTracingApp class
class ContactTacingApp:
    def __init__(self):
        pass

    #Write all the information that has been collected to the CSV file
    def add_entry(self, name, bday, gender, phone, email, address, name_2, phone_2, email_2, relationship, date, time, vaccine_1, symptoms_1, exposed_1, engaged_1, test_1, quarantine_1):
        with open("Add_Entry.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([name,bday, gender, phone, email, address, name_2, phone_2, email_2, relationship, date, time, vaccine_1, symptoms_1, exposed_1, engaged_1, test_1, quarantine_1])

    #From the CSV file, read all the entries and then search for the name 
    def search_entry(self, name):
        entries = []
        with open("Search_Entry.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:

                #Check to see if the name matches, then print whether or not the entry was found
                if row[0] == name:
                    entries.append(row)
        return entries
    
#Create a list to store the selected values from the radio button sets 