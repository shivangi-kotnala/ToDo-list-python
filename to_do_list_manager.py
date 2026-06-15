from datetime import datetime

tasks = []

def days_left(deadline_str):
    try:
        deadline = datetime.strptime(deadline_str, "%d-%m-%Y")
        today = datetime.today()
        diff = (deadline - today).days
        if diff < 0:
            return f"⚠️ Overdue by {abs(diff)} days"
        elif diff == 0:
            return "🔴 Due Today!"
        else:
            return f"🗓️ {diff} days left"
    except:
        return "📅 Invalid date"

"""ADD task function"""

def add_task():
    print("\n--- Add Task ---")
    name = input("Task name: ")
    priority = input("Priority (High / Medium / Low): ").capitalize()
    deadline = input("Deadline (DD-MM-YYYY): ")
    tasks.append({
        "name": name,
        "priority": priority,
        "deadline": deadline,
        "done": False
    })
    print(f"✅ Task '{name}' added!")

"""view task function"""

def view_tasks():
    print("\n--- Your Tasks ---")
    if not tasks:
        print("No tasks yet!")
        return
    for i, t in enumerate(tasks, 1):
        status = "✅ Done" if t["done"] else "⏳ Pending"
        time_left = days_left(t["deadline"]) if not t["done"] else "Completed"
        print(f"{i}. [{status}] {t['name']} | Priority: {t['priority']} | Deadline: {t['deadline']}|{time_left}")

"""delete task function"""

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("\nEnter task number to delete: "))
        removed = tasks.pop(num - 1)
        print(f"🗑️ Task '{removed['name']}' deleted!")
    except (ValueError, IndexError):
        print("Invalid number.")

"""Mark done function"""

def mark_done():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("\nEnter task number to mark as done: "))
        tasks[num - 1]["done"] = True
        print(f"🎉 Task marked as done!")
    except (ValueError, IndexError):
        print("Invalid number.")

"""Main function"""

def main():
    print("=" * 40)
    print("       📝 Simple To-Do List")
    print("=" * 40)
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("\nChoose an option (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("\nGoodbye! Stay organized! 👋")
            break
        else:
            print("Invalid choice. Please enter 1-5.")



main()


