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
#Gender
#Phone Number
#Email Address
#Address
#Contact Person Name
#Contact Person Phone Number
#Contact Person Email Address
#Relationship to the contact person
#Date today
#Time
#Create a list to store the StringVar variables for the radio button sets
#If vaccinated already
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