import re
from pathlib import Path

file = Path("nexvion-logs.txt")
if not file.exists():
    raise SystemExit("nexvion-logs.txt not found")

lines = file.read_text(errors="replace").splitlines()
for label, pattern in {
    "Errors": r"\berror\b|\bexception\b|\bfatal\b",
    "Warnings": r"\bwarn(?:ing)?\b",
    "Connection issues": r"connection refused|timeout|unreachable",
}.items():
    matches = [line for line in lines if re.search(pattern, line, re.I)]
    print(f"\n{label}: {len(matches)}")
    for line in matches[-5:]:
        print("-", line[:250])

print("\nRule-based log triage complete; no AI model is used.")
