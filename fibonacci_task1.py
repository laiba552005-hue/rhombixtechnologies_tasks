# Task 1: Fibonacci Generator
# Description: This program generates a sequence of Fibonacci numbers
# based on the user's input.

def generate_fibonacci(n):
    # Initializing the sequence with the first two Fibonacci numbers
    fib_sequence = [0, 1]

    # Using a loop to calculate the next numbers until the list reaches length 'n'
    # Logic: Next Number = Sum of the last two numbers
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    # Returning only the required number of terms
    return fib_sequence[:n]


# Main execution block
try:
    # Taking input from the user and converting it to an integer
    count = int(input("How many numbers of the Fibonacci series do you want? "))

    # Checking if the user entered a positive integer
    if count <= 0:
        print("Error: Please enter a positive number greater than zero.")
    else:
        # Calling the function and storing the result
        result = generate_fibonacci(count)

        # Displaying the final Fibonacci sequence
        print(f"\nFibonacci Series (first {count} terms):")
        print(result)

except ValueError:
    # Handling cases where the user enters non-numeric data (like text)
    print("Invalid input! Please enter a valid numerical value.")