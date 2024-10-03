import tkinter as tk
from tkinter import filedialog, messagebox


class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")
        self.root.geometry("600x400")

      
        self.root.configure(bg="#333333") 

        self.create_buttons()

       
        self.separator = tk.Frame(root, height=2, bd=1, relief='sunken', bg='gray')
        self.separator.pack(fill='x')

       
        self.text_area = tk.Text(root, wrap='word', bg="#ffffff", fg="#000000", font=("Helvetica", 12))
        self.text_area.pack(expand=1, fill='both', padx=10, pady=10)

    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg="#333333") 
        button_frame.pack(fill='x')

       
        new_button = tk.Button(button_frame, text="New File", command=self.new_file, bg="#FFEB3B", fg="#000000")
        new_button.grid(row=0, column=0, padx=5, pady=5)

        
        open_button = tk.Button(button_frame, text="Open File", command=self.open_file, bg="#FFEB3B", fg="#000000")
        open_button.grid(row=0, column=1, padx=5, pady=5)

        
        save_button = tk.Button(button_frame, text="Save File", command=self.save_file, bg="#FFEB3B", fg="#000000")
        save_button.grid(row=0, column=2, padx=5, pady=5)

       
        exit_button = tk.Button(button_frame, text="Exit", command=self.root.quit, bg="#FFEB3B", fg="#000000")
        exit_button.grid(row=0, column=3, padx=5, pady=5)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text files", "*.txt"),
                                                          ("All files", "*.*")])
        if file_path:
            self.text_area.delete(1.0, tk.END)  
            with open(file_path, 'r') as file:
                self.text_area.insert(tk.END, file.read())  

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"),
                                                            ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END).strip()) 

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
