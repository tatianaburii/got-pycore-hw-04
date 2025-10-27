from pathlib import Path
from typing import Tuple

def total_salary(path: str | Path) -> Tuple[int, float]:
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    name, amount = line.split(",", 1)
                    total += int(amount.strip())
                    count += 1
                except ValueError:
                    continue
    except FileNotFoundError:
        return 0, 0.0

    average = (total / count) if count else 0.0
    return total, average

path = Path("homework6/data.txt")
# total, average = total_salary("homework6/data.txt")
total, average = total_salary(path)

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
