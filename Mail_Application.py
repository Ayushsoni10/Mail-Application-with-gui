import smtplib
from tkinter import Tk, Label, Entry, Text, Button, END

class EmailClient:
    def __init__(self, window):
        self.window = window
        window.title("Email Client")

        # Define labels
        Label(window, text="From:").grid(row=0)
        Label(window, text="Password:").grid(row=1)
        Label(window, text="To:").grid(row=2)
        Label(window, text="Subject:").grid(row=3)
        Label(window, text="Message:").grid(row=4)

        # Define entries
        self.from_entry = Entry(window)
        self.from_entry.grid(row=0, column=1)

        self.pass_entry = Entry(window, show="*")
        self.pass_entry.grid(row=1, column=1)

        self.to_entry = Entry(window)
        self.to_entry.grid(row=2, column=1)

        self.subject_entry = Entry(window)
        self.subject_entry.grid(row=3, column=1)

        self.message_entry = Text(window)
        self.message_entry.grid(row=4, column=1)

        # Define button
        Button(window, text="Send", command=self.send_email).grid(row=5, column=1)

    def send_email(self):
        # Get the email details
        from_address = self.from_entry.get()
        password = self.pass_entry.get()
        to_address = self.to_entry.get()
        subject = self.subject_entry.get()
        message = self.message_entry.get("1.0", END)

        # Create the email
        email = f"Subject: {subject}\n\n{message}"

        # Send the email
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_address, password)
        server.sendmail(from_address, to_address, email)
        server.quit()

        # Clear the entries
        self.from_entry.delete(0, END)
        self.pass_entry.delete(0, END)
        self.to_entry.delete(0, END)
        self.subject_entry.delete(0, END)
        self.message_entry.delete("1.0", END)

window = Tk()
EmailClient(window)
window.mainloop()
