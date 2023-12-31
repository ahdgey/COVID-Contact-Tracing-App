#Alexza Jean R. Catanoy
#BSCPE 1-4
#COVID Contact Tracing App

import csv
import tkinter.messagebox as messagebox

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
        self.entries = []
        with open("Add_Entry.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                
                # Check if the row has at least one element before accessing it
                if len(row) > 0 and row[0] == name:
                        self.entries.append(row)

        #Save the search results to Search_Entry.csv
        if self.entries:
            self.save_search_entries()

        return self.entries
    
    def save_search_entries(self):
        with open("Search_Entry.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            
            for entry in self.entries:
                writer.writerow(entry) 
    
    #Create a list to store the selected values from the radio button sets 
    def get_radio_button_values(self):
        selected_values = []

        for var in self.radiobutton.vars:
            selected_value = var.get()
            selected_values.append(selected_value)

        return selected_value
