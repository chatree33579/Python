import numpy as np

try:
    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))

    print("Enter the entries in a single line (separated by space): ")

    # User input of entries in a
    # single line separated by space
    entries = list(map(int, input().split()))

    # Check if the number of entries is equal to R * C
    if len(entries) != R * C:
        raise ValueError("Number of entries does not match the size of the matrix.")

    # For printing the matrix
    matrix = np.array(entries).reshape(R, C)
    print(matrix)

except ValueError as e:
    print(f"Error: {e}. Please enter valid input.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
