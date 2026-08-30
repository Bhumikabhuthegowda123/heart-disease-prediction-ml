# main.py - Application Entry Point
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from login import LoginWindow
from dashboard import DashboardWindow
from database import init_database

def main():
    """Main application loop and DB initialization."""
    # Initialize SQLite Database tables
    init_database()
    
    root = tk.Tk()
    root.title("CardioGuard ML - Heart Disease Prediction System")
    root.geometry("1100x700")
    root.configure(bg="#0f172a")
    
    # Launch with Login Dialog
    def on_login_success(user_id, role, username):
        login_frame.destroy()
        dashboard = DashboardWindow(root, user_id, role, username)
        dashboard.pack(fill="both", expand=True)

    login_frame = LoginWindow(root, on_login_success)
    login_frame.pack(fill="both", expand=True)
    
    root.mainloop()

if __name__ == "__main__":
    main()
