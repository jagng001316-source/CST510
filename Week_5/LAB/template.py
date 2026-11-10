"""
RECORD CHECK  -  my version
===========================

Name  : Gibril
Lane  : Cyber
Date  :
"""

class Record:
    """Store one labeled value and its limit."""

    def __init__(self, label, value, limit):
        """Initialize a record with its label, value, and limit."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the status based on the value as a percentage of the limit."""
        percent = self.value / self.limit * 100
        if percent >= 100:
            return "OVER LIMIT"
        if percent >= 90:
            return "WARNING"
        return "OK"


records = [
    Record("R-001", 87, 100),
    Record("R-002", 120, 100),
    Record("R-003", 95, 100),
]

over_limit_count = 0

for record in records:
    status = record.status()
    if status == "OVER LIMIT":
        over_limit_count += 1

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  Value       : {record.value:>10.2f}")
    print(f"  Limit       : {record.limit:>10.2f}")
    print(f"  Status      : {status:>10}")
    print("=" * 34)

print(f"Records over limit: {over_limit_count}")
