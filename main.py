from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT = ('calibre', 10, 'normal')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """Generate password"""
    characters = {
        'letters': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],

        'numbers': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        'symbols': ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    }

    gen_pass = ''
    for i in range(15):
        pass_key = random.choice(list(characters.keys()))
        pass_value = characters[pass_key][random.randint(0, len(pass_key) - 1)]
        gen_pass += pass_value

    password_entry.insert(0, gen_pass)
    pyperclip.copy(gen_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    """Saves Password"""
    website_name = website_entry.get()
    username_ = username_entry.get()
    password_ = password_entry.get()

    new_data = {
        website_name: {
            'username': username_,
            'password': password_,
        }
    }
    if len(password_) == 0 or len(website_name) == 0:
        messagebox.showerror(title='Opps', message='Ensure all fields are not empty')
    else:
        is_okay = messagebox.askokcancel(title=website_name, message=f'YOUR DETAILS:\n Username: {username_}\n '
                                                                     f'Password: {password_}')
        if is_okay:
            try:
                with open('pm.json', mode='r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open('pm.json', mode='w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open('pm.json', mode='w') as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')


def search():
    """Searches the json file for user entry"""
    name = website_entry.get()
    with open('pm.json', mode='r') as file:
        data = json.load(file)

    try:
        user_name = data[name]['username']
        pass_word = data[name]['password']
    except KeyError:
        messagebox.showerror(title='Opps', message='Website detail does not exist')
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='Data not found')
    else:
        messagebox.showinfo(title=name, message=f'Username: {user_name}\n'
                                                f'Password: {pass_word}')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title('Password Manager')
window.config(padx=50, pady=50, )

canvas = Canvas(height=200, width=200, highlightthickness=0)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0, )

# Website row
website = Label(text='Website:')
website.grid(column=0, row=1, sticky='w')
website.focus()
website_entry = Entry(width=35, )
website_entry.grid(column=1, row=1, )

# Search button
search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2, )

# Email/Username row
username = Label(text='Email/Username:', )
username.grid(column=0, row=2, sticky='w')
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2)
username_entry.insert(0, 'am0du@gmail.com')

# Password row
password = Label(text='Password:', )
password.grid(column=0, row=3, sticky='w')
password_entry = Entry(width=35, )
password_entry.grid(column=1, row=3)

# Generate password row
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

# Add button
add_button = Button(width=30, text='Add', command=add)
add_button.grid(column=1, row=4, )

window.mainloop()
