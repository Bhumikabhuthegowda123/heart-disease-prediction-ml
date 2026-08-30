# dashboard.py - Clinical Control Dashboard
import tkinter as tk
from tkinter import ttk, messagebox
from predict import PredictorModule
from report import generate_pdf_report

class DashboardWindow(ttk.Frame):
    def __init__(self, parent, user_id, role, username):
        super().__init__(parent)
        self.user_id = user_id
        self.role = role
        self.username = username
        
        lbl_welcome = ttk.Label(
            self,
            text=f"Welcome, {username} ({role})",
            font=("Helvetica", 14)
        )
        lbl_welcome.pack(pady=10)
        
        # Tabs container
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Predictor Tab
        self.predictor_tab = PredictorModule(notebook)
        notebook.add(self.predictor_tab, text="Heart Predictor")
