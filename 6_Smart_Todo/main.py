import csv
import os

FILE_NAME = "todo_list.csv"

def add_task():
    task = input("Task Name: ").strip()
    if not task: return
    
    try:
        priority = int(input("Priority (1=High, 3=Low): "))
        deadline = input("Deadline (YYYY-MM-DD): ")
    except ValueError:
        print("Invalid input.")
        return

    with open(FILE_NAME, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([priority, task, deadline])
    print("Task added!")

def view_tasks():
    if not os.path.exists(FILE_NAME):
        print("No tasks found.")
        return
        
    tasks = []
    with open(FILE_NAME, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row: tasks.append(row)
    
    # Sort by priority (column 0)
    tasks.sort(key=lambda x: x[0])
    
    print("\n--- Smart Task List (Sorted by Priority) ---")
    print(f"{'Pri':<5} {'Task':<20} {'Deadline'}")
    print("-" * 40)
    
    for t in tasks:
        print(f"{t[0]:<5} {t[1]:<20} {t[2]}")
        
    if tasks:
        print(f"\nSuggestion: Do '{tasks[0][1]}' first!")

def main():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w') as f: pass 

    while True:
        print("\n1. Add Task\n2. View & Sort Tasks\n3. Exit")
        choice = input("Choice: ")
        if choice == '1': add_task()
        elif choice == '2': view_tasks()
        elif choice == '3': break

if __name__ == "__main__":
    main()
