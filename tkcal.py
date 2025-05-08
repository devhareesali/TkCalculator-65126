import tkinter as tk
from tkinter import ttk, messagebox
import math

# Evaluate expression safely
def evaluate_expression():
    try:
        expression = entry.get()
        if not all(char in '0123456789+-*/(). ' for char in expression):
            raise ValueError("Invalid characters used.")
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")
        entry.delete(0, tk.END)
    except Exception:
        messagebox.showerror("Error", "Invalid Expression")
        entry.delete(0, tk.END)

def button_click(char):
    entry.insert(tk.END, char)

def clear():
    entry.delete(0, tk.END)

def square():
    try:
        expression = entry.get()
        value = float(eval(expression))
        result = value ** 2
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        messagebox.showerror("Error", "Invalid input for square.")
        entry.delete(0, tk.END)

def square_root():
    try:
        expression = entry.get()
        value = float(eval(expression))
        if value < 0:
            raise ValueError("Cannot take square root of negative number.")
        result = math.sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        messagebox.showerror("Error", "Invalid input for square root.")
        entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Professional Calculator")
root.geometry("400x600")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# Style
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 16), padding=10, width=4,
                background="#3b3b3b", foreground="white")
style.map("TButton",
          background=[('active', '#505050')],
          foreground=[('active', '#00f7ff')])

# Entry field
entry = ttk.Entry(root, font=("Consolas", 22), justify="right")
entry.pack(fill="both", ipady=15, padx=10, pady=10)

# Buttons layout (balanced rows)
buttons = [
    ['C', '(', ')', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=', '√'],
    ['x²', '', '', '']
]

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

# Add buttons to the UI
for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        if char:
            if char == '=':
                btn = ttk.Button(frame, text=char, command=evaluate_expression)
            elif char == 'C':
                btn = ttk.Button(frame, text=char, command=clear)
            elif char == 'x²':
                btn = ttk.Button(frame, text=char, command=square)
            elif char == '√':
                btn = ttk.Button(frame, text=char, command=square_root)
            else:
                btn = ttk.Button(frame, text=char, command=lambda ch=char: button_click(ch))
            btn.grid(row=r, column=c, padx=5, pady=5, ipadx=5, ipady=10)

# Run app
root.mainloop()