def show_tasks(tasks):
    """Показывает список задач."""
    if not tasks:
        print("Список задач пуст.")
    else:
        print("\nСписок задач:")
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. {task['title']} [{status}]")
    print()

def add_task(tasks):
    """Добавляет новую задачу."""
    title = input("Введите описание задачи: ")
    tasks.append({"title": title, "done": False})
    print("Задача добавлена.\n")

def complete_task(tasks):
    """Отмечает задачу как выполненную."""
    show_tasks(tasks)
    try:
        task_number = int(input("Введите номер задачи для отметки выполнения: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number]["done"] = True
            print("Задача отмечена как выполненная.\n")
        else:
            print("Неверный номер задачи.\n")
    except ValueError:
        print("Введите корректное число.\n")

def delete_task(tasks):
    """Удаляет задачу из списка."""
    show_tasks(tasks)
    try:
        task_number = int(input("Введите номер задачи для удаления: ")) - 1
        if 0 <= task_number < len(tasks):
            removed_task = tasks.pop(task_number)
            print(f"Задача \"{removed_task['title']}\" удалена.\n")
        else:
            print("Неверный номер задачи.\n")
    except ValueError:
        print("Введите корректное число.\n")

def main():
    tasks = []
    while True:
        print("Меню:")
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Отметить задачу выполненной")
        print("4. Удалить задачу")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.\n")

if __name__ == "__main__":
    main()
