from db import insert_data
import customtkinter as ctk
from email_validator import validate_email


def register_screen(self):
    self.reg_container = ctk.CTkFrame(self, fg_color="#343eb3", corner_radius=20)
    self.reg_container.pack(pady=20, padx=60, expand=True)
    ctk.CTkLabel(self.reg_container, text="Create New Account", font=("Arial", 20, "bold"), text_color="white").pack(pady=(30, 10))
    self.email_entry = ctk.CTkEntry(self.reg_container,
                              placeholder_text="Email",
                              fg_color="#3f4ccc",
                              placeholder_text_color="white",
                              height=50,
                              width=320,
                              font=("Arial", 17, "normal"),
                              border_width=0,
                              corner_radius=15
                              )
    self.email_entry.pack(padx=40, pady=(10, 15))
    self.pass_entry = ctk.CTkEntry(self.reg_container,
                              placeholder_text="Password",
                              fg_color="#3f4ccc",
                              placeholder_text_color="white",
                              height=50,
                              width=320,
                              font=("Arial", 17, "normal"),
                              border_width=0,
                              corner_radius=15,
                              show="*")
    self.pass_entry.pack(pady=5, padx=40)
    self.pass2_entry = ctk.CTkEntry(self.reg_container,
                                   placeholder_text="Password",
                                   fg_color="#3f4ccc",
                                   placeholder_text_color="white",
                                   height=50,
                                   width=320,
                                   font=("Arial", 17, "normal"),
                                   border_width=0,
                                   corner_radius=15,
                                   show="*")
    self.pass2_entry.pack(pady=5, padx=40)
    self.reg_btn = ctk.CTkButton(self.reg_container,
                                text="Create Account",
                                width=200,
                                height=45,
                                corner_radius=10,
                                fg_color="#4649a3",
                                text_color="white",
                                font=("Arial", 14, "bold"),
                                hover_color="#3c3e7a",
                                command=lambda: handle_register(self))
    self.reg_btn.pack(pady=(30, 10))

    self.back_btn = ctk.CTkButton(self.reg_container,
                                text="Back to Login",
                                width=200,
                                height=45,
                                corner_radius=10,
                                fg_color="transparent",
                                text_color="#ffffff",
                                border_width=1,
                                border_color="#ffffff",
                                font=("Arial", 14, "bold"),
                                hover_color="#3f4ccc",
                                command=self.show_login_screen)
    self.back_btn.pack(pady=(0, 30))

def handle_register(self):
    email = self.email_entry.get()
    password = self.pass_entry.get()
    password2 = self.pass2_entry.get()
    try:
        res = validate_email(email)
        if email == "" or password == "":
            self.label.configure(text=f"Error! No empty spaces available!", text_color="#FF5C42",
                                 font=("Arial", 20, "bold"),
                                 wraplength=300)
            return
        if password != password2:
            self.label.configure(text=f"Passwords do not match!", text_color="#B51A00",
                                 font=("Arial", 20, "bold"),
                                 wraplength=300)
            return
        if insert_data(email, password):
            self.label.configure(text = f"User Registered Successfully! You can login now.", text_color="#07E81A",
                        font=("Arial", 20, "bold"),
                        wraplength=300)
        else:
            self.label.configure(text=f"Email already used.", text_color="#B51A00",
                                 font=("Arial", 20, "bold"),
                                 wraplength=300)
    except Exception as e:
        self.label.configure(text=f"{e}", text_color="#DB8D27",
                             font=("Arial", 20, "bold"),
                             wraplength=300)