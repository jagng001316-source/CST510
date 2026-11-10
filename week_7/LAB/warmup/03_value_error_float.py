# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

raw_line = "srv-01,used=unknown,total=100"
hostname_part, rest = raw_line.split(",", 1)

for piece in rest.split(","):
    key, value = piece.split("=")
    try:
        numeric_value = float(value)
    except ValueError:
        print(f"Could not convert value '{value}' for key '{key}' to float.")
        print(key, value)
    else:
        print(key, numeric_value)
