
import json

with open("artifacts/run.json") as f:
    data = json.load(f)

total = len(data["results"])
failures = sum(1 for r in data["results"] if r["status"] != "PASS")

report = f"""# Evaluation Report

Total tests: {total}
Failures: {failures}
Ledger hash: {data['ledger_hash']}
"""

with open("artifacts/report.md", "w") as f:
    f.write(report)

print(report)
