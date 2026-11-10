"""
RECORD CHECK  -  my version
===========================

Name  : Gibril
Lane  : Cyber
Date  :
"""

def check_record(value, limit):
    """Calculate the difference, percentage and status for a record."""
    difference = value - limit
    percent = value / limit * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print a bordered report for one record."""
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


records = [
    {"label": "R-001", "value": 87, "limit": 100},
    {"label": "R-002", "value": 120, "limit": 100},
    {"label": "R-003", "value": 45, "limit": 100},
]

for record in records:
    difference, percent, status = check_record(record["value"], record["limit"])
    print_report(
        record["label"],
        record["value"],
        record["limit"],
        difference,
        percent,
        status,
    )
