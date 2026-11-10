"""
RECORD CHECK  -  my version
===========================

Name  : Gibril
Lane  : Cyber
Date  :
"""

label = input("Enter a label: ")
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

difference = first - second
percent = first / second * 100

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"  First value : {first:>10.2f}")
print(f"  Second value: {second:>10.2f}")
print(f"  Difference  : {difference:>+10.2f}")
print(f"  Percent     : {percent:>10.2f}%")
print("  Checked by  : Gibril")
print("=" * 34)
