import customtkinter as ctk
from db import login_data

def login_screen(self):
    self.login_container = ctk.CTkFrame(self, fg_color="#343eb3", corner_radius=20)
    self.login_container.pack(pady=20, padx=60, expand=True)
    ctk.CTkLabel(self.login_container, text="Welcome Back", font=("Arial", 20, "bold"), text_color="white").pack(pady=(30, 10))
    self.email_entry = ctk.CTkEntry(self.login_container,
                              placeholder_text="Email",
                              fg_color="#3f4ccc",
                              placeholder_text_color="white",
                              height=50,
                              width=320,
                              font=("Arial", 17, "normal"),
                              border_width=0,
                              corner_radius=15
                              )
    self.email_entry.pack(pady=(10, 15), padx=40)
    self.pw_entry = ctk.CTkEntry(self.login_container,
                              placeholder_text="Password",
                              fg_color="#3f4ccc",
                              placeholder_text_color="white",
                              height=50,
                              width=320,
                              font=("Arial", 17, "normal"),
                              border_width=0,
                              corner_radius=15,
                              show="*"
                              )
    self.pw_entry.pack(pady=5, padx=40)

    self.button_login = ctk.CTkButton(self.login_container,
                                width=200,
                                height=45,
                                corner_radius=10,
                                fg_color="#ffffff",
                                text_color="#22264d",
                                font=("Arial", 14, "bold"),
                                hover_color="#c2c7f0",
                                text="Login",
                                command=lambda: handle_login(self))
    self.button_login.pack(pady=(30, 10))

    self.button_register = ctk.CTkButton(self.login_container,
                                width=200,
                                height=45,
                                corner_radius=10,
                                fg_color="transparent",
                                text_color="#ffffff",
                                border_width=1,
                                border_color="#ffffff",
                                font=("Arial", 14, "bold"),
                                hover_color="#3f4ccc",
                                text="Register",
                                command=self.show_register_screen)
    self.button_register.pack(pady=(0, 30))


def handle_login(self):
    email = self.email_entry.get()
    password = self.pw_entry.get()

    if email == "" or password == "":
        self.label.configure(text=f"Error! No empty spaces available!", text_color="#FF5C42",
                                 font=("Arial", 20, "bold"),
                                 wraplength=300)
        return

    user_id = login_data(email, password)

    if user_id:
        self.current_user_id = user_id
        self.current_user_email = email
        self.label.configure(text="Login successful!", text_color="#07E81A")

        self.after(1000, self.dashboard)
    else:
        self.label.configure(text="Incorrect credentials.", text_color="#B51A00")