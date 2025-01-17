from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

YELLOW = "#f7f5dd"
GREEN = "#E7EAB5"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email)==0 or len(password) == 0:
        messagebox.showinfo(title="ERROR", message="OOps,Please make sure you haven't left any of "
                                                      "the field empty")

    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
            if data == None or data == '':
                print('I got a null or empty string value for data in a file')
            else:
                pass
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PASSWORD GENERATOR")
window.config(padx=20, pady=50)



#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entry
website_entry = Entry(width=39)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry()
email_entry.grid(column=1, row=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

#Button
password_button = Button(text="Generate Password", bg=GREEN, command=generate_password)
password_button.grid(column=2, row=3)
password_button.config(highlightthickness=0)

search_button = Button(text="Search", command=search_password)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", width=36, command=save, bg=GREEN)
add_button.grid(column=1, row=4, columnspan=2)
add_button.config(highlightthickness=0)

window.mainloop()