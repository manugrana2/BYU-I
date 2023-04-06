import tkinter as tk

class MainView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        self.label = tk.Label(self, text="Welcome to the Main View!")
        self.label.pack()
        
        self.button1 = tk.Button(self, text="Go to View 1", command=self.show_view1)
        self.button1.pack()
        
        self.button2 = tk.Button(self, text="Go to View 2", command=self.show_view2)
        self.button2.pack()
        
    def show_view1(self):
        view1 = None
        if view1 is None:
            view1 = View1(root)
        self.pack_forget()
        view1.pack()
        
    def show_view2(self):
        view2 = None
        if view2 is None:
            view2 = View2(root)
        self.pack_forget()
        view2.pack()
        
class View1(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        self.label = tk.Label(self, text="This is View 1!")
        self.label.pack()
        
        self.button = tk.Button(self, text="Go back to Main View", command=self.show_main_view)
        self.button.pack()
        
    def show_main_view(self):
        self.pack_forget()
        main_view.pack()
        
class View2(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        self.label = tk.Label(self, text="This is View 2!")
        self.label.pack()
        
        self.button = tk.Button(self, text="Go back to Main View", command=self.show_main_view)
        self.button.pack()
        
    def show_main_view(self):
        self.pack_forget()
        main_view.pack()
        
root = tk.Tk()
main_view = MainView(root)
view1 = None
view2 = None
root.mainloop()
