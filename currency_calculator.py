import customtkinter as ctk
import db
import config
import data_helpers
import some_classes
import datetime

class CurrencyCalculator(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid_columnconfigure(0, weight=1)

        self.header = ctk.CTkLabel(self, text=config.choosed_lang["currency_calculator"], font=("Roboto", 22, "bold"))
        self.header.grid(row=0, column=0, pady=20)

        self.calc_frame = ctk.CTkFrame(self, border_width=2)
        self.calc_frame.grid(row=1, column=0, pady=50)

        self.currency1 = some_classes.CurrencyMenu(self.calc_frame, command=lambda value: self.convert(2))
        self.currency1.set_value("USD") if config.currency != "USD" else self.currency1.set_value("EGP")
        self.currency1.grid(row=0, column=0)

        self.reverse_btn = ctk.CTkButton(self.calc_frame, text="↔", font=("Arial", 30, "bold"), command=self.reverse_currency)
        self.reverse_btn.grid(row=0, column=1, padx=10)

        self.currency2 = some_classes.CurrencyMenu(self.calc_frame, command=lambda value: self.convert(1))
        self.currency2.set_value(config.currency)
        self.currency2.grid(row=0, column=2)
        

        self.entry1 = some_classes.NumEntry(self.calc_frame, quick_plus_minus=False)
        self.entry1.bind("<KeyRelease>", lambda event: self.convert(1))
        self.entry1.grid(row=1, column=0, pady=15, padx=10)

        self.entry2 = some_classes.NumEntry(self.calc_frame, quick_plus_minus=False)
        self.entry2.bind("<KeyRelease>", lambda event: self.convert(2))
        self.entry2.grid(row=1, column=2, pady=15, padx=10)




        update_date = db.get_update_date()

        if config.direction == "rtl":
            column_one = 2
            column_three = 0
        else:
            column_one = 0
            column_three = 2

        update_date_frame = ctk.CTkFrame(self)
        update_date_frame.grid(row=2, column=0, pady=10)

        color_ball = ctk.CTkLabel(update_date_frame, text="•", font=("Arial", 35, 'bold'))
        color_ball.grid(row=0, column=column_one, padx=5)

        update_date_label = ctk.CTkLabel(update_date_frame, text=config.choosed_lang["update_date_label"],  font=("Arial", 18))
        update_date_label.grid(row=0, column=1, padx=5)

        date = ctk.CTkLabel(update_date_frame, text="  "+update_date+"  ", font=("Arial", 18, "italic"))
        date.grid(row=0, column=column_three)

        
        if update_date == datetime.datetime.now().strftime(r"%Y-%m-%d"):
            color_ball.configure(text_color="green")
            updated_note = ctk.CTkLabel(update_date_frame, text=" "+config.choosed_lang["updated"]+" ", font=("Arial", 14, "italic"))
            updated_note.grid(row=1, column=0, columnspan=3)
        else:
            color_ball.configure(text_color="red")
            update_btn = ctk.CTkButton(update_date_frame, text=config.choosed_lang["update"], command=self.master.update_currencies)
            update_btn.grid(row=1, column=0, columnspan=3)




        self.rate_show_frame = ctk.CTkFrame(self, border_width=2)
        self.rate_show_frame.grid(row=3, pady=10)

        currencies = config.LANG["en"]["currency_list"]

        row=0
        for currency in currencies:
            curr = ctk.CTkLabel(self.rate_show_frame, text=config.choosed_lang[currency], font=("Roboto", 18, 'bold'))
            curr.grid(row=row, column=0, padx=10, pady=5)

            separator = ctk.CTkLabel(self.rate_show_frame, text="  ▬▬▬▬► ", font=("Arial", 17))
            separator.grid(row=row, column=1, padx=10)

            amount = ctk.CTkLabel(self.rate_show_frame,  font=("Roboto", 18),
                                    text=round(data_helpers.from_to(1.0, currency, config.currency), 2))
            amount.grid(row=row, column=2, padx=5)

            main_currency = ctk.CTkLabel(self.rate_show_frame, text=config.choosed_lang[config.currency]+" ",  font=("Roboto", 18, 'italic'))
            main_currency.grid(row=row, column=3, padx=5)

            row += 1


    def reverse_currency(self):
        currency1 = self.currency1.get_currency()
        currency2 = self.currency2.get_currency()

        self.currency1.set_value(currency2)
        self.currency2.set_value(currency1)

        amount1 = self.entry1.get()
        amount2 = self.entry2.get()

        self.entry1.clear()
        self.entry1.insert(amount2)

        self.entry2.clear()
        self.entry2.insert(amount1)

    def convert(self, curr: int):
        currency1 = self.currency1.get_currency()
        currency2 = self.currency2.get_currency()

        if curr == 1:
            amount1 = self.entry1.get()

            self.entry2.clear()
            if amount1 == "" or amount1 == ".": return
            self.entry2.insert(data_helpers.from_to(float(amount1), currency1, currency2))

        elif curr == 2:
            amount2 = self.entry2.get()

            self.entry1.clear()
            if amount2 == "" or amount2 == ".": return
            self.entry1.insert(data_helpers.from_to(float(amount2), currency2, currency1))

