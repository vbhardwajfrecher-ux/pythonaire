import tkinter as tk

class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Todo App")
        self.geometry("300x400")

        self.tasks = []

        self.task_var = tk.StringVar(value=self.tasks)
        self.task_list = tk.Listbox(self, listvariable=self.task_var)
        self.task_list.pack(fill="both", expand=True)

        self.task_entry = tk.Entry(self)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self, text="Add", command=self.add_task)
        self.add_button.pack()

        self.remove_button = tk.Button(self, text="Remove", command=self.remove_task)
        self.remove_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        self.tasks.append(task)
        self.task_var.set(self.tasks)

    def remove_task(self):
        selected_task = self.task_list.get(self.task_list.curselection())
        self.tasks.remove(selected_task)
        self.task_var.set(self.tasks)

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()
