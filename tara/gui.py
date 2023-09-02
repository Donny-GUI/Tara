import os
import multiprocessing as mp
import customtkinter as ctk
from tkinter import filedialog
from tkinter import Text, END, messagebox, Listbox, Toplevel
from train_types import train_model
from type_hints import new_file_with_type_hints


class GuiApp:
    def __init__(self, root):
        self.root: ctk.CTk = root
        self.root.title("Python File Executor")
        self.topframe = ctk.CTkFrame(root)
        self.topmframe = ctk.CTkFrame(self.topframe)
        self.topmframe.pack(side="left")
        self.topframe.pack(pady=10)


        self.bottomframe = ctk.CTkFrame(root)
        self.bottomframe.pack(pady=10)
        # Create a browse button
        self.browse_button = ctk.CTkButton(self.topframe, text="Browse", command=self.browse_file)
        self.browse_button.bind("<Enter>", lambda sender : self.on_enter("Browse"))
        self.browse_button.bind("<Leave>", lambda sender : self.on_leave("Browse"))
        self.browse_button.pack(padx=5, pady=5)
        
        self.train_button = ctk.CTkButton(self.topframe, text="Train", command=self.train_event)
        self.train_button.bind("<Enter>", lambda sender : self.on_enter("Train"))
        self.train_button.bind("<Leave>", lambda sender : self.on_leave("Train"))
        self.train_button.pack(padx=5, pady=5)

        self.exit_button = ctk.CTkButton(self.topframe, text="Exit", command=exit)
        self.exit_button.bind("<Enter>", lambda sender : self.on_enter("Exit"))
        self.exit_button.bind("<Leave>", lambda sender : self.on_leave("Exit"))
        self.exit_button.pack(padx=5, pady=5)


        self.typed_files_listbox = Listbox(self.topmframe, height=3, width=50, background="black", foreground="green")
        self.typed_files_listbox.pack(padx=5, pady=5)
        self.selected_file_path = ""
        self.trainProcess = mp.Process(target=train_model)

        self.type_hint_button = ctk.CTkButton(self.topmframe, text="Add Type Hints", command=self.add_type_hints, state="disabled")
        self.type_hint_button.bind("<Enter>", lambda sender : self.on_enter("Add Type Hints"))
        self.type_hint_button.bind("<Leave>", lambda sender : self.on_leave("Add Type Hints"))
        self.type_hint_button.pack(padx=5, pady=5)


        # Create a text widget to display selected file path
        self.file_path_text = Text(self.bottomframe, height=1, width=75)
        self.file_path_text.pack(padx=5, pady=5)

        # text info widget
        self.textvar = ctk.StringVar()
        self.information_widget = ctk.CTkLabel(self.topmframe, height=4, width=75,font=ctk.CTkFont("ubuntu", 5, "normal", "roman"), textvariable=self.textvar)
        self.information_widget.pack(padx=5, pady=5)


    def on_enter(self, sender):
        if sender == "Browse":
            self.typed_files_listbox.delete(0, END)
            self.typed_files_listbox.insert(END, "  browse for a python file to add type hints too.")
            
        elif sender == "Train":
            self.typed_files_listbox.delete(0, END)
            self.typed_files_listbox.insert(END, "Train your model on the current version of ")
            self.typed_files_listbox.insert(END, "python you have and its modules")
    
        elif sender == "Exit":
            self.typed_files_listbox.delete(0, END)
            self.typed_files_listbox.insert(END, "Exit the gui program")
        
        elif sender == "Add Type Hints":
            if self.type_hint_button._state == "normal":
                self.typed_files_listbox.delete(0, END)
                self.typed_files_listbox.insert(END, "Add type hints and return types")
                self.typed_files_listbox.insert(END, "to your python file automatically")
            elif self.type_hint_button._state == "disabled":
                self.typed_files_listbox.delete(0, END)
                self.typed_files_listbox.insert(END, "You must browse for a file first...")

    def on_leave(self, sender):
        self.typed_files_listbox.delete(0, END)
        
    def check_training(self):
        if self.trainProcess.is_alive() == True:
            self.istraining = True
        elif self.trainProcess.is_alive() == False:
            self.istraining = False
        
    def train_event(self):
        self.check_training()
        if self.istraining is False:
            self.trainProcess = mp.Process(target=train_model)
            self.trainProcess.run()
            self.istraining = True

    def flicker_type_hint(self):
        if self.type_hint_button._state != "disabled":
            if self.type_hint_button._fg_color not in ["skyblue", "dodgerblue"]:
                self.type_hint_button.configure(fg_color="dodgerblue")
                self.flicker_type_hint()
            if self.type_hint_button._fg_color == "skyblue":
                self.root.after(350, lambda: self.type_hint_button.configure(fg_color = "dodgerblue"))
            elif self.type_hint_button._fg_color == "dodgerblue":
                self.root.after(350, lambda: self.type_hint_button.configure(fg_color = "skyblue"))
            self.root.after(350, self.flicker_type_hint)

    def browse_file(self):
        # Open a file dialog to select a Python file
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])

        if file_path:
            self.current_file = file_path
            self.selected_file_path = file_path
            self.file_path_text.delete(1.0, END)
            self.file_path_text.insert(END, file_path)
            self.type_hint_button.configure(state="normal")
            self.root.after(1000, self.flicker_type_hint)
    
    def add_type_hints(self):
        self.type_hint_button.configure(state="disabled")
        self.typed_files_listbox.delete(0, END)
        self.typed_files_listbox.insert(END, "Adding type hints to file:")
        self.typed_files_listbox.insert(END, self.file_path_text.get("0.0"))
        self.file_path_text.delete(0.0, END)
        delay = 5
        for i in range(125):
            delay+=5
            self.root.after(delay, lambda: self.file_path_text.insert(END, "█"))
        self.root.after(delay+2, lambda: self.file_path_text.delete(1.0,END))
        self.base = os.path.basename(self.current_file)
        self.name = os.path.splitext(self.base)[0]
        self.nname = "typed_"+self.name+".py"
        self.output_path = os.path.join(os.getcwd(), self.nname)
        new_file_with_type_hints(self.current_file, self.output_path)
        self.root.after(delay+90, lambda: self.file_path_text.delete(1.0, END))
        self.root.after(delay+100, lambda: self.file_path_text.insert(END, self.output_path))
        with open(self.output_path, "r") as f:
            self.source = f.read()   
        self.newwindow = Toplevel(self.root, width=800, height=1000, )
        self.newwindow.focus_force()
        self.newwindow_textwidget = Text(self.newwindow)
        self.newwindow_textwidget.tag_configure("red", foreground="red")
        self.newwindow_textwidget.tag_configure("blue", foreground="blue")
        self.newwindow_textwidget.tag_configure("cyan", foreground="cyan")
        self.newwindow_textwidget.tag_configure("yellow", foreground="yellow")
        self.newwindow_textwidget.tag_configure("green", foreground="green")
        self.pyregex_patterns = [
            ": int", ": float", ": bytes", ": str", ": list", ": set", ": bool", ": bytearray", ": complex", " -> bool:", " -> int:"
        ]
        
        self.newwindow_textwidget.pack(expand=True, fill="both")
        self.newwindow_textwidget.insert("1.0", self.source)

if __name__ == "__main__":
    root = ctk.CTk()
    app = GuiApp(root)
    root.mainloop()
