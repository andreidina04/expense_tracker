from doctest import register_optionflag
import customtkinter as ctk
from customtkinter import CTkEntry
from login import login_screen
from db import get_connection, add_transactions, adding_money_db
from register import register_screen
from dashboard import dashboard_items
from db import delete_from_db
class ExpenseTracker(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.current_user_id = None
        self.title("Expense Tracker - v1.0")
        self.configure(fg_color="#27308A")
        self.geometry("1000x700")
        self.grid_columnconfigure(0, weight=1)
        self.label = ctk.CTkLabel(self, text="Expense Tracker", fg_color="transparent", justify="center", font=("Arial", 25, "bold"), text_color="white")
        self.label.pack(pady=20, anchor="center")
        login_screen(self)

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.label = ctk.CTkLabel(self, text="Expense Tracker", fg_color="transparent", justify="center", font=("Arial", 25, "bold"), text_color="white")
        self.label.pack(pady=20, anchor="center")

    def show_register_screen(self):
        self.clear_screen()
        register_screen(self)

    def show_login_screen(self):
        self.clear_screen()
        login_screen(self)

    def dashboard(self):
        self.clear_screen()
        dashboard_items(self)

    def add_money_window(self):
        self.add_window = ctk.CTkToplevel(self)
        self.add_window.title("Add Money")
        self.add_window.geometry("400x450")
        self.add_window.configure(fg_color="#1C1F4A")
        self.add_window.attributes("-topmost", True)
        self.add_window.grab_set()

        ctk.CTkLabel(self.add_window, text="Income Details", font=("Arial", 20, "bold"), text_color="#00A36C").pack(
            pady=20)

        ctk.CTkLabel(self.add_window, text="Amount ($):", font=("Arial", 12, "bold")).pack(pady=(10, 0))
        self.entry_amount = ctk.CTkEntry(self.add_window, width=250, height=35, placeholder_text="Enter Amount",
                                         border_color="#00A36C")
        self.entry_amount.pack(pady=5)

        ctk.CTkLabel(self.add_window, text="Category:", font=("Arial", 12, "bold")).pack(pady=(10, 0))
        self.category = ctk.CTkOptionMenu(self.add_window, width=250, height=35,
                                          values=["Salary", "Investment", "Gift", "Bonus", "Other"], fg_color="#27308A", button_color="#27308A", dropdown_fg_color="#27308A", text_color="white", dropdown_text_color="white", dropdown_hover_color="#1C1F4A")
        self.category.pack(pady=5)

        btn_save = ctk.CTkButton(self.add_window, text="Add Money", width=250, height=40, corner_radius=8,
                                 font=("Arial", 13, "bold"), fg_color="#00A36C", hover_color="#008356",
                                 command=self.adding_money)
        btn_save.pack(pady=30)

    def add_transaction_window(self):
        self.add_twindow = ctk.CTkToplevel(self)
        self.add_twindow.title("Add Transactions")
        self.add_twindow.geometry("400x450")
        self.add_twindow.configure(fg_color="#1C1F4A")
        self.add_twindow.attributes("-topmost", True)
        self.add_twindow.grab_set()

        ctk.CTkLabel(self.add_twindow, text="Expense Details", font=("Arial", 20, "bold"), text_color="#FF5C42").pack(
            pady=20)

        ctk.CTkLabel(self.add_twindow, text="Amount ($):", font=("Arial", 12, "bold")).pack(pady=(10, 0))
        self.entry_amount = ctk.CTkEntry(self.add_twindow, width=250, height=35, placeholder_text="Enter Amount",
                                         border_color="#FF5C42")
        self.entry_amount.pack(pady=5)

        ctk.CTkLabel(self.add_twindow, text="Category:", font=("Arial", 12, "bold")).pack(pady=(10, 0))
        self.category = ctk.CTkOptionMenu(self.add_twindow, width=250, height=35,
                                          values=["Gym", "Food", "Rent", "Transport", "Entertainment", "Shopping"],
                                          fg_color="#27308A", button_color="#27308A", dropdown_fg_color="#27308A", text_color="white", dropdown_text_color="white", dropdown_hover_color="#1C1F4A")
        self.category.pack(pady=5)

        btn_save = ctk.CTkButton(self.add_twindow, text="Add Transaction", width=250, height=40, corner_radius=8,
                                 font=("Arial", 13, "bold"), fg_color="black", hover_color="#333333",
                                 command=self.execute_save)
        btn_save.pack(pady=30)

    def execute_save(self):
        try:
            amt = float(self.entry_amount.get())
            ctg = self.category.get()

            if add_transactions(self.current_user_id, amt, ctg):
                ctk.CTkLabel(self.add_twindow, text="Transaction Added!").pack(pady=10)
                self.dashboard()
            else:
                self.error_label = ctk.CTkLabel(self.add_twindow, text="Error in DB!", text_color="red")
                self.error_label.pack(pady=5)
        except ValueError:
            ctk.CTkLabel(self.add_twindow, text="Please insert a number!").pack(pady=10)

    def adding_money(self):
        try:
            amt = float(self.entry_amount.get())
            ctg = self.category.get()
            if adding_money_db(self.current_user_id, amt, ctg):
                ctk.CTkLabel(self.add_window, text="Money Added!").pack(pady=10)
                self.dashboard()
            else:
                self.error_label = ctk.CTkLabel(self.add_window, text="Error in DB!", text_color="red")
                self.error_label.pack(pady=5)
        except ValueError:
            ctk.CTkLabel(self.add_window, text="Please insert a number!").pack(pady=10)

    def delete_trans(self, transaction_id):
        if delete_from_db(transaction_id):
            self.dashboard()
        else:
            print("Error!")


if __name__ == "__main__":
    app = ExpenseTracker()
    app.mainloop()