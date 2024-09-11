from tkinter import filedialog
import tkinter as tk

def get_directory():
    # Create the root window for the Tkinter application
    root = tk.Tk()

    # Prompt the user to select a folder
    folder_path = filedialog.askdirectory()

    # Print the path of the selected folder
    print("Directory Selected:", folder_path, "\n")

    # Close the root window
    root.destroy()

    return folder_path