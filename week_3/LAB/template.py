"""
RECORD CHECK  -  my version
===========================

Name  : Gibril
Lane  : Cyber
Date  :
"""


def status_of(percent):
    """Return a status based on the percentage of the limit."""
    if percent >= 100:
        return "OVER LIMIT"
    if percent >= 90:
        return "WARNING"
    return "OK"


def check(value, limit):
    """Calculate and return the difference and percentage."""
    difference = value - limit
    percent = value / limit * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print one bordered record report."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Value       : {value:>10.2f}")
    print(f"  Limit       : {limit:>10.2f}")
    print(f"  Difference  : {difference:>+10.2f}")
    print(f"  Of limit    : {percent:>9.1f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)


over_limit_count = 0

while True:
    label = input("Record label (or 'quit' to stop): ")
    if label.strip().lower() == "quit":
        break

    value = float(input("Value: "))
    limit = float(input("Limit: "))
    difference, percent = check(value, limit)
    status = status_of(percent)
    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_limit_count += 1

print(f"Records over limit: {over_limit_count}")
