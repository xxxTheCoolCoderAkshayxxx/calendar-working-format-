import tkinter as tk
import calendar

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Akshay's Calendar")
        self.root.geometry("400x300")
        self.root.config(background="light grey")
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(
            self.root, text="Calendar", bg="red", font=("Arial", 24), fg="white"
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Year Input Label
        year_label = tk.Label(
            self.root, text="Year: ", bg="light grey", font=("Arial", 12)
        )
        year_label.grid(row=1, column=0, padx=5, pady=10)
        self.year_entry = tk.Entry(self.root, bg="white", font=("Arial", 12))
        self.year_entry.grid(row=1, column=1, padx=5, pady=10)

        # Show Calendar Button
        show_btn = tk.Button(
            self.root, text="Show Calendar", bg="green", fg="white",
            font=("Arial", 12), command=self.show_calendar
        )
        show_btn.grid(row=2, column=0, columnspan=3, pady=10)

        # Exit Button
        exit_btn = tk.Button(
            self.root, text="Exit", bg="grey", fg="white", font=("Arial", 12), command=self.root.quit
        )
        exit_btn.grid(row=3, column=0, columnspan=3, pady=10)

    def show_calendar(self):
        # Create a new window for displaying the calendar
        calendar_window = tk.Toplevel(self.root)
        calendar_window.title("Yearly Calendar")
        calendar_window.geometry("600x500")
        year = int(self.year_entry.get())
        calendar_content = calendar.TextCalendar().formatyear(year)

        # Display the calendar content in a Text widget with a Scrollbar
        calendar_text = tk.Text(calendar_window, font=("Courier", 10), wrap="none")
        calendar_text.insert(tk.END, calendar_content)
        calendar_text.config(state="disabled")  # Make it read-only
        calendar_text.pack(expand=True, fill="both", padx=10, pady=10)

        # Add a vertical Scrollbar
        scrollbar = tk.Scrollbar(calendar_window, command=calendar_text.yview)
        scrollbar.pack(side="right", fill="y")
        calendar_text.config(yscrollcommand=scrollbar.set)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()