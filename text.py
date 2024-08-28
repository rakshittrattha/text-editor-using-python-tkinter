import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, colorchooser

class MyTextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("My Text Editor")
        self.master.geometry("800x600")

        # Default settings for text attributes
        self.current_font_family = 'Helvetica'
        self.current_font_size = 12
        self.current_text_color = 'black'

        # Set up the main text area
        self.text_widget = tk.Text(master, wrap='word', undo=True)
        self.text_widget.pack(expand=True, fill='both')

        # Create the menu bar
        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)

        # File menu with options
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.clear_text)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Exit", command=self.quit_editor)

        # Edit menu with text customization options
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        # Font family dropdown
        self.font_family_var = tk.StringVar(value=self.current_font_family)
        self.font_family_menu = tk.Menu(self.edit_menu, tearoff=0)
        for font in ["Helvetica", "Arial", "Courier New", "Times New Roman", "Verdana"]:
            self.font_family_menu.add_command(label=font, command=lambda f=font: self.change_font_family(f))
        self.edit_menu.add_cascade(label="Font Style", menu=self.font_family_menu)

        # Font size dropdown
        self.font_size_var = tk.StringVar(value=str(self.current_font_size))
        self.font_size_menu = tk.Menu(self.edit_menu, tearoff=0)
        for size in [8, 10, 12, 14, 16, 18, 20, 24, 28, 36, 48]:
            self.font_size_menu.add_command(label=str(size), command=lambda s=size: self.change_font_size(s))
        self.edit_menu.add_cascade(label="Font Size", menu=self.font_size_menu)

        # Text color dropdown
        self.text_color_var = tk.StringVar(value=self.current_text_color)
        self.text_color_menu = tk.Menu(self.edit_menu, tearoff=0)
        for color in ["black", "red", "green", "blue", "yellow", "orange", "purple", "gray"]:
            self.text_color_menu.add_command(label=color, command=lambda c=color: self.change_text_color(c))
        self.edit_menu.add_cascade(label="Text Color", menu=self.text_color_menu)

        # Apply initial settings
        self.apply_text_attributes()

    def clear_text(self):
        """Clear the text widget."""
        self.text_widget.delete(1.0, tk.END)

    def open_file(self):
        """Open a file and load its contents into the text widget."""
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"),
                       ("Markdown files", "*.md"),
                       ("Python files", "*.py"),
                       ("All files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text_widget.delete(1.0, tk.END)
                    self.text_widget.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror("File Error", f"Could not open the file: {e}")

    def save_file(self):
        """Save the content of the text widget to a file."""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"),
                       ("Markdown files", "*.md"),
                       ("Python files", "*.py"),
                       ("All files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    content = self.text_widget.get(1.0, tk.END)
                    file.write(content)
            except Exception as e:
                messagebox.showerror("File Error", f"Could not save the file: {e}")

    def quit_editor(self):
        """Ask the user if they want to exit and close the editor."""
        if messagebox.askokcancel("Exit", "Do you really want to quit?"):
            self.master.quit()

    def change_font_family(self, font):
        """Change the font family of the text widget."""
        self.current_font_family = font
        self.apply_text_attributes()

    def change_font_size(self, size):
        """Change the font size of the text widget."""
        self.current_font_size = size
        self.apply_text_attributes()

    def change_text_color(self, color):
        """Change the text color of the text widget."""
        self.current_text_color = color
        self.apply_text_attributes()

    def apply_text_attributes(self):
        """Apply the selected font family, size, and color to the text widget."""
        self.text_widget.config(font=(self.current_font_family, self.current_font_size))
        self.text_widget.config(fg=self.current_text_color)

if __name__ == "__main__":
    root = tk.Tk()
    editor = MyTextEditor(root)
    root.mainloop()
