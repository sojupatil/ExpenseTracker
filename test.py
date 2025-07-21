import customtkinter as ctk
from tkinter import messagebox
import os

# --- App Setup ---
ctk.set_appearance_mode("dark")  # Options: "light", "dark", "system"
ctk.set_default_color_theme("blue")  # Options: blue, green, dark-blue, etc.

app = ctk.CTk()
app.title("💰 Expense Tracker")
app.geometry("400x450")
app.resizable(False, False)

# --- Title ---
title_label = ctk.CTkLabel(app, text="Expense Tracker", font=("Segoe UI", 24, "bold"))
title_label.pack(pady=20)

# --- Input Fields ---
def create_input(label_text):
    label = ctk.CTkLabel(app, text=label_text, anchor="w", font=("Segoe UI", 14))
    label.pack(padx=20, anchor="w")
    entry = ctk.CTkEntry(app, width=300, height=35, font=("Segoe UI", 14))
    entry.pack(pady=5)
    return entry

amount_entry = create_input("Amount (₹):")
category_entry = create_input("Category:")
desc_entry = create_input("Description:")
date_entry = create_input("Date (YYYY-MM-DD):")

# --- Save Logic ---
def save_expense():
    amount = amount_entry.get()
    category = category_entry.get()
    description = desc_entry.get()
    date = date_entry.get()

    if not amount or not category or not description or not date:
        messagebox.showerror("Missing Data", "Please fill in all fields.")
        return

    try:
        amount = int(amount)
    except ValueError:
        messagebox.showerror("Invalid Input", "Amount must be a number.")
        return

    full_des = f"Bought '{description}' in category '{category}' for ₹{amount} on {date}\n"

    if not os.path.exists("main.txt"):
        with open("main.txt", "x") as f:
            pass  # Create the file

    with open("main.txt", "a") as f:
        f.write(full_des)

    messagebox.showinfo("Saved", "Expense saved successfully.")

    # Clear entries
    for entry in [amount_entry, category_entry, desc_entry, date_entry]:
        entry.delete(0, "end")

# --- Save Button ---
save_button = ctk.CTkButton(app, text="💾 Save Expense", command=save_expense, width=200, height=40, font=("Segoe UI", 14, "bold"))
save_button.pack(pady=30)

# --- Run App ---
app.mainloop()
