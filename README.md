# BMI Calculator Application

This is a simple BMI Calculator application built using Python and Tkinter. The application allows users to input their weight and height, calculates their Body Mass Index (BMI), and categorizes the result.

## Features

- Input collection for weight and height in both metric and imperial units.
- BMI calculation based on user input.
- Categorization of BMI values (Underweight, Normal weight, Overweight, Obesity).
- User-friendly graphical interface built with Tkinter.

## Project Structure

```
bmi-calculator-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── calculator.py    # Contains BMI calculation logic
│   ├── ui.py            # Defines the user interface
│   └── utils.py         # Utility functions for input validation
├── requirements.txt     # Lists project dependencies
└── README.md            # Project documentation
```

## Requirements

To run this application, you need to have Python installed on your machine. The following libraries are required:

- Tkinter (usually included with Python installations)

You can install any additional dependencies listed in `requirements.txt` using pip:

```
pip install -r requirements.txt
```

## Running the Application

To run the BMI Calculator application, navigate to the `src` directory and execute the `main.py` file:

```
python main.py
```

## Usage

1. Enter your weight and height in the provided fields.
2. Click the "Calculate BMI" button.
3. The application will display your BMI value and its category.

## License

This project is open-source and available for modification and distribution.