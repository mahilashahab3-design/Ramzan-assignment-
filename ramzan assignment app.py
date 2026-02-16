import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime, timedelta

class CountdownApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("500x300")
        self.root.configure(bg="#1e1e2f")

        self.target_date = None

        # Title Label
        self.title_label = tk.Label(
            root,
            text="Countdown Timer",
            font=("Helvetica", 24, "bold"),
            fg="white",
            bg="#1e1e2f"
        )
        self.title_label.pack(pady=10)

        # Countdown Display Frame
        self.frame = tk.Frame(root, bg="#1e1e2f")
        self.frame.pack(pady=20)

        self.days_label = self.create_time_label("Days")
        self.hours_label = self.create_time_label("Hours")
        self.minutes_label = self.create_time_label("Minutes")
        self.seconds_label = self.create_time_label("Seconds")

        # Button to set date
        self.set_button = tk.Button(
            root,
            text="Set Target Date",
            command=self.set_date,
            font=("Helvetica", 12),
            bg="#4CAF50",
            fg="white",
            padx=10,
            pady=5
        )
        self.set_button.pack(pady=10)

    def create_time_label(self, text):
        frame = tk.Frame(self.frame, bg="#2b2b45", padx=15, pady=10)
        frame.pack(side="left", padx=10)

        value_label = tk.Label(
            frame,
            text="00",
            font=("Helvetica", 20, "bold"),
            fg="white",
            bg="#2b2b45"
        )
        value_label.pack()

        text_label = tk.Label(
            frame,
            text=text,
            font=("Helvetica", 12),
            fg="white",
            bg="#2b2b45"
        )
        text_label.pack()

        return value_label

    def set_date(self):
        date_str = simpledialog.askstring(
            "Input Date",
            "Enter target date and time (YYYY-MM-DD HH:MM:SS):"
        )
        try:
            self.target_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
            self.update_countdown()
        except:
            messagebox.showerror("Invalid Format", "Please use format: YYYY-MM-DD HH:MM:SS")

    def update_countdown(self):
        if self.target_date:
            now = datetime.now()
            remaining = self.target_date - now

            if remaining.total_seconds() > 0:
                days = remaining.days
                hours, remainder = divmod(remaining.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)

                self.days_label.config(text=f"{days:02}")
                self.hours_label.config(text=f"{hours:02}")
                self.minutes_label.config(text=f"{minutes:02}")
                self.seconds_label.config(text=f"{seconds:02}")

                self.root.after(1000, self.update_countdown)
            else:
                messagebox.showinfo("Time's up!", "Countdown Finished!")
                self.days_label.config(text="00")
                self.hours_label.config(text="00")
                self.minutes_label.config(text="00")
                self.seconds_label.config(text="00")

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()