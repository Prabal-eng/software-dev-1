import tkinter as tk
from tkinter import ttk, messagebox
import re

class TemperatureConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("Temperature Converter")
        self.master.geometry("720x1080")
        self.master.resizable(False, False)

        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = ttk.Label(self.master, text="Advanced Temperature Converter", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Main frame
        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Input frame
        input_frame = ttk.LabelFrame(main_frame, text="Input", padding="10")
        input_frame.pack(fill=tk.X, padx=10, pady=5)

        ttk.Label(input_frame, text="Enter temperature:").grid(row=0, column=0, sticky=tk.W)
        self.entry_temp = ttk.Entry(input_frame, width=15)
        self.entry_temp.grid(row=0, column=1, padx=5)

        ttk.Label(input_frame, text="From:").grid(row=1, column=0, sticky=tk.W)
        self.combo_from = ttk.Combobox(input_frame, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", width=12)
        self.combo_from.set("Celsius")
        self.combo_from.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="To:").grid(row=2, column=0, sticky=tk.W)
        self.combo_to = ttk.Combobox(input_frame, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", width=12)
        self.combo_to.set("Fahrenheit")
        self.combo_to.grid(row=2, column=1, padx=5)

        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, padx=10, pady=10)

        convert_button = ttk.Button(button_frame, text="Convert", command=self.convert_temp)
        convert_button.pack(side=tk.LEFT, padx=5)

        clear_button = ttk.Button(button_frame, text="Clear", command=self.clear_fields)
        clear_button.pack(side=tk.LEFT, padx=5)

        # Result frame
        result_frame = ttk.LabelFrame(main_frame, text="Result", padding="10")
        result_frame.pack(fill=tk.X, padx=10, pady=5)

        self.result_var = tk.StringVar()
        result_label = ttk.Label(result_frame, textvariable=self.result_var, font=("Arial", 12))
        result_label.pack()

        # History frame
        history_frame = ttk.LabelFrame(main_frame, text="Conversion History", padding="10")
        history_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.history_text = tk.Text(history_frame, height=5, width=40, state='disabled')
        self.history_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(history_frame, orient="vertical", command=self.history_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.history_text.configure(yscrollcommand=scrollbar.set)

    def convert_temp(self):
        try:
            input_temp = float(self.entry_temp.get())
            from_unit = self.combo_from.get()
            to_unit = self.combo_to.get()

            if from_unit == to_unit:
                result = input_temp
            elif from_unit == "Celsius":
                if to_unit == "Fahrenheit":
                    result = (input_temp * 9/5) + 32
                else:  # Kelvin
                    result = input_temp + 273.15
            elif from_unit == "Fahrenheit":
                if to_unit == "Celsius":
                    result = (input_temp - 32) * 5/9
                else:  # Kelvin
                    result = (input_temp - 32) * 5/9 + 273.15
            else:  # from Kelvin
                if to_unit == "Celsius":
                    result = input_temp - 273.15
                else:  # Fahrenheit
                    result = (input_temp - 273.15) * 9/5 + 32

            self.result_var.set(f"{input_temp:.2f} {from_unit} = {result:.2f} {to_unit}")
            self.add_to_history(f"{input_temp:.2f} {from_unit} → {result:.2f} {to_unit}")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    def clear_fields(self):
        self.entry_temp.delete(0, tk.END)
        self.combo_from.set("Celsius")
        self.combo_to.set("Fahrenheit")
        self.result_var.set("")

    def add_to_history(self, conversion):
        self.history_text.configure(state='normal')
        self.history_text.insert(tk.END, conversion + "\n")
        self.history_text.see(tk.END)
        self.history_text.configure(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverter(root)
    root.mainloop()
