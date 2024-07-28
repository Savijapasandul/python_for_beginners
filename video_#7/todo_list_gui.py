import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.todos = []

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.listbox = tk.Listbox(self.frame)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add To-Do", command=self.add_todo)
        self.add_button.pack()

        self.delete_button = tk.Button(root, text="Delete To-Do", command=self.delete_todo)
        self.delete_button.pack(pady=5)

    def add_todo(self):
        todo = self.entry.get()
        if todo:
            self.listbox.insert(tk.END, todo)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a to-do item.")

    def delete_todo(self):
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a to-do item to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
