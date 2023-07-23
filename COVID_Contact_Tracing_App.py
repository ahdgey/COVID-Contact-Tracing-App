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

        else:
            messagebox.showinfo("Error", "Your entry has not been found.")

        return self.entries
    
    def save_search_entries(self):
        with open("Search_Entry.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(["Name:", "Date of Birth:", "Gender:", "Phone Number:", "Email Address:", "Address:", "Contact Person Name:", "Contact Person Phone Number:", "Contact Person Email Address:", 
                            "Relationship to the contact person:", "Date today:", "Time right now:", "Do you have a COVID-19 vaccine?", "Have you had any symptoms in the previous seven days?", 
                            "Have you recently been exposed to a suspected or confirmed case?", "Have you engaged with someone who may be exhibiting symptoms?", 
                            "In the previous 14 days, have you undergone a Covid-19 test?", "In the previous 14 days, have you undergone a self quarantine?"])
            
            for entry in self.entries:
                writer.writerow(entry) 
    
    #Create a list to store the selected values from the radio button sets 
    def get_radio_button_values(self):
        selected_values = []

        for var in self.radiobutton.vars:
            selected_value = var.get()
            selected_values.append(selected_value)

        return selected_value