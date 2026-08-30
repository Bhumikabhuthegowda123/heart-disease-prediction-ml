# login.py - User Authentication Module
import tkinter as tk
from tkinter import ttk, messagebox
from database import verify_user

class LoginWindow(ttk.Frame):
    def __init__(self, parent, success_callback):
        super().__init__(parent)
        self.success_callback = success_callback
        self.create_widgets()

    def create_widgets(self):
        lbl_title = ttk.Label(
            self,
            text="CardioGuard ML Security Portal",
            font=("Helvetica", 16, "bold")
        )
        lbl_title.pack(pady=20)

        # Username Field
        ttk.Label(self, text="Username:").pack()
        self.ent_user = ttk.Entry(self)
        self.ent_user.pack(pady=5)

        # Password Field
        ttk.Label(self, text="Password:").pack()
        self.ent_pwd = ttk.Entry(self, show="*")
        self.ent_pwd.pack(pady=5)

        # Role Selector
        ttk.Label(self, text="Role:").pack()
        self.cmb_role = ttk.Combobox(
            self,
            values=["Admin", "Doctor"]
        )
        self.cmb_role.current(0)
        self.cmb_role.pack(pady=5)

        # Buttons
        btn_login = ttk.Button(
            self,
            text="Login",
            command=self.handle_login
        )
        btn_login.pack(pady=10)

    def handle_login(self):
        user = self.ent_user.get()
        pwd = self.ent_pwd.get()
        role = self.cmb_role.get()

        valid, user_id = verify_user(user, pwd, role)

        if valid:
            messagebox.showinfo(
                "Success",
                f"Welcome Dr. {user}!"
            )
            self.success_callback(user_id, role, user)
        else:
            messagebox.showerror(
                "Auth Error",
                "Invalid Username or Password credentials."
          )
