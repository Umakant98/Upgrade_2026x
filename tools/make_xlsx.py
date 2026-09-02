import pandas as pd
from pathlib import Path

csv_dir = Path("upgrade-runbook/excel_sheets")
out_xlsx = Path("upgrade-runbook/Upgrade_RunTracker_R2026x.xlsx")

files_and_sheets = [
    ("Master_Task_Tracker.csv","Master Task Tracker"),
    ("Cutover_Runbook.csv","Cutover Runbook"),
    ("Validation_Evidence.csv","Validation Evidence"),
    ("Risk_Register.csv","Risk Register"),
    ("Gantt.csv","Gantt"),
]

with pd.ExcelWriter(out_xlsx, engine="openpyxl") as writer:
    for fname, sheet in files_and_sheets:
        path = csv_dir / fname
        if path.exists():
            df = pd.read_csv(path)
            df.to_excel(writer, sheet_name=sheet, index=False)
        else:
            pd.DataFrame({"Note":[f"{fname} not found"]}).to_excel(writer, sheet_name=sheet, index=False)

print("Wrote", out_xlsx)
