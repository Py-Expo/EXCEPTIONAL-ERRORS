import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Light and Dark Mode Toggle")
        self.current_mode = tk.StringVar(value="Light")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Hello, World!", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.mode_button = tk.Button(self.master, textvariable=self.current_mode, command=self.toggle_mode)
        self.mode_button.pack()

    def toggle_mode(self):
        current_mode = self.current_mode.get()
        new_mode = "Dark" if current_mode == "Light" else "Light"
        self.current_mode.set(new_mode)

        if new_mode == "Dark":
            self.master.config(bg="black")
            self.label.config(fg="white")
            self.mode_button.config(bg="white", fg="black")
        else:
            self.master.config(bg="white")
            self.label.config(fg="black")
            self.mode_button.config(bg="black", fg="white")


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
