from __future__ import annotations
from arabic_reshaper import arabic_reshaper as ar
import os, sys

# Light mode theme colors
LIGHT_THEME = {
    "sidebar_bg": "#f0f0f5",
    "main_bg": "grey90",
    "login_bg": "grey87",
    "text": "#222222",
    "heading": "#0a0a0a",
    "sidebar_btn": "grey20",
    "sidebar_btn_active": "#a3c9ff",
    "accent": "#3b82f6",
    "entry_bg": "#ffffff",
    "entry_fg": "#000000",
    "button_text": "#ffffff",
    "border": "#dcdcdc"
}

Light_Blue = {
    "bg": "#f0f4ff",
    "fg": "#1c1c1c",
    "login_bg": "grey87",
    "sidebar_bg": "#e1ecff",
    "sidebar_btn": "#2196F3",
    "sidebar_btn_active": "#a3c9ff",
    "accent": "#3b82f6",
    "entry_bg": "#ffffff",
    "entry_fg": "#000000"
}

Light_Yellow = {
    "bg": "#fffdf0",
    "fg": "#1c1c1c",
    "login_bg": "grey87",
    "sidebar_bg": "#fff8cc",
    "sidebar_btn": "#FFD54F",
    "sidebar_btn_active": "#ffe066",
    "accent": "#facc15",
    "entry_bg": "#ffffff",
    "entry_fg": "#000000"
}

Light_Green = {
    "bg": "#f0fff5",
    "fg": "#1c1c1c",
    "login_bg": "grey87",
    "sidebar_bg": "#d1fae5",
    "sidebar_btn": "#4CAF50",
    "sidebar_btn_active": "#6ee7b7",
    "accent": "#10b981",
    "entry_bg": "#ffffff",
    "entry_fg": "#000000"
}

Light_Red = {
    "bg": "#fff5f5",
    "fg": "#1c1c1c",
    "login_bg": "grey87",
    "sidebar_bg": "#ffe4e6",
    "sidebar_btn": "#e63946",
    "sidebar_btn_active": "#fca5a5",
    "accent": "#ef4444",
    "entry_bg": "#ffffff",
    "entry_fg": "#000000"
}

Light_Blue = {
    "bg": "#f0f4ff",
    "fg": "#1c1c1c",
    "login_bg": "grey87",
    "sidebar_bg": "#e1ecff",
    "sidebar_btn": "#cce0ff",
    "sidebar_btn_active": "#a3c9ff",
    "accent": "#3b82f6",
    "entry_bg": "#ffffff",
    "entry_fg": "#000000"
}

Light_Purple = {
    "bg": "#f6f0ff",              # general background
    "fg": "#1d1426",              # general text
    "login_bg": "#efe3fc",
    "sidebar_bg": "#e4d4f7",
    "sidebar_btn": "#B388EB",
    "sidebar_btn_active": "#be9ae8",
    "accent": "#a855f7",
    "entry_bg": "#ffffff",
    "entry_fg": "#000000"
}

Light_Black = {
    "bg": "#f2f2f2",
    "fg": "#0d0d0d",
    "login_bg": "#e8e8e8",
    "sidebar_bg": "#d4d4d4",
    "sidebar_btn": "#333333",
    "sidebar_btn_active": "#a5a5a5",
    "accent": "#333333",
    "entry_bg": "#ffffff",
    "entry_fg": "#000000"
}

Light_Grey = {
    "bg": "#f7f7f7",
    "fg": "#1e1e1e",
    "login_bg": "#eaeaea",
    "sidebar_bg": "#dedede",
    "sidebar_btn": "#B0B0B0",
    "sidebar_btn_active": "#b8b8b8",
    "accent": "#8a8a8a",
    "entry_bg": "#ffffff",
    "entry_fg": "#000000"
}

# Dark mode theme colors
DARK_THEME = {
    "sidebar_bg": "#1e1e2f",
    "main_bg": "#121222",
    "login_bg": "#2a2a3b",
    "text": "#f5f5f5",
    "heading": "#ffffff",
    "button_bg": "#1a73e8",
    "button_text": "#ffffff",
    "border": "#444444"
}

Dark_Blue = {
    "bg": "#0f172a",
    "fg": "#e0f2fe",
    "login_bg": "#2a2a3b",
    "sidebar_bg": "#1e293b",
    "sidebar_btn": "#1565C0",
    "sidebar_btn_active": "#3b82f6",
    "accent": "#3b82f6",
    "entry_bg": "#1e293b",
    "entry_fg": "#ffffff"
}

Dark_Yellow = {
    "bg": "#1f1c0f",
    "fg": "#fff7cd",
    "login_bg": "#2a2a3b",
    "sidebar_bg": "#2c260f",
    "sidebar_btn": "#D4AC3F",
    "sidebar_btn_active": "#facc15",
    "accent": "#facc15",
    "entry_bg": "#2c260f",
    "entry_fg": "#ffffff"
}

Dark_Green = {
    "bg": "#0f2e1f",
    "fg": "#d1fae5",
    "login_bg": "#2a2a3b",
    "sidebar_bg": "#134e4a",
    "sidebar_btn": "#2e7d32",
    "sidebar_btn_active": "#10b981",
    "accent": "#10b981",
    "entry_bg": "#1f3f32",
    "entry_fg": "#ffffff"
}

Dark_Red = {
    "bg": "#2c0f0f",                              # general background
    "fg": "#fecaca",                              # general text
    "login_bg": "#3b1a1a",                        # login screen background
    "sidebar_bg": "#4b1e1e",                      # sidebar background
    "sidebar_btn": "#800000",                     # sidebar button normal
    "sidebar_btn_active": "#ef4444",              # sidebar button active
    "accent": "#ef4444",                          # main accent
    "entry_bg": "#3a1a1a",                        # entry background
    "entry_fg": "#ffffff",                        # entry text
}

Dark_Purple = {
    "bg": "#1e102b",
    "fg": "#f4f0fa",
    "login_bg": "#2e1c45",
    "sidebar_bg": "#321b4f",
    "sidebar_btn": "#7B61A8",
    "sidebar_btn_active": "#6d30a3",
    "accent": "#c084fc",
    "entry_bg": "#2a1e3d",
    "entry_fg": "#ffffff"
}

Dark_Black = {
    "bg": "#0d0d0d",
    "fg": "#f0f0f0",
    "login_bg": "#1a1a1a",
    "sidebar_bg": "#222222",
    "sidebar_btn": "#2D2D2D",
    "sidebar_btn_active": "#444444",
    "accent": "#ffffff",
    "entry_bg": "#1c1c1c",
    "entry_fg": "#ffffff"
}

Dark_Grey = {
    "bg": "#1f1f1f",
    "fg": "#f0f0f0",
    "login_bg": "#2c2c2c",
    "sidebar_bg": "#3a3a3a",
    "sidebar_btn": "#444444",
    "sidebar_btn_active": "#626262",
    "accent": "#b0b0b0",
    "entry_bg": "#2e2e2e",
    "entry_fg": "#ffffff"
}

# Language

LANG = {
    "en": {
        "username" : "Username", 
        "password" : "Password",
        "login_label" : "Log In",
        "login_button" : "Log in",
        "show_password_checkbox" : "show password",
        "invalid_user_note" : "User name or Password is not True!",
        "signup_link_note" : "Don't have an account? Sign Up.",
        "signup_label" : "Sign Up",
        "signup_button" : "sign up",
        "confirm_password" : "Confirm Password",
        "reserved_username_note" : "This user name is already used, try another one",
        "wrong_password_confirmation_note" : "please, rewrite confirmation of the password corrctly",
        "special_character_note" : "Password can not contain special characters or white spaces",
        "login_link_note" : "You already have an account? Log in",
        "non_english_characters" : "Only english letters, numbers  and other some characters are available",
        "empty_password" : "Password cannot be empty",
        "Home" : "Home",
        "add_transaction" : "Add Transaction",
        "History" : "History",
        "Budget" : "Budget",
        "Stats" : "Stats",
        "Settings" : "Settings",
        "Appearance_mode" : "Appearance mode",
        "light_mode" : "Light mode",
        "dark_mode" : "Dark mode",
        "theme" : "Theme",
        "blue" : "Blue",
        "yellow" : "Yellow",
        "green" : "Green",
        "red" : "Red",
        "purple" : "Purple",
        "grey" : "Grey",
        "black" : "Black",
        "remember_login" : "Remember my login",
        "change_password" : "change password",
        "write_old_password" : "Enter the current password",
        "cancel" : "Cancel",
        "continue" : "Continue",
        "save" : "Save",
        "old_password_note" : "Password is incorrect",
        "enter_the_new_password" : "enter the new password",
        "confirm_changing_message" : "Are you sure to change the Password?",
        "yes" : "yes",
        "password_changed_successfully" : "Password has been changed successfully!",
        "lang" : "Language",
        "account" : "Account",
        "log_out" : "Log out",
        "delete_account" : "Delete account",
        "confirm_deleting_message" : "Are you sure you want to delete your account permenantly?",
        "delete" : "Delete",
        "income" : "Income",
        "expense" : "Expense",
        "amount" : "Amount:",
        "enter_amount" : "Enter the amount",
        "category" : "Category",
        "currency_list" : ["EGP", "SAR", "AED", "USD", "EUR", "GBP"],
        "EGP" : "EGP",
        "SAR" : "SAR",
        "AED" : "AED",
        "USD" : "USD",
        "EUR" : "EUR",
        "GBP" : "GBP",

        "symbols" : {
            "EGP" : "EGP",
            "SAR" : "SAR",
            "AED" : "AED",
            "USD" : "USD",
            "EUR" : "EUR",
            "GBP" : "GBP",
        },

        "income_categories" : {
            "bocket money" : "Bocket Money",
            "salary": "Salary",
            "freelance": "Freelance",
            "business": "Business",
            "investment": "Investment",
            "rental": "Rental",
            "gift": "Gift",
            "loan": "Loan",
            "scholarship": "Scholarship",
            "refund": "Refund",
            "other": "Other",
        },
        "expenses_categories" : {
            "food": "Food",
            "transportations": "Transportations",
            "housing": "Housing",
            "utilities": "Utilities",
            "health": "Health",
            "education": "Education",
            "entertainment": "Entertainment",
            "shopping": "Shopping",
            "subscriptions": "Subscriptions",
            "debts": "Debts",
            "donations": "Donations",
            "travel": "Travel",
            "personal": "Personal",
            "pets": "Pets",
            "other": "Other"
        },

        "add_note" : "Notes:",
        "date" : "Date:",
        "open_cal" : "choose date",
        "transaction_type_error" : "transaction type should be determined",
        "amount_error" : "you did not enter an amount",
        "category_error" : "category should be selected",
        "search" : "Search in notes...",
        "transaction_type_menu" : ["all", "income", "expense"],
        "date_from" : "Date from",
        "date_to" : "Date to",
        "select" : "Select",
        "transaction_type_labl" : "Transaction type: ",
        "category_list_labl" : "Category: ",
        "currency_list_labl" : "Currency: ",
        "table_headings" : ["Type", "Category", "Amount", "Currency", "Date", "Notes"],
        "all" : "all",
        "search_btn" : "Search",
        "retry" : "Retry",
        "total_budget" : "Total budget for expenses: ",
        "enter_total_budget" : "Targeted expenses",
        "choose_budget_currency" : "Currency",
        "savings" : "Savings amount: ",
        "apply_for_coming_months" : "Auto Apply\nfor coming months",
        "add_budget_labl" : "Plan your budget for this month!",
        "add_budget" : "Add Budget",
        "add_category" : "Add Category",
        "plan_detail_expenses" : "Plan your expenses details",
        "save_budget_note_set_two_categories" : "You can not set a category more than one time",
        "save_budget_note_category_not_specified": "You forgot to specify a category you added, if not needed you can delete it",
        "save_budget_note_total_budget_not_set" : "You didn't set the total budget amount",
        "save_budget_note_savings_budget_not_set" : "You didn't set savings amount",
        "budget_heading" : "Your budget for this month!",
        "budget_over_view" : " - Budget Overview",
        "spent_so_far" : "Spent so far: ",
        "remaining" : "Remaining: ",
        "check_connection_message" : "\tConnection error, check your network\nthe currencies rates used in the app were not updated\nthe lastest updated values will be used",
        "api_responce_error_message" : "error hapened while getting currencies rate\nfrom the source, the lastest updated values will be used\nmay be your computer date is not true\nIf continued contact the app support",
        "unkown_error_message" : "Unkown error happened while updating currencies rates\nthe lastest updated values will be used",
        "not_consistant_user" : "It has been so long since the last time you visited us :(\n'catching your flying money grows your savings'\n~Elmokhber Eleqtisady\nplease not: if you have auto updating budget\nit was cancelled, make sure to plan your budget!",
        "category_budget_overview_label" : "Category Budgets",
        "category_budget_not_set_note" : "You did not set any category budget yet!",
        "set_budget" : "Set Budget",
        "edit_budget" : "Edit Budget",
        "statistics" : "Your Statistics!",
        "total_income" : "Total Income",
        "total_expense" : "Total Expense",
        "net_balance" : "Net Balance",
        "bar_title" : "Your incomes expenses over monthes",
        "months" : "Monthes",
        "piechart_categories_title" : "Expenses ratios for the month",
        "clear" : "Clear",
        "delete_selected" : "Delete Selected",
        "current_month_balance" : "Your Balance for Current month",
        "remaining_budget" : "Remaining in your Budget",
        "no_expense_yet" : "you didn't spent on any thing yet \nin the current month",
        "not_budget_set" : "No budget yet",
        "categories_expenses_current_month" : "Categories expenses for the current month",
        "recent_transactions" : "Recent Transactions",
        "view_all" : "View all",
        "main_currency_across_app" : "Main currency across the app",
        "currency_calculator" : "Currency calculator",
        "update_date_label" : "Currencies rates update date",
        "updated" : "Updated",
        "update" : "Update",
        "not_set" : "Not Set",




    },
    "ar": {
        "username" : ar.reshape("اسم المستخدم"),
        "password" : ar.reshape("كلمة المرور"),
        "login_label" : ar.reshape("تسجيل الدخول"),
        "login_button" : ar.reshape("تسجيل الدخول"),
        "show_password_checkbox" : ar.reshape("اظهر كلمة المرور"),
        "invalid_user_note" : ar.reshape("اسم المستخدم غير موجود أو كلمة المرور غير صحيحة"),
        "signup_link_note" : ".أليس لديك حسابٌ بعد ؟  إنشاء حساب",
        "signup_label" : ar.reshape("إنشاء حساب"),
        "signup_button" : ar.reshape("إنشاء حساب"),
        "confirm_password" : ar.reshape("تأكيد كلمة المرور"),
        "reserved_username_note" : ar.reshape("اسم المستخدم الذي ادخلته مستخدم بالفعل, جرب اسم مستحدم آخر"),
        "wrong_password_confirmation_note" : ar.reshape("رجاءً تأكد من كتابة تأكيد كلمة المرور بشكل صحيح"),
        "special_character_note" : ar.reshape("كلمة المرور لا يجب أن تحتوي على مسافات أو علامات مميزة"),
        "login_link_note" : "لديك حساب بالفعل ؟  تسجيل الدخول.",
        "non_english_characters" : ar.reshape("فقط الحروف الإنجليزية والأرقام وبعض العلامات مسموح بها في كلمة المرور"),
        "empty_password" : ar.reshape("لا يمكن ترك كلمة المرور فارغة"),
        "Home" : ar.reshape("الصفحة الرئيسية"),
        "add_transaction" : ar.reshape("إضافة عملية"),
        "History" : ar.reshape("السجل"),
        "Budget" : ar.reshape("الميزانية"),
        "Stats" : ar.reshape("إحصائيات"),
        "Settings" : ar.reshape("الإعدادات"),
        "Appearance_mode" : ar.reshape("المظهر"),
        "light_mode" : ar.reshape("فاتح"),
        "dark_mode" : ar.reshape("داكن"),
        "theme" : ar.reshape("الثيم"),
        "blue" : ar.reshape("أزرق"),
        "yellow" : ar.reshape("أصفر"),
        "green" : ar.reshape("أخضر"),
        "red" : ar.reshape("أحمر"),
        "purple" : ar.reshape("بنفسجي"),
        "grey" : ar.reshape("رمادي"),
        "black" : ar.reshape("أسود"),
        "remember_login" : ar.reshape("تذكر حسابي"),
        "change_password" : ar.reshape("تغيير كلمة المرور"),
        "write_old_password" : ar.reshape("أدخل كلمة المرور الحالية"),
        "cancel" : ar.reshape("إلغاء"),
        "continue" : ar.reshape("استمرار"),
        "save" : ar.reshape("حفظ"),
        "old_password_note" : ar.reshape("كلمة المرور غير صحيحة"),
        "enter_the_new_password" : ar.reshape("أدخل كلمة المرور الجديدة"),
        "confirm_changing_message" : ar.reshape("هل أنت متأكد من تغيير كلمة المرور ؟"),
        "yes" : ar.reshape("نعم"),
        "password_changed_successfully" : ar.reshape("تم تغيير كلمة المرور بنجاح!"),
        "lang" : ar.reshape("اللغة"),
        "account" : "الحــسـاب", 
        "log_out" : ar.reshape("تسجيل الخروج"),
        "delete_account" : ar.reshape("حذف الحساب"),
        "confirm_deleting_message" : ar.reshape("هل أنت متأكد من حذف حسابك نهائيا ؟"),
        "delete" : ar.reshape("احذف"),
        "income" : ar.reshape("دخل"),
        "expense" : ar.reshape("نفقات"),
        "amount" : ar.reshape("المبلغ:"),
        "enter_amount" : ar.reshape("أدخل المبلغ"),
        "category" : ar.reshape("البند"),
        "currency_list" : [ar.reshape("جنيه مصري"),ar.reshape("ريال سعودي"),ar.reshape("درهم إماراتي"),ar.reshape("دولار أمريكي"),
                            ar.reshape("يورو"),ar.reshape("جنيه بريطاني")],
        "EGP" : ar.reshape("جنيه مصري"),
        "SAR" : ar.reshape("ريال سعودي"),
        "AED" : ar.reshape("درهم إماراتي"),
        "USD" : ar.reshape("دولار أمريكي"),
        "EUR" : ar.reshape("يورو"),
        "GBP" : ar.reshape("جنيه بريطاني"),
        
        "symbols" : {
            "EGP" : ar.reshape("ج.م"),
            "SAR" : ar.reshape("ر.س"),
            "AED" : ar.reshape("د.إ"),
            "USD" : ar.reshape("د.أ"),
            "EUR" : ar.reshape("يورو"),
            "GBP" : ar.reshape("ج.ب")
        },


        "income_categories" : {
            "bocket money" : ar.reshape("مصروف"),
            "salary": ar.reshape("راتب"),
            "freelance": ar.reshape("عمل حر"),
            "business": ar.reshape("أعمال خاصة"),
            "investment": ar.reshape("استثمارات"),
            "rental": ar.reshape("إيجار"),
            "gift": ar.reshape("هدية"),
            "loan": ar.reshape("قرض"),
            "scholarship": ar.reshape("منحة دراسية"),
            "refund": ar.reshape("استرداد"),
            "other": ar.reshape("أخرى")
        },
        "expenses_categories" : {
            "food": ar.reshape("طعام"),
            "transportations": ar.reshape("المواصلات"),
            "housing": ar.reshape("السكن"),
            "utilities": ar.reshape("فواتير وخدمات"),
            "health": ar.reshape("الصحة"),
            "education": ar.reshape("التعليم"),
            "entertainment": ar.reshape("الترفيه"),
            "shopping": ar.reshape("تسوق"),
            "subscriptions": ar.reshape("الاشتراكات"),
            "debts": ar.reshape("الديون"),
            "donations": ar.reshape("التبرعات"),
            "travel": ar.reshape("السفر"),
            "personal": ar.reshape("شخصي"),
            "pets": ar.reshape("الحيوانات الأليفة"),
            "other": ar.reshape("أخرى")
        },

        "add_note" : ar.reshape("ملاحظات:"),
        "date" : ar.reshape("التاريخ:"),
        "open_cal" : ar.reshape("اختر التاريخ"),
        "transaction_type_error" : ar.reshape("يجب تحديد نوع العملية"),
        "amount_error" : ar.reshape("أنت لم تدخل المبلغ"),
        "category_error" : ar.reshape("يجب تحديد بند المعاملة"),
        "search" : ar.reshape("ابحث في الملاحظات..."),
        "transaction_type_menu" : [ar.reshape("الكل"), ar.reshape("دخل"), ar.reshape("نفقات")],
        "date_from" : ar.reshape("التاريخ من"),
        "date_to" : ar.reshape("التاريخ إلى"),
        "select" : ar.reshape("اختر"),
        "transaction_type_labl" : ar.reshape(" :نوع العملية"),
        "category_list_labl" : ar.reshape(" :البند"),
        "currency_list_labl" : ar.reshape(" :العملة"),
        "table_headings" : ["النوع", "البند", "المبلغ", "العملة", "التاريخ", "ملاحظات"],
        "all" : ar.reshape("الكل"),
        "search_btn" : "ابحث",
        "retry" : ar.reshape("إعادة المحاولة"),
        "total_budget" : ar.reshape("الميزانية الكلية للمصروفات: "),
        "enter_total_budget" : ar.reshape("ادخل المصروفات المستهدفة"),
        "choose_budget_currency" : ar.reshape("العملة"),
        "savings" : ar.reshape("قيمة المدخر: "),
        "apply_for_coming_months" : ar.reshape("للأشهر القادمة\nطبق تلقائيا"),
        "add_budget_labl" : ar.reshape("خطط ميزانيتك لهذا الشهر!"),
        "add_budget" : ar.reshape("أضف ميزانية"),
        "add_category" : ar.reshape("أضف بندا"),
        "plan_detail_expenses" : ar.reshape("خطط تفاصيل نفقاتك"),
        "save_budget_note_set_two_categories" : ar.reshape("لا يمكن تعيين بند أكثر من مرة"),
        "save_budget_note_category_not_specified": ar.reshape("لقد نسيت أن تحدد قيمة لبند اخترته، إن لم ترده يمكن حذفه"),
        "save_budget_note_total_budget_not_set" : ar.reshape("أنت لم تحدد قيمة الميزانية"),
        "save_budget_note_savings_budget_not_set" : ar.reshape("أنت لم تحدد قيمة المدخر"),
        "budget_heading" : ar.reshape("ميزانيتك لهذا الشهر!"),
        "budget_over_view" : " - نظرة عامة على الميزانية",
        "spent_so_far" :" :النفقات حتى الآن",
        "remaining" : ar.reshape("المتبقي: "),
        "check_connection_message" : ar.reshape("سيتم استخدام آخر تحديث للعملات\nلم يتم تحديث قيمة العملات\nمشكلة في الاتصال، تأكد من شبكة الإنترنت"),
        "api_responce_error_message" : ar.reshape("""إذا استمرت المشكلة تواصل مع الدعم الفني للتطبيق
        سيتم استخدام آخر تحديث للعملات،
        ربما التاريخ على جهازك ليس مضبوطا، أو أن تاريخ اليوم المحلي مختلف في الوقت الحالي عن تاريخ اليوم بتوقيت جرينتش
        خطأ ما حدث أثناء تحديث قيمة العملات من المصدر"""),
        "unkown_error_message" : ar.reshape("العملات سيتم استخدام آخر تحديث للعملات\nخطأ غير معروف حدث أثناء تحديث قيمة"),
        "not_consistant_user" : ar.reshape("""تأكد من تخطيط ميزانيتك!
        رجاء لاحظ: إن كان لديك ميزانيات تُحدّث تلقائيا فقد تم إلغاؤها
        ~المخبر الإقتصادي
        'الإمساك بالنقود الطائرة هي أولى خطوات الإدخار'
        لقد مر وقت طويل منذ آخر مرة رأيناك :("""),
        "category_budget_overview_label" : ar.reshape("ميزانيات البنود"),
        "category_budget_not_set_note" : ar.reshape("أنت لم تحدد ميزانية لأي بند بعد!"),
        "set_budget" : ar.reshape("إضافة ميزانية"),
        "edit_budget" : ar.reshape("تعديل الميزانية"),
        "statistics" : ar.reshape("إحصائياتك!"),
        "total_income" : ar.reshape("الدخل الكلي"),
        "total_expense" : ar.reshape("النفقات الكلية"),
        "net_balance" : ar.reshape("الصافي"),
        "bar_title" : ar.reshape("الدخل والنفقات على مدار الشهور"),
        "months" : ar.reshape("الشهور"),
        "piechart_categories_title" : ar.reshape("توزيع النفقات للشهر"),
        "clear" : ar.reshape("محو"),
        "delete_selected" : ar.reshape("حذف المحدد"),
        "current_month_balance" : ar.reshape("رصيدك للشهر الحالي"),
        "remaining_budget" : ar.reshape("المتبقي في ميزانيتك"),
        "no_expense_yet" : ar.reshape(" لم تنفق على شيء بعد هذا الشهر"),
        "not_budget_set" : ar.reshape("لم تحدد ميزانية بعد"),
        "categories_expenses_current_month" : ar.reshape("مصروفات البنود لهذا الشهر"),
        "recent_transactions" : ar.reshape("المعاملات الحديثة"),
        "view_all" : ar.reshape("عرض الكل"),
        "main_currency_across_app" : ar.reshape("العملة الرئيسية في التطبيق"),
        "currency_calculator" : ar.reshape("حاسبة العملات"),
        "update_date_label" : ar.reshape("آخر تاريخ لتحديث للعملات"),
        "updated" : ar.reshape("محدث"),
        "update" : ar.reshape("حدث"),
        "not_set" : ar.reshape("غير محدد"),


        
    }
}

# align
align = {
    "add_transaction" : {
        "ltr": {
            "amount_labl": {"column": 0, "sticky": "w"},
            "amount_entry": {"column": 0, "sticky": "e"},
            "currency": {"column": 1, "sticky": "w"},
            "note_labl": {"column": 0, "sticky": "w"},
            "note_text_box": {"column": 1, "sticky": "e"},
            "date_frame" : {"column": 0, "sticky": "w"},
            "date_labl" : {"column": 0, "sticky": "e"},
            "open_cal_btn" : {"column": 2, "sticky": "w"},
            
        },
        "rtl": {
            "amount_labl": {"column": 1, "sticky": "e"},
            "amount_entry": {"column": 1, "sticky": "w"},
            "currency": {"column": 0, "sticky": "e"},
            "note_labl": {"column": 1, "sticky": "e"},
            "note_text_box": {"column": 0, "sticky": "w"},
            "date_frame" : {"column": 1, "sticky": "e"},
            "date_labl" : {"column": 2, "sticky": "e"},
            "open_cal_btn" : {"column": 0, "sticky": "e"},

    }
        },

    "budget" : {
        "ltr": {
            "total_budget_lbl" : {"column": 0, "sticky": "w"},
            "total_budget_amount" : {"column": 1, "sticky": "w"},
            "spent_lbl" : {"column": 0, "sticky": "w"},
            "spent_amount" : {"column": 1, "sticky": "w"},
            "remaining_lbl" : {"column": 0, "sticky": "w"},
            "remaining_amount" : {"column": 1, "sticky": "w"},
            "currency" : {"column": 2, "sticky": "w"}

        },
        "rtl": {
            "total_budget_lbl" : {"column": 2, "sticky": "e"},
            "total_budget_amount" : {"column": 1, "sticky": "e"},
            "spent_lbl" : {"column": 2, "sticky": "e"},
            "spent_amount" : {"column": 1, "sticky": "e"},
            "remaining_lbl" : {"column": 2, "sticky": "e"},
            "remaining_amount" : {"column": 1, "sticky": "e"},
            "currency" : {"column": 0, "sticky": "e"}

        }
    },
}


currency = "EGP"
current_user_id = "not defined"
choosed_mode = "dark"
choosed_theme = "black"
choosed_colors = Dark_Black
lang_name = "en"
choosed_lang = LANG[lang_name]
direction = "rtl"

def set_mode(mode: str) -> None:
    "set the app choosed mode ['light', 'dark']"
    global choosed_mode
    if mode == 'light':
        choosed_mode = 'light'
    elif mode == 'dark':
        choosed_mode = 'dark'

    set_theme(choosed_theme)

def set_theme(theme: str) -> None:
    """sets the theme used in the app into the choosed theme by passing dictionary name
    ['blue' - 'yellow' - 'green' - 'red']
    default value will use the current theme"""
    global choosed_colors, choosed_mode, choosed_theme
    choosed_theme = theme
    if choosed_mode == 'light':
        if theme == 'blue':
            choosed_colors = Light_Blue
        elif theme == 'yellow':
            choosed_colors  = Light_Yellow
        elif theme == 'green':
            choosed_colors = Light_Green
        elif theme == 'red':
            choosed_colors = Light_Red
        elif theme == 'purple':
            choosed_colors = Light_Purple
        elif theme == 'grey':
            choosed_colors = Light_Grey
        elif theme == 'black':
            choosed_colors = Light_Black
    elif choosed_mode == 'dark':
        if theme == 'blue':
            choosed_colors = Dark_Blue
        elif theme == 'yellow':
            choosed_colors  = Dark_Yellow
        elif theme == 'green':
            choosed_colors = Dark_Green
        elif theme == 'red':
            choosed_colors = Dark_Red
        elif theme == 'purple':
            choosed_colors = Dark_Purple
        elif theme == 'grey':
            choosed_colors = Dark_Grey
        elif theme == 'black':
            choosed_colors = Dark_Black


def set_lang(lang: str) -> None:
    "sets the language used in the app by passing the dictionary name ['AR' - 'EN']"
    global choosed_lang, lang_name, direction
    if lang == "ar":
        lang_name = "ar"
        direction = "rtl"
    elif lang == "en":
        lang_name = "en"
        direction = "ltr"
    
    choosed_lang = LANG[lang_name]
        

def get_current_lang() -> str:
    "returns the curent choosed language"
    global lang_name
    return lang_name


def set_current_user_id(user_id) -> None:
    "sets the global user id used in the whole app during the session"
    global current_user_id
    current_user_id = str(user_id)

def get_current_user_id() -> int | str:
    "returns the global user id used in the session"
    if current_user_id != 'not defined':
        return int(current_user_id)
    else:
        return 0



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)