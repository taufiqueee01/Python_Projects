import json
import os
import datetime

FILE_NAME = "habits.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return {}
    try:
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(FILE_NAME, 'w') as f:
        json.dump(data, f, indent=4)

def add_habit(data):
    name = input("Enter new habit name: ").strip()
    if name and name not in data:
        data[name] = []
        save_data(data)
        print("Habit added.")
    else:
        print("Habit already exists or invalid name.")

def mark_done(data):
    name = input("Enter habit to mark done: ").strip()
    if name in data:
        today = str(datetime.date.today())
        if today not in data[name]:
            data[name].append(today)
            save_data(data)
            print("Marked as done for today!")
        else:
            print("Already marked for today.")
    else:
        print("Habit not found.")

def view_streaks(data):
    print("\n--- Habit Streaks ---")
    for habit, dates in data.items():
        dates.sort()
        max_streak = 0
        
        if not dates:
            print(f"{habit}: 0 days")
            continue
            
        current_streak = 1
        date_objs = [datetime.datetime.strptime(d, "%Y-%m-%d").date() for d in dates]
        
        for i in range(1, len(date_objs)):
            delta = (date_objs[i] - date_objs[i-1]).days
            if delta == 1:
                current_streak += 1
            else:
                max_streak = max(max_streak, current_streak)
                current_streak = 1
        max_streak = max(max_streak, current_streak)
        
        print(f"{habit}: Longest Streak = {max_streak} days")

def main():
    data = load_data()
    while True:
        print("\n1. Add Habit\n2. Mark Done\n3. View Streaks\n4. Exit")
        c = input("Choice: ")
        if c == '1': add_habit(data)
        elif c == '2': mark_done(data)
        elif c == '3': view_streaks(data)
        elif c == '4': break

if __name__ == "__main__":
    main()
