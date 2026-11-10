# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

import pandas as pd

df = pd.DataFrame({"value": ["87", "120", "45"], "limit": [100, 100, 100]})

# Convert "value" to float, divide by "limit", and multiply by 100 to get the percent
df["value_float"] = df["value"].astype(float)
df["percent"] = (df["value_float"] / df["limit"]) * 100
print(df[["value", "percent"]])
