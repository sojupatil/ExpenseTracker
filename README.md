# 💰 Simple Expense Tracker (CLI-based)

A beginner-friendly Python script to track your daily expenses in a plain text file. It stores each entry with the amount, category, description, and date of purchase in a readable format.

---

## 📌 Description

This project allows users to record their spending directly from the command line. It checks if a file named `main.txt` exists:

- If the file exists, it asks the user for:
  - Amount of the item
  - Category of the expense
  - Description of the item
  - Date of the purchase  
  Then it saves this data in a human-readable sentence format in `main.txt`.

- If the file doesn't exist, it creates it on the first run and prompts the user to rerun the script.

---

## 🛠️ Features

- Append new expense entries to `main.txt`
- Human-readable log (one entry per line)
- Automatically creates the file if it doesn’t exist
- CLI-based interaction (simple and fast)

---

## 📂 Sample Entry Format

