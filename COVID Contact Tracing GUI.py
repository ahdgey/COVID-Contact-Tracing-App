import tkinter as tk
from tkinter import messagebox
from COVID_Contact_Tracing_App import ContactTracingApp

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
        self.radiobutton_2_var = tk.StringVar()  
        self.radiobutton_2_var.set(None)
        self.radiobutton_vars.append(self.radiobutton_2_var)

        self.symptoms_label = tk.Label(root, text="Have you had any symptoms in the previous seven days?")
        self.symptoms_label.grid(row=5, column=4, padx=15, pady=10, sticky=tk.W)
        
        self.symptoms_radiobutton_1 = tk.Radiobutton(root, text="Yes", variable=self.radiobutton_2_var, value="Yes")
        self.symptoms_radiobutton_1.grid(row=6, column=4)

        self.symptoms_radiobutton_2 = tk.Radiobutton(root, text="No", variable=self.radiobutton_2_var, value="No")
        self.symptoms_radiobutton_2.grid(row=7, column=4)

        #If had been recently exposed to a suspected or confirmed case
        self.radiobutton_3_var = tk.StringVar()
        self.radiobutton_3_var.set(None)
        self.radiobutton_vars.append(self.radiobutton_3_var)

        self.exposed_label = tk.Label(root, text="Have you recently been exposed to a suspected or confirmed case?")
        self.exposed_label.grid(row=8, column=2, padx=15, pady=10, sticky=tk.W)
        
        self.exposed_radiobutton_1 = tk.Radiobutton(root, text="Yes", variable=self.radiobutton_3_var, value="Yes")
        self.exposed_radiobutton_1.grid(row=9, column=2)

        self.exposed_radiobutton_2 = tk.Radiobutton(root, text="No", variable=self.radiobutton_3_var, value="No")
        self.exposed_radiobutton_2.grid(row=10, column=2)

        #If had been engaged with somebody who maybe exhibiting symptoms
        self.radiobutton_4_var = tk.StringVar()
        self.radiobutton_4_var.set(None) 
        self.radiobutton_vars.append(self.radiobutton_4_var)
    
        self.enggaged_label = tk.Label(root, text="Have you engaged with someone who may be exhibiting symptoms?")
        self.enggaged_label.grid(row=8, column=4, padx=15, pady=10, sticky=tk.W)
        
        self.enggaged_radiobutton_1 = tk.Radiobutton(root, text="Yes", variable=self.radiobutton_4_var, value="Yes")
        self.enggaged_radiobutton_1.grid(row=9, column=4)

        self.enggaged_radiobutton_2 = tk.Radiobutton(root, text="No", variable=self.radiobutton_4_var, value="No")
        self.enggaged_radiobutton_2.grid(row=10, column=4)

        #If have been undergone a Covid-19 test
        self.radiobutton_5_var = tk.StringVar()
        self.radiobutton_5_var.set(None)
        self.radiobutton_vars.append(self.radiobutton_5_var)
    
        self.test_label = tk.Label(root, text="In the previous 14 days, have you undergone a Covid-19 test?")
        self.test_label.grid(row=11, column=2, padx=15, pady=10, sticky=tk.W)
        
        self.test_radiobutton_1 = tk.Radiobutton(root, text="Yes", variable=self.radiobutton_5_var, value="Yes")
        self.test_radiobutton_1.grid(row=12, column=2)

        self.test_radiobutton_2 = tk.Radiobutton(root, text="No", variable=self.radiobutton_5_var, value="No")
        self.test_radiobutton_2.grid(row=13, column=2)

        #If have been undergone a self quarantine
        self.radiobutton_6_var = tk.StringVar()
        self.radiobutton_6_var.set(None)
        self.radiobutton_vars.append(self.radiobutton_6_var)

        self.quarantine_label = tk.Label(root, text="In the previous 14 days, have you undergone a self quarantine?")
        self.quarantine_label.grid(row=11, column=4, padx=15, pady=10, sticky=tk.W)
        
        self.quarantine_radiobutton_1 = tk.Radiobutton(root, text="Yes", variable=self.radiobutton_6_var, value="Yes")
        self.quarantine_radiobutton_1.grid(row=12, column=4)

        self.quarantine_radiobutton_2 = tk.Radiobutton(root, text="No", variable=self.radiobutton_6_var, value="No")
        self.quarantine_radiobutton_2.grid(row=13, column=4)

        #Create an instance of the contact tracing app
        self.contact_tracing = ContactTracingApp()

        #Method to handle add_entry 
        def add_entry(self):

            #Get all the input values from the entry fields and radiobutton variables
            name = self.name_entry.get()
            bday = self.bday_entry.get()
            gender = self.gender_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()
            name_2 = self.name_2_entry.get()
            phone_2 = self.phone_2_entry.get()
            email_2 = self.email_2_entry.get()
            relationship = self.relationship_entry.get()
            date = self.date_entry.get()
            time = self.time_entry.get()
            vaccine_1 = self.radiobutton_1_var.get() 
            symptoms_1 = self.radiobutton_2_var.get() 
            exposed_1 = self.radiobutton_3_var.get() 
            engaged_1 = self.radiobutton_4_var.get() 
            test_1 = self.radiobutton_5_var.get() 
            quarantine_1 = self.radiobutton_6_var.get() 

            self.contact_tracing.add_entry(name, bday, gender, phone, email, address, name_2, phone_2, email_2, relationship, date, time, vaccine_1, symptoms_1, exposed_1, engaged_1, test_1, quarantine_1)

        #Method to show the message box 
        def add_entry(self):
            self.clear_entries()
            messagebox.showinfo("Confirmation", "Your entry has been submitted.")

        #Method to handle search_entry 
        def search_entry(self):
            name = self.name_entry.get()

#From the ContactTracingApp class, call all the search_entry method and message box
#Clear all entry fields and reset the radio buttons
#Create the main window