import csv
import os
import datetime

FILE_NAME = "study_log.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Subject", "Hours"])

def log_session():
    print("\n--- Log Session ---")
    subject = input("Enter Subject: ").strip()
    if not subject:
        print("Subject cannot be empty.")
        return

    try:
        hours = float(input("Enter Hours Studied: "))
        if hours <= 0:
            print("Hours must be positive.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    today = datetime.date.today()
    with open(FILE_NAME, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([today, subject, hours])
    print(f"Saved: {hours} hours for {subject}.")

def view_analytics():
    if not os.path.exists(FILE_NAME):
        print("No data found.")
        return

    total_hours = 0
    subject_map = {}
    
    try:
        with open(FILE_NAME, 'r') as f:
            reader = csv.reader(f)
            next(reader) # Skip header
            for row in reader:
                if not row: continue
                subj = row[1]
                try:
                    hrs = float(row[2])
                    total_hours += hrs
                    subject_map[subj] = subject_map.get(subj, 0) + hrs
                except ValueError:
                    continue
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    if total_hours == 0:
        print("No sessions recorded yet.")
        return

    print(f"\nTotal Study Time: {total_hours} hours")
    print(f"Average per subject: {round(total_hours / len(subject_map), 2)} hours")
    
    most_studied = max(subject_map, key=subject_map.get)
    print(f"Most Studied Subject: {most_studied} ({subject_map[most_studied]} hours)")

def main():
    initialize_file()
    while True:
        print("\n1. Log Study Time\n2. View Analytics\n3. Exit")
        choice = input("Choice: ")
        if choice == '1': log_session()
        elif choice == '2': view_analytics()
        elif choice == '3': break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()
