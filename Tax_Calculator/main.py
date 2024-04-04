import customtkinter as ctk
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TaxCalculator:
    def __init__(self):
        logging.info('Initializing TaxCalculator')
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
        logging.info('Updating result display')
        self.Result_entry.delete(0, ctk.END)
        self.Result_entry.insert(0, text)
    
    #? logic to calucate the tax of numbers inserted into the GUI
    def calulate_tax(self):
        logging.info('Attempting to calculate tax')
        try:
            income: float = float(self.income_entry.get())
            tax_rate: float = float(self.tax_rate_entry.get())
            tax = income * (tax_rate / 100)
            logging.info(f'Calculated tax: ${tax:,.2f} for income: ${income:,.2f} and tax rate: {tax_rate}%')
            self.update_result(f'${tax:,.2f}')
        except ValueError:
            logging.error('Invalid input, could not calculate tax')
            self.update_result('Invalid Input, Provide a Number')
        
    def run(self):
        logging.info('Starting Tax Calculator Application')
        self.window.mainloop()
        logging.info('Exiting Tax Calculator Application')


if __name__ == '__main__':
    tc = TaxCalculator()
    tc.run()
    
