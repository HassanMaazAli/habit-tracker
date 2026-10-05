# habit_tracker.py

habits = [
    ("Drink water", True),
    ("Read 10 pages", False),
    ("Exercise", True),
    ("Sleep 8 hours", True)
]

def habit_report(habits):
    completed_count = sum(1 for name, status in habits if status)
    return {"completed": completed_count, "total": len(habits)}

# Loop through and display each habit status
for name, status in habits:
    status_str = "Done" if status else "Not done"
    print(f"{name}: {status_str}")

# Print report
report = habit_report(habits)
print(report)