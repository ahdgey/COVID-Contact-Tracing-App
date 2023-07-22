#Alexza Jean R. Catanoy
#BSCPE 1-4
#COVID Contact Tracing App

import csv

#Initialize ContactTracingApp class
class ContactTracingApp:
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
        with open("Add_Entry.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:

                #Check to see if the name matches, then print whether or not the entry was found
                if row[0] == name:
                    entries.append(row)
        #Save the search results to Search_Entry.csv
        self.save_search_entries(entries)

        return entries
    
    def save_search_entries(self, entries):
        with open("Search_Entry.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(entries)
    
    #Create a list to store the selected values from the radio button sets 
    def get_radio_button_values(self):
        selected_values = []

        for var in self.radiobutton.vars:
            selected_value = var.get()
            selected_values.append(selected_value)

        return selected_value