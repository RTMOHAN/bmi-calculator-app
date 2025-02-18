import tkinter as tk

class BMIApp:
    def __init__(self, master):
        self.master = master
        master.title("BMI Calculator")

        self.label_weight = tk.Label(master, text="Weight (kg):")
        self.label_weight.pack()

        self.entry_weight = tk.Entry(master)
        self.entry_weight.pack()

        self.label_height = tk.Label(master, text="Height (m):")
        self.label_height.pack()

        self.entry_height = tk.Entry(master)
        self.entry_height.pack()

        self.calculate_button = tk.Button(master, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def calculate_bmi(self):
        weight = float(self.entry_weight.get())
        height = float(self.entry_height.get())
        bmi = weight / (height ** 2)
        category = self.categorize_bmi(bmi)
        self.result_label.config(text=f"BMI: {bmi:.2f} - Category: {category}")

    def categorize_bmi(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"