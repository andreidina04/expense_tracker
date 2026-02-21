import customtkinter as ctk
from db import transaction_history, get_connection, get_total_spends, get_total_income, delete_from_db, filter_data
from login import handle_login

def dashboard_items(self):

    total_spends = get_total_spends(self.current_user_id)
    total_income = get_total_income(self.current_user_id)
    self.sidebar = ctk.CTkFrame(self, width=300, corner_radius=20, fg_color="#1C1F4A")
    self.sidebar.pack(side="left", fill="y")

    self.logo_label = ctk.CTkLabel(self.sidebar, text="Expense Tracker", font=("Arial", 25, "bold"), text_color="white")
    self.logo_label.pack(pady=20, padx=20)

    self.btn_dash = ctk.CTkButton(self.sidebar, text="Dashboard", fg_color="transparent", text_color="white", font=("Arial", 17, "bold"), command=self.dashboard, hover_color="#27308A")
    self.btn_dash.pack(padx=10, pady=10)

    self.btn_add_money = ctk.CTkButton(self.sidebar, text="Add Money", fg_color="transparent", text_color="white", font=("Arial", 17, "bold"), command=self.add_money_window, hover_color="#27308A")
    self.btn_add_money.pack(padx=10, pady=10)

    self.btn_add = ctk.CTkButton(self.sidebar, text="Add Transaction", fg_color="transparent", text_color="white", font=("Arial", 17, "bold"), command=self.add_transaction_window, hover_color="#27308A")
    self.btn_add.pack(padx=10, pady=10)

    self.btn_logout = ctk.CTkButton(self.sidebar, text="Logout", fg_color="transparent", text_color="red", font=("Arial", 17, "bold"), command = self.show_login_screen, hover_color="#27308A")
    self.btn_logout.pack(padx=10, pady=10)

    self.user_label = ctk.CTkLabel(self.sidebar, text=f"email: {self.current_user_email}", fg_color="transparent", font=("Arial", 12, "bold"))
    self.user_label.pack(padx=0, pady=0)
    self.user_label = ctk.CTkLabel(self.sidebar, text=f"id: {self.current_user_id}", fg_color="transparent", font=("Arial", 12, "bold"))
    self.user_label.pack(padx=0, pady=0)

    self.main_view = ctk.CTkFrame(self, corner_radius=20, fg_color="#1C1F4A")
    self.main_view.pack(side="right", fill="both", expand = True, padx=20, pady=20)

    self.balance_card = ctk.CTkFrame(self.main_view, height=200, width=500, corner_radius=10, fg_color="#00A36C")
    self.balance_card.pack(pady=20,padx=20, fill="x")

    self.balance_title = ctk.CTkLabel(self.balance_card, text="Total Balance", text_color="white", fg_color="transparent", font=("Arial", 14, "bold"))
    self.balance_title.pack(pady=10, padx=20)

    self.balance_amount = ctk.CTkLabel(self.balance_card, text=f"{total_income - total_spends}$", text_color="white", fg_color="transparent", font=("Arial", 16, "bold"))
    self.balance_amount.pack(pady=10, padx=0)

    self.spends_card = ctk.CTkFrame(self.main_view, height=100, width=500, corner_radius=10, fg_color="red")
    self.spends_card.pack(pady=20, padx=20, fill="x")

    self.spends_title = ctk.CTkLabel(self.spends_card, text="Total Spends", text_color="white", fg_color="transparent", font=("Arial", 14, "bold"))
    self.spends_title.pack(pady=10, padx=20)

    self.spends_amount = ctk.CTkLabel(self.spends_card, text=f"{total_spends}$", text_color="white", fg_color="transparent", font=("Arial", 16, "bold"))
    self.spends_amount.pack(pady=10, padx=0)

    self.history = ctk.CTkLabel(self.main_view, text="Transactions History", text_color="white", font=("Arial", 16, "bold"))
    self.history.pack(pady=(10,0), padx=20, anchor="w")

    self.filter = ctk.CTkOptionMenu(self.main_view, width=250, height=35,
                                          values=["All", "Gym", "Food", "Rent", "Transport", "Entertainment", "Shopping"],
                                          fg_color="#27308A", button_color="#27308A", dropdown_fg_color="#27308A", text_color="white", dropdown_text_color="white", dropdown_hover_color="#1C1F4A", command=lambda category:update_list(self, category))
    self.filter.pack(pady=5)

    self.history.frame = ctk.CTkScrollableFrame(self.main_view, fg_color="transparent", height=300)
    self.history.frame.pack(fill="both", expand=True, padx=20, pady=10)

    update_transaction(self)
def update_transaction(self):
    transaction_date = transaction_history(self.current_user_id)

    for child in self.history.frame.winfo_children():
        child.destroy()

    for t in transaction_date:
        row = ctk.CTkFrame(self.history.frame, fg_color="#27308A", height=50)
        row.pack(pady=5, padx=10, fill="x")

        ctg_label = ctk.CTkLabel(row, text=f"{t['category']}", font=("Arial", 12, "bold"), text_color="white")
        ctg_label.pack(side="left", padx=15)

        db_type = str(t['type']).lower().strip()

        color = "#07DE16" if db_type == "income" else "#DE0707"
        sign = "+" if db_type == "income" else "-"

        details = ctk.CTkLabel(row, text=f"{sign}{t['amount']} $", font=("Arial", 12, "bold"), text_color=color)
        details.pack(side="right", padx=10)

        t_id = t['id']
        delete_btn = ctk.CTkButton(row, text="✕", font=("Arial", 12, "bold"), width=25,
        height=25,
        fg_color="transparent",
        hover_color="#DE0707",
        text_color="white",
        command=lambda i= t_id:self.delete_trans(i))
        delete_btn.pack(side="right", padx=10)
        date_format = t['date'].strftime("%Y-%m-%d")
        date = ctk.CTkLabel(row, text=f"{date_format}", font=("Arial", 12, "italic"), text_color="#B5B5B5")
        date.pack(padx=10, pady=10)

def update_list(self, category):
    filtered_list = filter_data(self.current_user_id, category)

    for child in self.history.frame.winfo_children():
        child.destroy()

    for t in filtered_list:
        row = ctk.CTkFrame(self.history.frame, fg_color="#27308A", height=50)
        row.pack(pady=5, padx=10, fill="x")

        ctg_label = ctk.CTkLabel(row, text=f"{t['category']}", font=("Arial", 12, "bold"), text_color="white")
        ctg_label.pack(side="left", padx=15)

        db_type = str(t['type']).lower().strip()
        color = "#07DE16" if db_type == "income" else "#DE0707"
        sign = "+" if db_type == "income" else "-"

        details = ctk.CTkLabel(row, text=f"{sign}{t['amount']} $", font=("Arial", 12, "bold"), text_color=color)
        details.pack(side="right", padx=10)

        t_id = t['id']
        delete_btn = ctk.CTkButton(row, text="✕", font=("Arial", 12, "bold"), width=25,
            height=25, fg_color="transparent", hover_color="#DE0707", text_color="white",
            command=lambda i=t_id: self.delete_trans(i))
        delete_btn.pack(side="right", padx=10)

        date_format = t['date'].strftime("%Y-%m-%d")
        date = ctk.CTkLabel(row, text=f"{date_format}", font=("Arial", 12, "italic"), text_color="#B5B5B5")
        date.pack(padx=10, pady=10)

