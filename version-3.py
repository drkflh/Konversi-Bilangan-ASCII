from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Konversi String ke ASCII dan Sistem Bilangan")
root.geometry("400x300")

# Function to convert string to ASCII
def convert_to_ascii():
    string = str_entry.get()
    ascii_list = [ord(c) for c in string]
    ascii_result = ', '.join(str(i) for i in ascii_list)
    ascii_label.config(text=ascii_result)

# Function to convert string to decimal
def convert_to_decimal():
    string = str_entry.get()
    decimal_result = int.from_bytes(string.encode(), 'big')
    decimal_label.config(text=decimal_result)

# Function to convert string to binary
def convert_to_binary():
    string = str_entry.get()
    binary_result = ' '.join(format(ord(c), '08b') for c in string)
    binary_label.config(text=binary_result)

# Function to convert string to octal
def convert_to_octal():
    string = str_entry.get()
    octal_result = ' '.join(format(ord(c), '03o') for c in string)
    octal_label.config(text=octal_result)

# Function to convert string to hexadecimal
def convert_to_hex():
    string = str_entry.get()
    hex_result = ' '.join(format(ord(c), '02X') for c in string)
    hex_label.config(text=hex_result)

# Create string input label and entry box
str_label = Label(root, text="Masukkan String:")
str_label.pack()
str_entry = Entry(root)
str_entry.pack()

# Create button to trigger conversion functions
button = ttk.Button(root, text="Konversi", command=lambda: [convert_to_ascii(), convert_to_decimal(), convert_to_binary(), convert_to_octal(), convert_to_hex()])
button.pack()

# Create labels to display results
ascii_label = Label(root, text="")
ascii_label.pack()
decimal_label = Label(root, text="")
decimal_label.pack()
binary_label = Label(root, text="")
binary_label.pack()
octal_label = Label(root, text="")
octal_label.pack()
hex_label = Label(root, text="")
hex_label.pack()

root.mainloop()
