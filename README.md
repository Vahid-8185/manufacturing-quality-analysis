# Manufacturing Quality and Production Analysis

> Portfolio project for an Applied Data Science internship. This is a learning project using a **synthetic sample dataset**, not real Siemens data.

## Goal
Explore production output, defects, and downtime, then summarize useful operational indicators.

## Questions
- Which product lines have the highest defect rates?
- How does downtime vary by production line?
- What patterns should a manufacturing team investigate?

## Tools
Python, pandas, matplotlib, Power BI or Excel (optional).

## Dataset
`data/manufacturing_sample.csv` is a small synthetic dataset generated for this project. It is illustrative only and must not be represented as real factory data.

## Run
```bash
python -m pip install -r requirements.txt
python analyze.py
```

The script prints summary metrics and saves charts in `outputs/`.

## Method
1. Check missing values and data types.
2. Calculate total units, defect rate, and downtime by production line.
3. Visualize output and defect-rate comparisons.
4. Write a short findings report.

## Results
Run the analysis and replace this section with your actual output and observations. Do not invent performance improvements or business impact.

## Limitations
The dataset is synthetic and small. Results demonstrate the workflow only; they do not establish real-world manufacturing conclusions.
