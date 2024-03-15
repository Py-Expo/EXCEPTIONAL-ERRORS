import calendar
import tkinter as tk
from tkinter import ttk

def show_calendar():
    year = int(year_entry.get())
    month = int(month_combobox.get())

    # Clear existing calendar and events
    for widget in calendar_frame.winfo_children():
        widget.destroy()

    for widget in events_frame.winfo_children():
        widget.destroy()

    # Generate the calendar for the selected month and year
    cal_content = calendar.monthcalendar(year, month)

    # Display the calendar in the GUI
    for week_num, week in enumerate(cal_content, start=1):
        for day_num, day in enumerate(week):
            if day != 0:
                day_button = ttk.Button(calendar_frame, text=str(day), command=lambda d=day: add_event(year, month, d))
                day_button.grid(row=week_num, column=day_num, padx=5, pady=5)

def add_event(year, month, day):
    event_window = tk.Toplevel(root)
    event_window.title("Add Event")

    # Label and entry for event name
    ttk.Label(event_window, text="Event Name:").grid(row=0, column=0, padx=5, pady=5)
    event_name_entry = ttk.Entry(event_window)
    event_name_entry.grid(row=0, column=1, padx=5, pady=5)

    # Label and entry for event time
    ttk.Label(event_window, text="Event Time:").grid(row=1, column=0, padx=5, pady=5)
    event_time_entry = ttk.Entry(event_window)
    event_time_entry.grid(row=1, column=1, padx=5, pady=5)

    # Function to add event to calendar
    def save_event():
        event_name = event_name_entry.get()
        event_time = event_time_entry.get()

        # Create or append events for the selected day
        event_date = f"{year}-{month:02d}-{day:02d}"
        if event_date not in events:
            events[event_date] = []
        events[event_date].append((event_name, event_time))

        # Display the event below the calendar
        display_events()

        event_window.destroy()

    # Button to save event
    save_button = ttk.Button(event_window, text="Save", command=save_event)
    save_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

def display_events():
    # Clear existing events
    for widget in events_frame.winfo_children():
        widget.destroy()

    # Display events for the selected month
    for day, event_list in events.items():
        day_label = ttk.Label(events_frame, text=f"Day {day}:")
        day_label.pack()
        for event_name, event_time in event_list:
            event_label = ttk.Label(events_frame, text=f"{event_name} ({event_time})", foreground="blue")
            event_label.pack()

# Create tkinter window
root = tk.Tk()
root.title("Event Calendar")

# Year entry
year_label = ttk.Label(root, text="Year:")
year_label.grid(row=0, column=0, padx=5, pady=5)
year_entry = ttk.Entry(root)
year_entry.grid(row=0, column=1, padx=5, pady=5)

# Month combobox
month_label = ttk.Label(root, text="Month:")
month_label.grid(row=0, column=2, padx=5, pady=5)
month_combobox = ttk.Combobox(root, values=list(range(1, 13)))
month_combobox.grid(row=0, column=3, padx=5, pady=5)
month_combobox.set(1)  # Default to January

# Button to display calendar
show_button = ttk.Button(root, text="Show Calendar", command=show_calendar)
show_button.grid(row=0, column=4, padx=5, pady=5)

# Frame to hold calendar
calendar_frame = ttk.Frame(root)
calendar_frame.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

# Frame to hold events
events_frame = ttk.Frame(root)
events_frame.grid(row=2, column=0, columnspan=5, padx=10, pady=10)

# Label for events
events_label = ttk.Label(events_frame, text="Events for the selected month:")
events_label.pack()

# Dictionary to store events
events = {}

root.mainloop()
