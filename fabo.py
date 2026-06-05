
import tkinter as tk
from tkinter import messagebox

# Function to generate Fibonacci series
def fibonacci_generator(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fib_sequence = [0, 1]

    for i in range(2, n):
        next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_number)

    return fib_sequence


# Function triggered when button is clicked
def generate():
    try:
        n = int(entry.get())

        if n <= 0:
            messagebox.showerror("Error", "Please enter a number greater than 0")
            return

        result = fibonacci_generator(n)

        # Display result in text box
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, str(result))

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer")


# Create main window
window = tk.Tk()
window.title("Fibonacci Generator")
window.geometry("400x300")


# Label
label = tk.Label(window, text="Enter number of Fibonacci terms:", font=("Arial", 12))
label.pack(pady=10)


# Input field
entry = tk.Entry(window, font=("Arial", 12))
entry.pack(pady=5)


# Button
button = tk.Button(window, text="Generate", command=generate, font=("Arial", 12))
button.pack(pady=10)


# Output box
output_text = tk.Text(window, height=8, width=40)
output_text.pack(pady=10)


# Run GUI
window.mainloop()
