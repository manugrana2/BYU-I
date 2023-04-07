import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter.messagebox import askyesno
import csv
import os.path
from tkinter import messagebox
import os
import webbrowser


sale_indexes = ['Product', 'Client Name', 'Unit Price', 'Units Sold', 'Date', 'Discount', 'Sale Taxes', 'Seller']

def validate_entry_number(new_value):
    return new_value.isnumeric() or new_value == ""

def validate_sale_data(sale_data):
    """This function validates the sale data.

    This function validates the sale data before adding it to the sales.csv file.

    Args:
        sale_data (array): This is an array containing the information about the sale as described in sale_indexes.

    Returns:
        bool: True if the sale data is valid, False otherwise.

    Raises:
        None

    sale_data = ['Product', 'Client Name', 'Unit Price', 'Units Sold', 'Date', 'Discount', 'Sale Taxes', 'Seller']
    """
    errors_list = []
    if not isinstance(sale_data, list):
        errors_list.append("Sale data should be a list")
    elif len(sale_data) != 1:
        errors_list.append("Sale data should contain only one sale")
    else:
        sale = sale_data[0]
        if not isinstance(sale, list):
            errors_list.append("Sale data should be a list of lists")
        elif len(sale) != 8:
            errors_list.append("Sale data should contain 8 fields")
        else:
            if not isinstance(sale[0], str) or sale[0].strip() == "":
                errors_list.append("Product Name is Empty")
            if not isinstance(sale[1], str) or sale[1].strip() == "":
                errors_list.append("Client Name is Empty")
            try:
                if not isinstance(float(sale[2]), float) or float(sale[2]) <= 0:
                    errors_list.append("Unit Price is Invalid")
            except ValueError:
                errors_list.append("Unit Price is Invalid")
            try:
                if not isinstance(int(sale[3]), int) or int(sale[3]) <= 0:
                    errors_list.append("Units Sold is Invalid")
            except ValueError:
                errors_list.append("Units Sold is Invalid")
            if not isinstance(sale[4], str) or sale[4].strip() == "":
                errors_list.append("Date is Empty")
            try:
                if not isinstance(float(sale[5]), float) or float(sale[5]) < 0:
                    errors_list.append("Discount Sold is Invalid")
            except ValueError:
                errors_list.append("Discount Sold is Invalid")
            try:
                if not isinstance(float(sale[6]), float) or float(sale[6]) < 0:
                    errors_list.append("Sale Taxes Sold is Invalid")
            except ValueError:
                errors_list.append("Sale Taxes Sold is Invalid")
            if not isinstance(sale[7], str) or sale[7].strip() == "":
                errors_list.append("Seller Sold is Empty")

    if len(errors_list) > 0:
        print(errors_list)
        return False
    else:
        return True


if __name__ == "__main__":
    # Create Tkinter window
    root = tk.Tk()
    root.title("Save Sale")
    root.minsize(600, 400)
    validation = root.register(validate_entry_number)


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
    date_entry = DateEntry(mainframe, width=12, background='darkblue', foreground='white', borderwidth=2, font=("TkDefaultFont", 16))
    date_entry.grid(row=4, column=1, sticky="ew", padx=10, pady=10)

    # Add sales discount label and input field
    discount_label = tk.Label(mainframe, text="Discount %",  font=("TkDefaultFont", 16))
    discount_label.grid(row=5, column=0, sticky="w")
    discount_entry = tk.Entry(mainframe, font=("TkDefaultFont", 16))
    discount_entry.grid(row=5, column=1, sticky="ew", padx=10, pady=10)

    # Add sales tax label and input field
    sales_tax_label = tk.Label(mainframe, text="Sale Taxes %",  font=("TkDefaultFont", 16))
    sales_tax_label.grid(row=6, column=0, sticky="w")
    sales_tax_entry = tk.Entry(mainframe, font=("TkDefaultFont", 16))
    sales_tax_entry.grid(row=6, column=1, sticky="ew", padx=10, pady=10)

    # Add seller label and input field
    seller_label = tk.Label(mainframe, text="Seller",  font=("TkDefaultFont", 16))
    seller_label.grid(row=7, column=0, sticky="w")
    seller_entry = tk.Entry(mainframe, font=("TkDefaultFont", 16))
    seller_entry.grid(row=7, column=1, sticky="ew", padx=10, pady=10)

    def clear_entries():
        product_entry.delete(0, tk.END)
        client_entry.delete(0, tk.END)
        unit_price_entry.delete(0, tk.END)
        units_entry.delete(0, tk.END)
        discount_entry.delete(0, tk.END)
        sales_tax_entry.delete(0, tk.END)
        seller_entry.delete(0, tk.END)

    # Save info when button is clicked
    def show_sales():
        # Add your code to handle the button click here
        # Specify the file name of your CSV file
        filename = 'sales.csv'

        # Get the absolute path to the CSV file
        filepath = os.path.abspath(filename)

        # Open the CSV file with the default program
        webbrowser.open(filepath)

    #Confirm to save sale
    def confirm():
        filename = 'sales.csv'
        header = ['Product', 'Client Name', 'Unit Price', 'Units Sold', 'Date', 'Discount', 'Sale Taxes', 'Seller']

        sale_info = f"Product: {product_entry.get()} \nClient's name: {client_entry.get()}"
        sale_info += f"\nUnit Price: {unit_price_entry.get()} \nUnits Sold: {units_entry.get()}"
        sale_info += f"\nDate: {date_entry.get_date()}"
        sale_info += f"\nDiscount: {discount_entry.get()}%"
        sale_info += f"\nSale Taxes: {sales_tax_entry.get()}%"
        sale_info += f"\nSeller: {seller_entry.get()}"
        sale_data = [
            [
                product_entry.get(), 
                client_entry.get(), 
                unit_price_entry.get(), 
                units_entry.get(), 
                date_entry.get_date().strftime("%m/%d/%Y"), 
                discount_entry.get(), 
                sales_tax_entry.get(), 
                seller_entry.get()
            ]
                    ]
        answer = askyesno(title='Confirmation',
            message='Are you sure you want to save this sale?\n\n'+sale_info)
        if answer:
            if validate_sale_data(sale_data):
                if os.path.isfile(filename):
                    print("Adding sale to the Sales file...")
                    with open(filename, 'a', newline="") as file:
                        csvwriter = csv.writer(file) # 2. create a csvwriter object
                        csvwriter.writerows(sale_data) # 5. write the rest of the data
                        messagebox.showinfo(message="Sale Saved", title="Congrats!")
                        clear_entries()


                else:
                    print("Creating Sales File")
                    with open(filename, 'w', newline="") as file:
                        csvwriter = csv.writer(file) # 2. create a csvwriter object
                        csvwriter.writerow(header) # 4. write the header
                        csvwriter.writerows(sale_data) # 5. write the rest of the data
                        messagebox.showinfo(message="Sale Saved", title="Congrats!")
                        clear_entries()
            else:
                messagebox.showerror("Error", "Error, you should complete all the required info before saving a sale!")

                


    # Add save button
    save_button = tk.Button(mainframe, text="Save",  font=("TkDefaultFont", 16), command=confirm)
    save_button.grid(row=7, column=2, sticky="e")

    # Get the Saved Sales File
    if os.path.isfile("sales.csv"):
        save_button = tk.Button(mainframe, text="View Previous Saved Sales",  font=("TkDefaultFont", 16), command=show_sales)
        save_button.grid(row=10, column=1, sticky="e")


    # Configure the grid and padding
    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    mainframe.grid_columnconfigure(0, weight=1)
    mainframe.grid_columnconfigure(1, weight=1)

    root.mainloop()


