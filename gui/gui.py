import os
import tkinter as tk
from tkinter import filedialog, messagebox
from core.utils import build_bionic_epub\

class BionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EPUB Bionic Reader")
        self.root.geometry("700x120")
        self.root.resizable(False, False)

        label = tk.Label(root, text="Convert EPUB to Bionic Reading EPUB", font=("Arial", 12, "bold"))
        label.pack(pady=10)

        frame = tk.Frame(root)
        frame.pack(padx=10)

        # Input Row
        self.input_entry = tk.Entry(frame, width=60)
        self.input_entry.grid(row=0, column=0, padx=(0, 5))
        browse_btn = tk.Button(frame, text="Browse", command=self.browse_input)
        browse_btn.grid(row=0, column=1)

        # Output Row
        self.output_entry = tk.Entry(frame, width=60)
        self.output_entry.grid(row=1, column=0, padx=(0, 5), pady=10)
        build_btn = tk.Button(frame, text="Build", command=self.build_output)
        build_btn.grid(row=1, column=1)

    def browse_input(self):
        path = filedialog.askopenfilename(filetypes=[("EPUB files", "*.epub")])
        if path:
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, path)

            # Auto-fill output
            directory = os.path.dirname(path)
            filename = os.path.basename(path)
            if filename.lower().endswith(".epub"):
                base_name = filename[:-5]  
            else:
                base_name = filename
            new_name = f"(Bionic) {base_name}.epub"
            output_path = os.path.join(directory, new_name)

            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, output_path)
    
    def build_output(self):
        input_path = self.input_entry.get()
        output_path = self.output_entry.get()
        if not input_path or not output_path:
            messagebox.showwarning("Missing Fields", "Please provide both input and output paths.")
            return
        build_bionic_epub(input_path, output_path)
        messagebox.showinfo("Success", f"New EPUB saved to:\n{output_path}")
