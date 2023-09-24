import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import zipfile
import os
class HardchiveUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hardchive UI")

        self.registry = []
        self.filename = ""

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Hardchive File:")
        self.label.pack()

        self.file_button = tk.Button(self.root, text="Select File", command=self.select_file)
        self.file_button.pack()

        self.register_button = tk.Button(self.root, text="Register File", command=self.register_file)
        self.register_button.pack()

        self.create_button = tk.Button(self.root, text="Create Hardchive", command=self.create_hardchive)
        self.create_button.pack()

    def select_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.label.config(text=f"Selected File: {self.file_path}")

    def register_file(self):
        if self.file_path:
            self.registry.append(self.file_path)
            messagebox.showinfo("File Registered", "File registered successfully.")
        else:
            messagebox.showerror("Error", "No file selected.")

    def create_hardchive(self):
        if not self.registry:
            messagebox.showerror("Error", "No files registered.")
            return

        self.filename = filedialog.asksaveasfilename(defaultextension=".xzip", filetypes=[("Hardchive Files", "*.xzip")])
        if self.filename:
            try:
                with zipfile.ZipFile(self.filename, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
                    for file_path in self.registry:
                        zipf.write(file_path, arcname=os.path.basename(file_path))
                messagebox.showinfo("Hardchive Created", f"Hardchive '{self.filename}' created successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HardchiveUI(root)
    root.mainloop()
