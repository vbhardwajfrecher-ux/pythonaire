import tkinter as tk
from tkinter import ttk

def process_input():
    # Get the input text from the input textbox
    input_text = input_textbox.get("1.0", "end").strip()

    # Split the input into a list of numbers
    numbers = input_text.split("\n")

    # Format each number and join them with commas
    formatted_output = ",".join([f"'{number}'" for number in numbers])

    # Clear the output textbox
    output_textbox.delete("1.0", "end")

    # Insert the formatted output into the output textbox
    output_textbox.insert("1.0", formatted_output)


# Create the main window
window = tk.Tk()
window.title("Input Formatter")

# Configure the style
style = ttk.Style()
style.theme_use("clam")  # Choose a built-in theme (change as desired)

# Configure custom colors
style.configure("TLabel",
                background="#1e1e1e",
                foreground="white",
                font=("Helvetica", 12))
style.configure("TButton",
                background="#1e1e1e",
                foreground="white",
                font=("Helvetica", 12, "bold"))
style.configure("TText",
                background="#1e1e1e",
                foreground="white",
                font=("Courier New", 12))

# Create the input label and textbox
input_label = ttk.Label(window, text="Input:")
input_label.pack()

input_textbox = tk.Text(window, height=20, width=40)
input_textbox.pack()

# Create the process button
process_button = ttk.Button(window, text="Process", command=process_input)
process_button.pack()

# Create the output label and textbox
output_label = ttk.Label(window, text="Output:")
output_label.pack()

output_textbox = tk.Text(window, height=20, width=40)
output_textbox.pack()

# Start the Tkinter event loop
window.mainloop()
