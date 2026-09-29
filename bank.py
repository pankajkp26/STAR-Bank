import tkinter as tk
from tkinter import messagebox
import random

clients = []

current_client = None


def create_account():
    name = name_entry.get()
    deposit = deposit_entry.get()
    password = password_entry.get()

    if name == "" or deposit == "" or password == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    try:
        deposit = float(deposit)
    except ValueError:
        messagebox.showerror("Error", "Enter a valid deposit")
        return

    if deposit < 0:
        messagebox.showerror("Error", "Deposit cannot be negative")
        return

    account_number = random.randint(100000, 999999)

    customer = {
        "name": name,
        "deposit": deposit,
        "password": password,
        "account_number": account_number
    }

    clients.append(customer)

    messagebox.showinfo(
        "Account Created",
        "Account created successfully!\n\n"
        "Your account number is: " + str(account_number)
    )

    name_entry.delete(0, tk.END)
    deposit_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


def login():
    global current_client

    name = login_name.get()
    account = login_account.get()
    password = login_password.get()

    if name == "" or account == "" or password == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    try:
        account = int(account)
    except ValueError:
        messagebox.showerror("Error", "Account number must be a number")
        return

    for customer in clients:
        if (customer["name"] == name and
                customer["account_number"] == account and
                customer["password"] == password):

            current_client = customer
            account_window()
            return

    messagebox.showerror("Error", "Wrong login details")


def account_window():
    window = tk.Toplevel(root)
    window.title("My Account")
    window.geometry("400x400")

    tk.Label(
        window,
        text="Welcome " + current_client["name"],
        font=("Arial", 18)
    ).pack(pady=20)

    tk.Label(
        window,
        text="Account Number: "
        + str(current_client["account_number"])
    ).pack(pady=5)

    balance = tk.Label(
        window,
        text="Balance: ₹" + str(current_client["deposit"]),
        font=("Arial", 14)
    )
    balance.pack(pady=20)

    tk.Label(window, text="Enter Amount").pack()

    amount_entry = tk.Entry(window)
    amount_entry.pack(pady=5)

    def deposit_money():
        try:
            amount = float(amount_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Enter a valid amount")
            return

        if amount <= 0:
            messagebox.showerror("Error", "Amount must be positive")
            return

        current_client["deposit"] += amount

        balance.config(
            text="Balance: ₹" + str(current_client["deposit"])
        )

        amount_entry.delete(0, tk.END)

        messagebox.showinfo(
            "Success",
            "Money deposited successfully"
        )

    def withdraw_money():
        try:
            amount = float(amount_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Enter a valid amount")
            return

        if amount <= 0:
            messagebox.showerror("Error", "Amount must be positive")
            return

        if amount > current_client["deposit"]:
            messagebox.showerror(
                "Error",
                "Insufficient balance"
            )
            return

        current_client["deposit"] -= amount

        balance.config(
            text="Balance: ₹" + str(current_client["deposit"])
        )

        amount_entry.delete(0, tk.END)

        messagebox.showinfo(
            "Success",
            "Money withdrawn successfully"
        )

    tk.Button(
        window,
        text="Deposit",
        command=deposit_money
    ).pack(pady=5)

    tk.Button(
        window,
        text="Withdraw",
        command=withdraw_money
    ).pack(pady=5)

    tk.Button(
        window,
        text="Check Balance",
        command=lambda: messagebox.showinfo(
            "Balance",
            "Your balance is ₹"
            + str(current_client["deposit"])
        )
    ).pack(pady=5)

    tk.Button(
        window,
        text="Logout",
        command=window.destroy
    ).pack(pady=10)


root = tk.Tk()

root.title("STAR Bank")
root.geometry("500x600")


tk.Label(
    root,
    text="STAR Bank",
    font=("Arial", 24, "bold")
).pack(pady=20)


tk.Label(
    root,
    text="Create New Account",
    font=("Arial", 16, "bold")
).pack(pady=10)

tk.Label(root, text="Name").pack()

name_entry = tk.Entry(root)
name_entry.pack()


tk.Label(root, text="Initial Deposit").pack()

deposit_entry = tk.Entry(root)
deposit_entry.pack()


tk.Label(root, text="Password").pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()


tk.Button(
    root,
    text="Create Account",
    command=create_account
).pack(pady=15)


tk.Label(
    root,
    text="Login",
    font=("Arial", 16, "bold")
).pack(pady=10)

tk.Label(root, text="Name").pack()

login_name = tk.Entry(root)
login_name.pack()


tk.Label(root, text="Account Number").pack()

login_account = tk.Entry(root)
login_account.pack()


tk.Label(root, text="Password").pack()

login_password = tk.Entry(root, show="*")
login_password.pack()


tk.Button(
    root,
    text="Login",
    command=login
).pack(pady=15)


tk.Button(
    root,
    text="Exit",
    command=root.destroy
).pack(pady=10)


root.mainloop()