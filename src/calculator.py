class BMI_Calculator:
    def calculate_bmi(self, weight, height, unit='metric'):
        if unit == 'imperial':
            bmi = (weight / (height ** 2)) * 703
        else:
            bmi = weight / (height ** 2)
        return round(bmi, 2)

    def categorize_bmi(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"