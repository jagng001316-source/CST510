"""
RECORD CHECK  -  my version
===========================

Name  : Gibril
Lane  : Cyber
Date  :
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

lab_dir = Path(__file__).resolve().parent
df = pd.read_csv(lab_dir / "records_sample.csv")

df["percent"] = (df["value"] / df["limit"]) * 100
df["status"] = df["percent"].apply(
    lambda percent: (
        "OVER LIMIT" if percent >= 100 else "WARNING" if percent >= 90 else "OK"
    )
)

print("All records:")
print(df)

print("\nRecords that need attention:")
print(df[df["status"] != "OK"])

status_counts = df.groupby("status").size()
print("\nCount by status:")
print(status_counts)

df.to_csv(lab_dir / "records_report.csv", index=False)
status_counts.plot(kind="bar", xlabel="Status", ylabel="Number of records")
plt.tight_layout()
plt.savefig(lab_dir / "status_counts.png")

# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
