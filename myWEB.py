import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import webview

class WebBrowserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Browser")

        self.create_widgets()

    def create_widgets(self):
        self.url_entry = ttk.Entry(self.root, width=50)
        self.url_entry.pack(pady=10)

        self.open_button = ttk.Button(self.root, text="Open Link", command=self.open_link)
        self.open_button.pack(pady=5)

        self.webview = None

    def open_link(self):
        link = self.url_entry.get()
        if not link.startswith("http://") and not link.startswith("https://"):
            messagebox.showwarning("Invalid Link", "Please enter a valid URL starting with 'http://' or 'https://'")
            return

        if self.webview:
            self.webview.destroy()

        self.webview = webview.create_window("Web Browser", url=link, width=800, height=600)

# Create the main window
root = tk.Tk()

# Check if WebView is available
if webview.available():
    app = WebBrowserApp(root)
else:
    messagebox.showerror("WebView Not Available", "The WebView component is not available on this platform.")

# Start the Tkinter event loop
root.mainloop()
