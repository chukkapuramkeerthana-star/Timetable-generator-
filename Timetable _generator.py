# Timetable Generator

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
periods = 6

subjects = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    subject = input(f"Enter subject {i+1}: ")
    subjects.append(subject)

print("\nWEEKLY TIMETABLE\n")

count = 0

for day in days:
    print(day)
    for period in range(1, periods + 1):
        print(f"Period {period}: {subjects[count % len(subjects)]}")
        count += 1
    print("-" * 20)
