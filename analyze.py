from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).parent
DATA = ROOT / "data" / "manufacturing_sample.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
required = {"date", "line", "product", "units_produced", "defects", "downtime_minutes"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Dataset is missing columns: {sorted(missing)}")

if (df["units_produced"] < 0).any() or (df["defects"] < 0).any():
    raise ValueError("Units and defects must be non-negative.")
if (df["defects"] > df["units_produced"]).any():
    raise ValueError("Defects cannot exceed units produced.")

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date", "line", "units_produced", "defects"])
df["defect_rate_pct"] = df["defects"].div(df["units_produced"].replace(0, pd.NA)).mul(100)

summary = (
    df.groupby("line", as_index=False)
      .agg(units_produced=("units_produced", "sum"),
           defects=("defects", "sum"),
           downtime_minutes=("downtime_minutes", "sum"))
)
summary["defect_rate_pct"] = summary["defects"] / summary["units_produced"].replace(0, float("nan")) * 100
summary.to_csv(OUT / "line_summary.csv", index=False)
print("Summary by production line:")
print(summary.round(2).to_string(index=False))

plt.figure()
plt.bar(summary["line"], summary["units_produced"])
plt.title("Units produced by line")
plt.xlabel("Production line")
plt.ylabel("Units produced")
plt.tight_layout()
plt.savefig(OUT / "units_by_line.png", dpi=160)
plt.close()

plt.figure()
plt.bar(summary["line"], summary["defect_rate_pct"])
plt.title("Defect rate by line")
plt.xlabel("Production line")
plt.ylabel("Defect rate (%)")
plt.tight_layout()
plt.savefig(OUT / "defect_rate_by_line.png", dpi=160)
plt.close()

print(f"\nSaved outputs to: {OUT}")
