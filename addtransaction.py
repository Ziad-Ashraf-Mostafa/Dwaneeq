import customtkinter
from tkcalendar import Calendar
import datetime
from arabic_reshaper import arabic_reshaper as ar
from some_classes import *
import db
import config

class Transaction(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        
        direction=config.direction
        align = config.align["add_transaction"][direction]

        self.grid_columnconfigure((0, 1), weight=1)

        self.title = customtkinter.CTkLabel(self, text=config.choosed_lang["add_transaction"], font=("Arial", 30, "bold"))
        self.title.grid(row=0, column=0, columnspan=2, pady=10, sticky="EW")

        # transaction type taken
        self.type_frame=customtkinter.CTkFrame(self, fg_color="transparent")
        self.type_frame.grid_columnconfigure((0,1), weight=1)
        self.type_frame.grid(row=1, column=0, columnspan=2)

        self.type_var = customtkinter.StringVar(self)
        self.income = customtkinter.CTkRadioButton(self.type_frame, text=config.choosed_lang["income"], fg_color="green",
                                                    value='income', variable=self.type_var, command=self.choose_type)
        self.income.grid(row=0, column=0, pady=20, sticky="E")
        self.expense = customtkinter.CTkRadioButton(self.type_frame, text=config.choosed_lang["expense"], fg_color="red",
                                                    value='expense', variable=self.type_var, command=self.choose_type)
        self.expense.grid(row=0, column=1, pady=20, sticky="W")

        # taking amount along with currency
        self.amount_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.amount_frame.grid(row=2, column=align["amount_labl"]["column"], padx=20, pady=20, sticky="EW")
        self.amount_frame.grid_columnconfigure((0,1), weight=1)

        self.amount_label = customtkinter.CTkLabel(self.amount_frame, text=config.choosed_lang["amount"])
        self.amount_label.grid(row=0, column=align["amount_labl"]["column"], padx=20, pady=10, sticky=align["amount_labl"]["sticky"])

        self.amount_entry = NumEntry(self.amount_frame, placeholder_text=config.choosed_lang["enter_amount"], width=200,
                                    quick_plus_minus=True, align_direction=config.direction)
        self.amount_entry.grid(row=0, padx=40, column=align["amount_entry"]["column"])

        self.amount_currency_menu = CurrencyMenu(self.amount_frame, width=80)
        self.amount_currency_menu.set_value(config.currency)
        self.amount_currency_menu.grid(row=0, padx=15, column=align["currency"]["column"], sticky=align["currency"]["sticky"])

        # taking the category according to the type income/expense
        self.category_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.category_frame.grid_columnconfigure((0,1,2,3), weight=1)
        self.category_frame.grid(row=3, column=0, columnspan=2, padx=20, pady=20, sticky="EW")

        self.cate_labl = customtkinter.CTkLabel(self.category_frame, text=config.choosed_lang["category"], font=("Roboto",20,"bold"))
        self.cate_labl.grid(row=0, column=0, columnspan=4, pady=10)

        self.income_categories = list(config.LANG["en"]["income_categories"].keys())
        self.expense_categories = list(config.LANG["en"]["expenses_categories"].keys())
        self.income_categories_radiobuttons = {}
        self.expense_categories_radiobuttons = {}

        self.category_var = customtkinter.StringVar(self.category_frame)

        for category in self.income_categories:
            self.category_btn = customtkinter.CTkRadioButton(self.category_frame, text=config.choosed_lang["income_categories"][category],
                                                            value=config.LANG["en"]["income_categories"][category],
                                                            variable=self.category_var, fg_color="green")
            self.income_categories_radiobuttons.update({category:self.category_btn})

        for category in self.expense_categories:
            self.category_btn = customtkinter.CTkRadioButton(self.category_frame, text=config.choosed_lang["expenses_categories"][category],
                                                            value=config.LANG["en"]["expenses_categories"][category],
                                                            variable=self.category_var, fg_color="red")
            self.expense_categories_radiobuttons.update({category:self.category_btn})

        # taking note
        self.note_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.note_frame.grid(row=4, column=align["note_labl"]["column"], padx=20, pady=10, sticky=align["note_labl"]["sticky"])

        self.note_labl = customtkinter.CTkLabel(self.note_frame, text=config.choosed_lang["add_note"])
        self.note_labl.grid(row=0, padx=20, column=align["note_labl"]["column"], sticky=align["note_labl"]["sticky"])

        self.note_text_box = customtkinter.CTkTextbox(self.note_frame, width=200, height=60)
        self.note_text_box.grid(row=0, padx=15, column=align["note_text_box"]["column"])

        # taking date
        self.date_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.date_frame.grid(row=5, column=align["date_frame"]["column"], padx=20, pady=10, sticky=align["date_frame"]["sticky"])

        self.date_labl = customtkinter.CTkLabel(self.date_frame, text=config.choosed_lang["date"])
        self.date_labl.grid(row=0, padx=10, column=align["date_labl"]["column"])

        self.date_entry = customtkinter.CTkEntry(self.date_frame)
        self.date_entry.insert(0, datetime.datetime.now().strftime(r"%Y-%m-%d"))
        self.date_entry.configure(state="disabled")
        self.date_entry.grid(row=0, column=1)

        self.open_cal_btn = customtkinter.CTkButton(self.date_frame, text=config.choosed_lang["open_cal"], command=self.open_cal)
        self.open_cal_btn.grid(row=0, column=align["open_cal_btn"]["column"])

        # save button
        self.btns_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.btns_frame.grid(row=6, pady=20, column=0, columnspan=2)

        self.save_btn = customtkinter.CTkButton(self.btns_frame, text=config.choosed_lang["save"], command=self.save_transaction)
        self.save_btn.grid(row=0, padx=10, column=0)

        self.cancel_btn = customtkinter.CTkButton(self.btns_frame, text=config.choosed_lang["cancel"], command=self.cancel)
        self.cancel_btn.grid(row=0, padx=10, column=1)


    def choose_type(self):
        for category in self.category_frame.winfo_children():
            if category == self.cate_labl:
                continue
            category.grid_remove()
        
        self.category_var.set("")

        if self.type_var.get() == "income":
            dict_to_grid = list(self.income_categories_radiobuttons.values())
            self.save_btn.configure(hover_color="green")
        elif self.type_var.get() == "expense":
            dict_to_grid = list(self.expense_categories_radiobuttons.values())
            self.save_btn.configure(hover_color="red")


        row=1; column=0
        for category in dict_to_grid:
            category.grid(row=row, column=column, padx=10, pady=10)
            if column < 3:
                column += 1
            else:
                column=0
                row += 1

    def open_cal(self):
        "open the top frame calender to choose the date"
        def pick_date():
            "get the date from the calender and put it into the date entry"
            self.date_entry.configure(state="normal")
            self.date_entry.delete(0, customtkinter.END)
            self.date_entry.insert(0, cal.get_date())
            self.date_entry.configure(state="disabled")
            self.top_frame.destroy()

        self.top_frame = customtkinter.CTkToplevel(self.date_frame, title="Date")
        self.top_frame.attributes('-topmost', True); self.top_frame.resizable(False, False)

        cal = Calendar(self.top_frame, selectmode='day', year=datetime.datetime.now().year,
                   month=datetime.datetime.now().month, day=datetime.datetime.now().day,
                   date_pattern="yyyy-mm-dd")
        cal.grid(row=0, pady=20, padx=10)

        select_btn = customtkinter.CTkButton(self.top_frame, text=config.choosed_lang["select"] ,command=pick_date)
        select_btn.grid(row=1, pady=20, padx=10)

    def cancel(self):
        self.type_var.set("")
        self.amount_entry.entry.delete(0, "end")
        self.category_var.set("")
        self.note_text_box.delete("0.0", "end")
        self.date_entry.configure(state="normal")
        self.date_entry.delete(0, "end")
        self.date_entry.insert(0, datetime.datetime.now().strftime(r"%Y-%m-%d"))
        self.date_entry.configure(state="readonly")
        self.save_btn.configure(hover_color="grey")

        for category in self.category_frame.winfo_children():
            if category == self.cate_labl:
                continue
            category.grid_remove()

        if hasattr(self, "message"):
            self.message.destroy()
            self.message = None

    def save_transaction(self):
        transaction_type = self.type_var.get()
        amount = self.amount_entry.get()
        currency = self.amount_currency_menu.get_currency()
        category = self.category_var.get()
        note = self.note_text_box.get("0.0", "end").strip()
        date = self.date_entry.get()

        show_message = ""
        if transaction_type == "":
            show_message = "transaction_type_error" 
        elif amount == "":
            show_message = "amount_error" 
        elif category == "":
            show_message = "category_error" 
        
        if show_message:
            if hasattr(self, "message") and self.message:
                self.message.configure(text=config.choosed_lang[show_message])
            else:
                self.message = customtkinter.CTkLabel(self, text=config.choosed_lang[show_message], text_color="red")
            self.message.grid(row=7, column=0, columnspan=2)
        else:
            db.add_transaction(config.get_current_user_id(), float(amount), currency, transaction_type, category, date, note)
            self.cancel()
            self.master.clear_frame("destroy")
            self.master.open_side_bar()
            self.master.open_expense()