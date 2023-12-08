import tkinter as tk
from math import factorial, sqrt

def calculate_factorial():
    try:
        input_value = int(entry.get())
        result = factorial(input_value)
        result_label.config(text=f"Factorial: {result}")
    except ValueError:
        result_label.config(text="Invalid input! Please enter a valid integer.")

def calculate_square():
    try:
        input_value = float(entry.get())
        result = input_value ** 2
        result_label.config(text=f"Square: {result}")
    except ValueError:
        result_label.config(text="Invalid input! Please enter a valid number.")

def calculate_cube():
    try:
        input_value = float(entry.get())
        result = input_value ** 3
        result_label.config(text=f"Cube: {result}")
    except ValueError:
        result_label.config(text="Invalid input! Please enter a valid number.")

def check_prime():
    try:
        input_value = int(entry.get())
        if input_value > 1:
            for i in range(2, int(sqrt(input_value)) + 1):
                if input_value % i == 0:
                    result_label.config(text=f"{input_value} is not a prime number.")
                    break
            else:
                result_label.config(text=f"{input_value} is a prime number.")
        else:
            result_label.config(text=f"{input_value} is not a prime number.")
    except ValueError:
        result_label.config(text="Invalid input! Please enter a valid integer.")

app = tk.Tk()
app.title("Input and Output Operations")

window_width = 400
window_height = 300
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

x_position = int((screen_width - window_width) / 2)
y_position = int((screen_height - window_height) / 2)

app.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

entry = tk.Entry(app)
entry.pack(pady=10)

factorial_button = tk.Button(app, text="Factorial", command=calculate_factorial)
factorial_button.pack(pady=5)

square_button = tk.Button(app, text="Square", command=calculate_square)
square_button.pack(pady=5)

cube_button = tk.Button(app, text="Cube", command=calculate_cube)
cube_button.pack(pady=5)

check_prime_button = tk.Button(app, text="Check Prime", command=check_prime)
check_prime_button.pack(pady=5)

result_label = tk.Label(app, text="Result:")
result_label.pack(pady=10)

app.mainloop()