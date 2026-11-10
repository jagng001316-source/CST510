# Broken on purpose.
# The code is broken because the constructor argument is 'value', but the attribute is stored as 'amount'.
# Update the code to use the correct attribute name when accessing the value.

class Record:
    def __init__(self, label, value, limit):
        self.amount = value    # stored as "amount", not "value"; users of this class should access the value using 'amount' (e.g., r.amount), not 'value'
        self.amount = value    # stored as "amount", not "value"
        self.limit = limit

r = Record("R-001", 87.0, 100.0)
print(r.amount)
