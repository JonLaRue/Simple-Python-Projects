from PIL import Image
import re
import tkinter as tk
from tkinter import ttk, filedialog
import pytesseract
import sys
import os

# Function to get the path of the Tesseract executable
def get_tesseract_path():
    try:
        # Try to use _MEIPASS (set by PyInstaller to the temp folder containing bundled resources)
        base_path = sys._MEIPASS
    except Exception:
        # Fallback to the current directory if not running as a PyInstaller bundle
        base_path = os.path.abspath(".")

    # Adjust the path below if you place Tesseract in a subdirectory
    return os.path.join(base_path, 'tesseract.exe')

# Set the Tesseract command to the dynamically determined path
pytesseract.pytesseract.tesseract_cmd = get_tesseract_path()


# Function to browse and select an image file
def browse_image():
    filename = filedialog.askopenfilename()
    if filename:
        analyze_image(filename)

# Function to analyze the selected image
def analyze_image(image_path):
    
    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(Image.open(image_path))

    # Extract material numbers using regular expressions
    material_numbers = re.findall(r'\b\d{8,9}\b', text)

    # Clear previous results
    text_widget.delete(1.0, tk.END)

    # Check if material numbers were found
    if material_numbers:
        # Insert the material numbers into the text widget
        text_widget.insert(tk.INSERT, "\n".join(material_numbers))
    else:
        # Insert "No Material Numbers found" message
        text_widget.insert(tk.INSERT, "No Material Numbers found")

# Create a tkinter window
root = tk.Tk()
root.title("Material Numbers")

# Create a button to browse and select an image
browse_button = ttk.Button(root, text="Browse Image", command=browse_image)
browse_button.pack()

# Create a text widget to display the results
text_widget = tk.Text(root, width=40, height=10)
text_widget.pack()

# Create a frame to hold the buttons
button_frame = ttk.Frame(root)
button_frame.pack()

# Create a button to select all and copy
def select_all_and_copy():
    text_widget.tag_add("sel", "1.0", "end-1c")
    root.clipboard_clear()
    root.clipboard_append(text_widget.selection_get())

select_all_button = ttk.Button(button_frame, text="Select All & Copy", command=select_all_and_copy)
select_all_button.pack(side=tk.LEFT)

# Create a button to close the window
close_button = ttk.Button(button_frame, text="Close", command=root.destroy)
close_button.pack(side=tk.LEFT)

# Run the tkinter main loop
root.mainloop()
