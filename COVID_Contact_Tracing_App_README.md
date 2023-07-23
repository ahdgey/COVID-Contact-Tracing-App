# COVID Contact Tracing App
Using Python's Tkinter library, the offered code develops a COVID contact tracing program with a graphical user interface. COVID_Contact_Tracing_App.py and COVID_Contact_Tracing_GUI.py are the two files that make up the code.

The program code for COVID_Contact_Tracing_App.py is in charge of making the app work. It establishes the ContactTracingApp class, which has methods for adding and searching entries. The add_entry method accepts as inputs the name, date of birth, gender, phone number, email address, address, relationship to the contact person, contact person's name, contact person's number, and contact person's email address, as well as six (6) questions with two possible answers: yes or no. This data is then saved to a CSV file. The Search_Entry method accepts a name as input, searches the file for matching entries, and returns the findings.

The graphical user interface (GUI) is managed by the COVID_Contact_Tracing_GUI file. It creates a window with buttons, radio buttons, labels, and input fields. Users can submit their name, date of birth, gender, phone number, email address, address, relationship to the contact person, date, time, and six (6) questions by selecting yes or no. They can also enter the name, date of birth, gender, contact person's name, number, and email address. The entered information is saved to a file called Add_Entry.csv when you click the "Add Entry" button. When the "Search Entry" button is clicked, the file is searched for matching entries, which are then shown on the screen and saved to a file called Search_Entry.csv.

## Installation
1. In order to execute the code on your computer, install Python. This link will take you to the most recent version: https://www.python.org/downloads
2. From the repository, copy the code to your clipboard.
3. Copy the code into an IDE.
4. Give the file a.py extension when saving it.
5. Run your code.
6. A message and a keyword must be entered, it will prompt you. Once your message and keyword have been entered, press Enter.
7. All uppercase letters from the encrypted text will be visible.

## Usage
1. Run the application: COVID_Contact_Tracing_GUI.py
2. The GUI window will be displayed.
3. Enter your details in the respective fields.
4. Click the "Add Entry" button to save the information to the file.
5. Click the "Search Entry" button to find existing entries based on the name.