# BROKEN ON PURPOSE: This code will raise a FileNotFoundError if "records.txt" does not exist.
# Run it, read the last line, then fix it.

try:
    with open("records.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: 'records.txt' not found.")
