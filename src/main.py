# bmi-calculator-app/src/main.py

import tkinter as tk
from ui import BMIApp

def main():
    root = tk.Tk()
    root.title("BMI Calculator")
    app = BMIApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()