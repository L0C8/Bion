import os
import customtkinter
from tkinter import filedialog, messagebox
from core.utils import build_bionic_epub  # Ensure this path is correct

class BionApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Bion EPUB Converter")
        self.window.geometry("430x136")
        self.window.configure(bg="#FFFFFF")

        # Input Label
        self.label_input = customtkinter.CTkLabel(
            master=window,
            text="Input:",
            font=("Arial", 14),
            text_color="#000000",
            height=30,
            width=50,
            corner_radius=0,
            bg_color="#FFFFFF",
            fg_color="#FFFFFF",
        )
        self.label_input.place(x=20, y=30)

        # Output Label
        self.label_output = customtkinter.CTkLabel(
            master=window,
            text="Output:",
            font=("Arial", 14),
            text_color="#000000",
            height=30,
            width=50,
            corner_radius=0,
            bg_color="#FFFFFF",
            fg_color="#FFFFFF",
        )
        self.label_output.place(x=20, y=80)

        # Input Entry
        self.input_entry = customtkinter.CTkEntry(
            master=window,
            placeholder_text="Select an EPUB file",
            placeholder_text_color="#454545",
            font=("Arial", 14),
            text_color="#000000",
            height=30,
            width=220,
            border_width=2,
            corner_radius=6,
            border_color="#000000",
            bg_color="#FFFFFF",
            fg_color="#F0F0F0",
        )
        self.input_entry.place(x=80, y=30)

        # Output Entry
        self.output_entry = customtkinter.CTkEntry(
            master=window,
            placeholder_text="Output file path",
            placeholder_text_color="#454545",
            font=("Arial", 14),
            text_color="#000000",
            height=30,
            width=220,
            border_width=2,
            corner_radius=6,
            border_color="#000000",
            bg_color="#FFFFFF",
            fg_color="#F0F0F0",
        )
        self.output_entry.place(x=80, y=80)

        # Browse Button
        self.browse_button = customtkinter.CTkButton(
            master=window,
            text="Browse",
            font=("Arial", 14),
            text_color="#000000",
            hover=True,
            hover_color="#949494",
            height=30,
            width=95,
            border_width=2,
            corner_radius=6,
            border_color="#000000",
            bg_color="#FFFFFF",
            fg_color="#F0F0F0",
            command=self.browse_input,
        )
        self.browse_button.place(x=310, y=30)

        # Build Button
        self.build_button = customtkinter.CTkButton(
            master=window,
            text="Build",
            font=("Arial", 14),
            text_color="#000000",
            hover=True,
            hover_color="#949494",
            height=30,
            width=95,
            border_width=2,
            corner_radius=6,
            border_color="#000000",
            bg_color="#FFFFFF",
            fg_color="#F0F0F0",
            command=self.build_output,
        )
        self.build_button.place(x=310, y=80)

    def browse_input(self):
        path = filedialog.askopenfilename(filetypes=[("EPUB files", "*.epub")])
        if path:
            self.input_entry.delete(0, "end")
            self.input_entry.insert(0, path)

            # Auto-fill output path
            directory = os.path.dirname(path)
            filename = os.path.basename(path)
            base = filename[:-5] if filename.lower().endswith(".epub") else filename
            outpath = os.path.join(directory, f"(Bionic) {base}.epub")

            self.output_entry.delete(0, "end")
            self.output_entry.insert(0, outpath)

    def build_output(self):
        input_path = self.input_entry.get()
        output_path = self.output_entry.get()
        if not input_path or not output_path:
            messagebox.showwarning("Missing Fields", "Please provide both input and output paths.")
            return

        try:
            build_bionic_epub(input_path, output_path)
            messagebox.showinfo("Success", f"New EPUB saved to:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to build EPUB:\n{e}")
