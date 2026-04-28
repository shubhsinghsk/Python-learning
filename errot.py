# Function to safely perform division and handle exceptions
def safe_divide(a, b):
    try:
        # Attempt division
        div = a / b
        print(div)  # Print the result
    except ZeroDivisionError:
        # Handle division by zero
        print("Zero division is not supported")
    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred: {e}")

# Example call
safe_divide(5, 0)