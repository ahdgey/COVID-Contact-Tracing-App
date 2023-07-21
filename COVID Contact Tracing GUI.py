import tkinter as tk
from tkinter import messagebox
from COVID_Contact_Tracing_App import ContactTacingApp

class ContactTracingAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("COVID Contact Tracing App")

        #Create add entry and search entry buttons plus the grid
        self.add_button = tk.Button(root, text="Add Entry", command=self.add_entry)
        self.add_button.grid(row=15, column=2, padx=15, pady=10)

        self.search_button = tk.Button(root, text="Search Entry", command=self.search_entry)
        self.search_button.grid(row=15, column=4, padx=15, pady=10)

        #Create the labels, entry, and grid fields
        #Name
        self.name_label = tk.Label(root, text="Name: ")
        self.name_label.grid(row=0, column=0, padx=15, pady=10, sticky=tk.W)

        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, pady=15, padx=10)

        #Date of Birth
        self.bday_label = tk.Label(root, text="Date of Birth: ")
        self.bday_label.grid(row=1, column=0, padx=15, pady=10, sticky=tk.W)

        self.bday_entry = tk.Entry(root)
        self.bday_entry.grid(row=1, column=1, pady=15, padx=10)

        #Gender
        self.gender_label = tk.Label(root, text="Gender: ")
        self.gender_label.grid(row=2, column=0, padx=15, pady=10, sticky=tk.W)

        self.gender_entry = tk.Entry(root)
        self.gender_entry.grid(row=2, column=1, pady=15, padx=10)

        #Phone Number
        self.phone_label = tk.Label(root, text="Phone Number: ")
        self.phone_label.grid(row=3, column=0, padx=15, pady=10, sticky=tk.W)

        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=3, column=1, pady=15, padx=10)

        #Email Address
        self.email_label = tk.Label(root, text="Email Address: ")
        self.email_label.grid(row=0, column=2, padx=15, pady=10, sticky=tk.W)

        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=0, column=3, pady=15, padx=10)

        #Address
        self.address_label = tk.Label(root, text="Address: ")
        self.address_label.grid(row=1, column=2, padx=15, pady=10, sticky=tk.W)

        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=1, column=3, pady=15, padx=10)

        #Contact Person Name
        self.name_2_label = tk.Label(root, text="Contact Person Name: ")
        self.name_2_label.grid(row=2, column=2, padx=15, pady=10, sticky=tk.W)

        self.name_2_entry = tk.Entry(root)
        self.name_2_entry.grid(row=2, column=3, pady=15, padx=10)

        #Contact Person Phone Number
        self.phone_2_label = tk.Label(root, text="Contact Person Phone Number: ")
        self.phone_2_label.grid(row=3, column=2, padx=15, pady=10, sticky=tk.W)

        self.phone_2_entry = tk.Entry(root)
        self.phone_2_entry.grid(row=3, column=3, pady=15, padx=10)

        #Contact Person Email Address
        self.email_2_label = tk.Label(root, text="Contact Person Email Address: ")
        self.email_2_label.grid(row=0, column=4, padx=15, pady=10, sticky=tk.W)

        self.email_2_entry = tk.Entry(root)
        self.email_2_entry.grid(row=0, column=5, pady=15, padx=10)

        #Relationship to the contact person
        self.relationship_label = tk.Label(root, text="Relationship to the contact person: ")
        self.relationship_label.grid(row=1, column=4, padx=15, pady=10, sticky=tk.W)

        self.relationship_entry = tk.Entry(root)
        self.relationship_entry.grid(row=1, column=5, pady=15, padx=10)

        #Date today
        self.date_label = tk.Label(root, text="Date today: ")
        self.date_label.grid(row=2, column=4, padx=15, pady=10, sticky=tk.W)

        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=2, column=5, pady=15, padx=10)

        #Time
        self.time_label = tk.Label(root, text="Time right now: ")
        self.time_label.grid(row=3, column=4, padx=15, pady=10, sticky=tk.W)

        self.time_entry = tk.Entry(root)
        self.time_entry.grid(row=3, column=5, pady=15, padx=10)

        #Create a list to store the StringVar variables for the radio button sets
        self.radiobutton_vars = []

        #If vaccinated already
        self.radiobutton_1_var = tk.StringVar()
        self.radiobutton_1_var.set(None)
        self.radiobutton_vars.append(self.radiobutton_1_var)

        self.vaccine_label = tk.Label(root, text="Do you have a COVID-19 vaccine? ")
        self.vaccine_label.grid(row=5, column=2, padx=15, pady=10, sticky=tk.W)

        self.vaccine_radiobutton_1 = tk.Radiobutton(root, text="Yes", variable=self.radiobutton_1_var, value="Yes")
        self.vaccine_radiobutton_1.grid(row=6, column=2)

        self.vaccine_radiobutton_2 = tk.Radiobutton(root, text="No", variable=self.radiobutton_1_var, value="No")
        self.vaccine_radiobutton_2.grid(row=7, column=2)

#If experiencing any symptoms
#If had been recently exposed to a suspected or confirmed case
#If had been engaged with somebody who maybe exhibiting symptoms
#If have been undergone a Covid-19 test
#If have been undergone a self quarantine
#Create an instance of the contact tracing app
#Method to handle add_entry 
#Get all the input values from the entry fields and radiobutton variables
#Method to show the message box 
#Method to handle search_entry 
#From the ContactTracingApp class, call all the search_entry method and message box
#Clear all entry fields and reset the radio buttons
#Create the main window