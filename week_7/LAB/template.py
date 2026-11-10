"""
RECORD CHECK  -  my version
===========================

Name  : Gibril
Lane  : Cyber
Date  :
"""

from pathlib import Path


def parse_line(raw_line):
    """Clean and parse one comma-separated cyber event line."""
    record = {}
    for piece in raw_line.strip().split(","):
        key, value = piece.split("=", 1)
        record[key.strip().lower()] = value.strip().lower()

    record["attempts"] = int(record["attempts"])
    return record


def status_of(record):
    """Flag events with failed results or at least ten attempts."""
    if record["result"] == "failed" or record["attempts"] >= 10:
        return "FLAGGED"
    return "OK"


data_path = Path(__file__).resolve().parent / "cyber_events.txt"
with data_path.open(encoding="utf-8") as data_file:
    raw_records = [line for line in data_file if line.strip()]

flagged_count = 0
for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record)
    if status == "FLAGGED":
        flagged_count += 1
    print(record, status)

print(f"Records: {len(raw_records)}; flagged: {flagged_count}")
