import customtkinter
from tkinter import ttk
import datetime
from arabic_reshaper import arabic_reshaper as ar
import db
import config; import some_classes


class SearchAndFilterFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.search_entry = customtkinter.CTkEntry(self, width=400, placeholder_text=config.choosed_lang["search"])
        self.search_entry.grid(row=0, column=0, padx=20, pady=10)

        self.trans_type_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.trans_type_frame.grid(row=0, column=1, padx=10)
        self.type_label = customtkinter.CTkLabel(self.trans_type_frame, text=config.choosed_lang["transaction_type_labl"])
        self.type_label.grid(row=0, column=0)
        self.transaction_type_menu = customtkinter.CTkOptionMenu(self.trans_type_frame, values=config.choosed_lang["transaction_type_menu"], width=80,
                                                                command=self.show_category_menu)
        self.transaction_type_menu.grid(row=0, column=1)

        self.currency_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.currency_frame.grid(row=0, column=3, padx=10)
        self.currency_label = customtkinter.CTkLabel(self.currency_frame, text=config.choosed_lang["currency_list_labl"])
        self.currency_label.grid(row=0, column=0)
        self.currency_menu = some_classes.CurrencyMenu(self.currency_frame, True)
        # self.currency_menu = customtkinter.CTkOptionMenu(self.currency_frame, width=80,
        #                                                     values=[config.choosed_lang["all"], *config.choosed_lang["currency_list"]])
        self.currency_menu.grid(row=0, column=1)

        self.date_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.date_frame.grid(row=1, column=1, columnspan=3, sticky="E")
        self.date_from_entry = customtkinter.CTkEntry(self.date_frame, width=90); self.date_from_entry.configure(state="readonly")
        self.date_from_entry.grid(row=0, column=0, padx=10, pady=10)

        self.date_from = customtkinter.CTkButton(self.date_frame, text=config.choosed_lang["date_from"],  width=50,
                                                    command=lambda: self.open_cal(self.date_from_entry))
        self.date_from.grid(row=0, column=1)

        self.date_to_entry = customtkinter.CTkEntry(self.date_frame, width=90)
        self.date_to_entry.insert(0, datetime.datetime.now().strftime(r"%Y-%m-%d")); self.date_to_entry.configure(state="readonly")
        self.date_to_entry.grid(row=0, column=2, padx=10, pady=10)
        
        self.date_to = customtkinter.CTkButton(self.date_frame, text=config.choosed_lang["date_to"], width=50,
                                                    command=lambda: self.open_cal(self.date_to_entry))
        self.date_to.grid(row=0, column=3)

        self.search_btn = customtkinter.CTkButton(self, width=100, text=config.choosed_lang["search_btn"], command=self.search)
        self.search_btn.grid(row=1, column=0, padx=20)

        self.delete_btn = customtkinter.CTkButton(self, width=100, text=config.choosed_lang["delete_selected"], command=self.delete_selected)
        self.delete_btn.grid(row=1, column=0, padx=50, sticky="E")


    def show_category_menu(self, value):
        if hasattr(self, "category_menu"):
            if self.category_frame != None:
                self.category_frame.destroy()
                self.category_frame = None

        if self.get_type() == "all":
            return
        else:
            self.category_frame = customtkinter.CTkFrame(self, fg_color="transparent")
            self.category_frame.grid(row=0, column=2)
            self.category_label = customtkinter.CTkLabel(self.category_frame, text=config.choosed_lang["category_list_labl"])
            self.category_label.grid(row=0, column=0)

            self.category_menu = some_classes.CategoryMenu(self.category_frame, add_all=True, type=self.get_type())
            self.category_menu.grid(row=0, column=1)

    def get_type(self) -> str:
        "get the english velue of the transaction_type option menu even if the appearing values are arabic to be dealed with in the logic"
        if config.lang_name == "en":
            return self.transaction_type_menu.get()

        transaction_types_en = config.LANG["en"]["transaction_type_menu"]
        transaction_types_ar = config.LANG["ar"]["transaction_type_menu"]
        index = transaction_types_ar.index(self.transaction_type_menu.get())
        return transaction_types_en[index]

    def get_category(self):
        "get the english velue of the category option menu even if the appearing values are arabic to be dealed with in the logic"
        if self.get_type() == "all":
            return ""

        return self.category_menu.get_category()

    def get_currency(self):
        return self.currency_menu.get_currency()

    def search(self):
        self.master.fill_table(filter=True)

    def delete_selected(self):
        tree = self.master.tree
        selected_ids = tree.selection()
        db.delete_transactions(config.get_current_user_id(), selected_ids)

        self.master.master.clear_frame("destroy")
        self.master.master.open_side_bar()
        self.master.master.open_history()

    def open_cal(self, date_entry):
        "open the top frame calender to choose the date"
        cal = some_classes.DateCalender(self, date_entry)

class History(customtkinter.CTkFrame):
    def __init__(self, master, search_bar: bool=True, limit: int=None):
        super().__init__(master)
        self.master = master
        self.limit = limit

        if search_bar:
            self.topbar = SearchAndFilterFrame(self)
            self.topbar.pack(side="top", fill="x", expand=False)

        self.body = customtkinter.CTkFrame(self)
        self.body.pack(fill="both", expand=True)

        columns=["type", "category", "amount", "currency", "date", "note"]
        headings=config.choosed_lang["table_headings"]
        if config.lang_name == "ar":
            columns = columns[::-1]
            headings = headings[::-1]

        style = ttk.Style()
        style.theme_use('default')

        # Treeview 
        style.configure("Treeview",
            background="#2a2d2e",
            foreground="white",
            rowheight=30,
            fieldbackground="#343638",
            bordercolor="#343638",
            borderwidth=0)

        style.map("Treeview",
            background=[('selected', '#22559b')],
            foreground=[('disabled', "white")])


        style.configure("Treeview.Heading",
            background="#565b5e",
            foreground="white",
            relief="flat",)

        style.map("Treeview.Heading",
            background=[('active', '#3484F0')])



        self.tree = ttk.Treeview(self.body, columns=columns)
        self.tree.column("#0", width=0, stretch=False)
        self.tree.heading("#0", text="")

        for i, col in enumerate(self.tree["columns"]):
            self.tree.column(col, width=80, anchor="center")
            self.tree.heading(col, text=headings[i])

        self.tree.tag_configure('evenrow', background="grey10")
        self.tree.tag_configure('oddrow', background="grey15")
        
        self.fill_table()

        if not limit:
            v_scroll = ttk.Scrollbar(self.body, orient='vertical')
            v_scroll.pack(side="right", fill="y")
        else:
            self.tree['height'] = min(5, len(self.tree.get_children()))

        self.tree.pack(fill="both", expand=True)



    def fill_table(self, filter: bool=False):
        transactions = self.data_for_show(filter)

        for row in self.tree.get_children():
            self.tree.delete(row)

        tag = "oddrow"
        for transaction in transactions:
            if config.lang_name == "ar":
                self.tree.insert("", "end", iid=transaction[-1], values=transaction[:6], tags=(tag,))
            else:
                self.tree.insert("", "end", iid=transaction[0], values=transaction[2:], tags=(tag,))
            
            if tag == "oddrow":
                tag = "evenrow"
            else:
                tag = "oddrow"

    def data_for_show(self, filter: bool):
        if filter:
            transactions = db.get_transactions(config.get_current_user_id(),
                                                self.topbar.search_entry.get(), self.topbar.get_type(), self.topbar.get_category(),
                                                self.topbar.get_currency(), self.topbar.date_from_entry.get(), self.topbar.date_to_entry.get())
        else:
            transactions = db.get_transactions(config.get_current_user_id(), limit=self.limit)
        
        if config.direction == 'rtl':
            transactios_as_lists = []
            for transaction in transactions:
                transactios_as_lists.append([*transaction])

            for transaction in transactios_as_lists:
                try:
                    transaction[3] = config.choosed_lang[transaction[2]+"_categories"][transaction[3].lower()]
                except:
                    transaction[3] = config.choosed_lang[transaction[2]+"s_categories"][transaction[3].lower()]

                transaction[2] = config.choosed_lang[transaction[2]]
                transaction[5] = config.choosed_lang[transaction[5]]

                transactions = []
                for transaction in transactios_as_lists:
                    transactions.append(tuple(transaction[::-1]))

        return transactions