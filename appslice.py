import tkinter as tk

def process_input():
    input_text = input_textbox.get("1.0", "end").strip()  # Get the input text and remove leading/trailing spaces
    numbers = input_text.split("\n")  # Split the input into a list of numbers
    formatted_output = ",".join(f"'{number}'" for number in numbers)  # Format each number and join them with commas
    
    output_textbox.delete("1.0", "end")  # Clear the output textbox
    output_textbox.insert("1.0", formatted_output)  # Insert the formatted output
    
# Create the main window
window = tk.Tk()
window.title("Input Formatter")

# Create the input label and textbox
input_label = tk.Label(window, text="Input:")
input_label.pack()

input_textbox = tk.Text(window, height=5, width=30)
input_textbox.pack()

# Create the process button
process_button = tk.Button(window, text="Process", command=process_input)
process_button.pack()

# Create the output label and textbox
output_label = tk.Label(window, text="Output:")
output_label.pack()

output_textbox = tk.Text(window, height=5, width=30)
output_textbox.pack()

# Start the Tkinter event loop
window.mainloop()
