# report.py - ReportLab PDF Export Generator
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf_report(filename, patient_data, risk_label, confidence):
    """Generates an official clinical PDF report."""
    c = canvas.Canvas(filename, pagesize=letter)

    c.setFont("Helvetica-Bold", 18)
    c.drawString(100, 750, "CardioGuard ML - Heart Disease Diagnostic Report")

    c.setFont("Helvetica", 12)
    c.drawString(50, 700, f"Patient ID: {patient_data['id']}")
    c.drawString(50, 680, f"Patient Name: {patient_data['name']}")
    c.drawString(50, 660, f"Age/Sex: {patient_data['age']} Yrs / {patient_data['sex']}")

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 600, f"Diagnostic Risk: {risk_label}")
    c.drawString(50, 580, f"Confidence Score: {confidence}%")

    c.save()
