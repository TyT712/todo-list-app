tasks = []

def add_task(task_name):
    """Thêm một công việc mới vào danh sách dưới dạng dictionary."""
    task = {'name': task_name, 'completed': False}
    tasks.append(task)
    print(f"Đã thêm công việc: '{task_name}'")

def complete_task(task_index):
    """Đánh dấu một công việc là hoàn thành dựa vào chỉ số (task_index)."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"Đã hoàn thành công việc: '{tasks[task_index]['name']}'")
    else:
        print(f"Lỗi: Chỉ số {task_index} không hợp lệ.")

def list_tasks(task_list=None):
    """Hiển thị danh sách các công việc cùng trạng thái hoàn thành."""
    current_tasks = tasks if task_list is None else task_list
    stt = 1
    for task in current_tasks:
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{stt}. {status} {task['name']}")
        stt += 1
        
# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    
    # Đánh dấu hoàn thành công việc đầu tiên (index 0)
    complete_task(0)
    
    list_tasks()