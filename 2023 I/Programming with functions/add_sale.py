import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter.messagebox import askyesno


# Create Tkinter window
root = tk.Tk()
root.title("Save Sale")
root.minsize(600, 400)

# Create canvas and scrollbar
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))
canvas.bind('<Configure>', on_configure)
root.bind('<MouseWheel>', lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), 'units'))

# Create a frame inside the canvas
mainframe = tk.Frame(canvas)
canvas.create_window((0, 0), window=mainframe, anchor='nw')

# Create input boxes inside the frame
# Add product label and input field
product_label = tk.Label(mainframe, text="Product",  font=("TkDefaultFont", 16))
product_label.grid(row=0, column=0, sticky="w")
product_entry = tk.Entry(mainframe, font=("TkDefaultFont", 16))
product_entry.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

# Add client name label and input field
client_label = tk.Label(mainframe, text="Client's Name",  font=("TkDefaultFont", 16))
client_label.grid(row=1, column=0, sticky="w")
client_entry = tk.Entry(mainframe, font=("TkDefaultFont", 16))
client_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=10)

# Add unit price label and input field
unit_price_label = tk.Label(mainframe, text="Unit Price",  font=("TkDefaultFont", 16))
unit_price_label.grid(row=2, column=0, sticky="w")
unit_price_entry = tk.Entry(mainframe, font=("TkDefaultFont", 16))
unit_price_entry.grid(row=2, column=1, sticky="ew", padx=10, pady=10)

# Add units label and input field
units_label = tk.Label(mainframe, text="Units Sold",  font=("TkDefaultFont", 16))
units_label.grid(row=3, column=0, sticky="w")
units_entry = tk.Entry(mainframe, font=("TkDefaultFont", 16))
units_entry.grid(row=3, column=1, sticky="ew", padx=10, pady=10)

# Add date label and calendar field
date_label = tk.Label(mainframe, text="Date",  font=("TkDefaultFont", 16))
date_label.grid(row=4, column=0, sticky="w")
cal = DateEntry(mainframe, width=12, background='darkblue', foreground='white', borderwidth=2, font=("TkDefaultFont", 16))
cal.grid(row=4, column=1, sticky="ew", padx=10, pady=10)

# Add sales disccount label and input field
disccount_label = tk.Label(mainframe, text="Disccount %",  font=("TkDefaultFont", 16))
disccount_label.grid(row=5, column=0, sticky="w")
disccount_entry = tk.Entry(mainframe, font=("TkDefaultFont", 16))
disccount_entry.grid(row=5, column=1, sticky="ew", padx=10, pady=10)

# Add sales tax label and input field
sales_tax_label = tk.Label(mainframe, text="Sale Taxes %",  font=("TkDefaultFont", 16))
sales_tax_label.grid(row=6, column=0, sticky="w")
sales_tax_entry = tk.Entry(mainframe, font=("TkDefaultFont", 16))
sales_tax_entry.grid(row=6, column=1, sticky="ew", padx=10, pady=10)

# Add vendedor label and input field
vendedor_label = tk.Label(mainframe, text="Seller",  font=("TkDefaultFont", 16))
vendedor_label.grid(row=7, column=0, sticky="w")
vendedor_entry = tk.Entry(mainframe, font=("TkDefaultFont", 16))
vendedor_entry.grid(row=7, column=1, sticky="ew", padx=10, pady=10)

# Save info when button is clicked
def save_button_click():
    # Add your code to handle the button click here
    print("Product ", product_entry.get(), "Saved")


# Add save button
save_button = tk.Button(mainframe, text="Save",  font=("TkDefaultFont", 16), command=save_button_click)
save_button.grid(row=7, column=2, sticky="e")



# Configure the grid and padding
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

mainframe.grid_columnconfigure(0, weight=1)
mainframe.grid_columnconfigure(1, weight=1)

# Start the main loop
root.mainloop()