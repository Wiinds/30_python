import customtkinter as ctk

class TaxCalculator:
    def __init__(self):
        #? Initialize our window 
        self.window = ctk.CTk()
        self.window.title('Tax Calculator')
        self.window.geometry('480x400')
        self.window.resizable(False, False)
        
        self.padding: dict = {'padx': 20, 'pady':10}
        #? Income label and Entry
        self.income_label = ctk.CTkLabel(self.window, text='Income:')
        self.income_label.grid(row=0, column=0, **self.padding)
        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(row=0, column=1, **self.padding)
        
        #? Tax label and Entry 
        self.tax_rate_label = ctk.CTkLabel(self.window, text='Percent:')
        self.tax_rate_label.grid(row=1, column=0, **self.padding)
        self.tax_rate_entry = ctk.CTkEntry(self.window)
        self.tax_rate_entry.grid(row=1, column=1, **self.padding)
        
        #? Result Label and Entry
        self.Result_label = ctk.CTkLabel(self.window, text='Tax:')
        self.Result_label.grid(row=2, column=0, **self.padding)
        self.Result_entry = ctk.CTkEntry(self.window)
        self.Result_entry.insert(0, '0')
        self.Result_entry.grid(row=2, column=1, **self.padding)
        
        #? Calculate Button
        self.calulate_button = ctk.CTkButton(self.window, text='Calulate', command=self.calulate_tax)
        self.calulate_button.grid(row=3, column=1, **self.padding)


    def update_result(self, text: str):
        self.Result_entry.delete(0, ctk.END)
        self.Result_entry.insert(0, text)
    
    #? logic to calucate the tax of numbers inserted into the GUI
    def calulate_tax(self):
        try:
            income: float = float(self.income_entry.get())
            tax_rate: float = float(self.tax_rate_entry.get())
            self.update_result(f'${income * (tax_rate / 100):,.2f}')
        except ValueError:
            self.update_result('Invalid Input, Provide a Number')
        
    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    tc = TaxCalculator()
    tc.run()
    
