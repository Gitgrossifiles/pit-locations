import pandas as pd
import json

# 1. Load Excel
df = pd.read_excel("Pit_GPS.xlsx")

# 2. Map columns A–F → fields
df = df.rename(columns={
    df.columns[0]: "address",      # A
    df.columns[1]: "business",     # B
    df.columns[2]: "description",  # C
    df.columns[3]: "lat",          # D
    df.columns[4]: "lng",          # E
    df.columns[5]: "serial"        # F
})

# 3. Coerce coordinates & drop bad rows
df["lat"] = pd.to_numeric(df["lat"], errors="coerce")
df["lng"] = pd.to_numeric(df["lng"], errors="coerce")
df = df.dropna(subset=["lat", "lng"])

# 4. Clean strings
for col in ["address", "business", "description", "serial"]:
    df[col] = (
        df[col]
        .fillna("")
        .astype(str)
        .str.replace("\r", " ", regex=False)
        .str.replace("\n", " ", regex=False)
        .str.strip()
    )

# 5. Convert to list of dicts
records = df.to_dict(orient="records")

# 6. Save JSON exactly as pit_locations.json
with open("pit_locations.json", "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=2)

print(f"Wrote {len(records)} records to pit_locations.json")

