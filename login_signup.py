import customtkinter
import db
import config


class Login_Sinup(customtkinter.CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master)

        self.master = master       # The App() instance

                        # Setting Log in box Frame

        # Setting the position in the box relative to the size of the main window
        self.login_frame_height = master.screen_height/1.75
        self.login_frame_width = master.screen_width/2
        self.login_frame = customtkinter.CTkFrame(self, width=self.login_frame_width, height=self.login_frame_height,
                                                    # fg_color=config.Light_Black["login_bg"]
                                                    )
        self.login_frame.pack(anchor="center",pady=(master.screen_height - self.login_frame_height)/2)
        self.login_frame.propagate(True)
        self.login_frame.columnconfigure((3), weight=1)

        # Title Label
        self.lbl1 = customtkinter.CTkLabel(self.login_frame, text=config.choosed_lang["login_label"], font=("arial", 32, "bold"))
        self.lbl1.grid(row=0, sticky="NSEW", pady=20)

        # user name and passowrd entries
        self.user_name_entry = customtkinter.CTkEntry(self.login_frame, width=300,
                                                        placeholder_text=config.choosed_lang["username"], fg_color="transparent",
                                                        # placeholder_text_color=config.choosed_colors["entry_placeholder_color"],
                                                        # border_color=config.choosed_colors["entry_border_color"]
                                                        )
        self.user_name_entry.grid(row=1, sticky="NSEW", pady=10, padx=30)
        self.password_entry = customtkinter.CTkEntry(self.login_frame, show="●", font=("Arial", 12), width=300,
                                                    placeholder_text=config.choosed_lang["password"], fg_color="transparent",
                                                    # placeholder_text_color=config.choosed_colors["entry_placeholder_color"],
                                                    # border_color=config.choosed_colors["entry_border_color"]
                                                    )
        self.password_entry.grid(row=2, sticky="NSEW", pady=10, padx=30)

        # Check box to show password or hide password, Default is that password is hidden
        self.show_password = customtkinter.BooleanVar(value=False)
        self.show_password_checkbox = customtkinter.CTkCheckBox(self.login_frame,text=config.choosed_lang["show_password_checkbox"],
                                                                # fg_color=config.choosed_colors["checkbox_fg_color"],
                                                                # hover_color=config.choosed_colors["checkbox_hover_color"],
                                                                # border_color=config.choosed_colors["checkbox_border_color"],
                                                                # checkmark_color=config.choosed_colors["checkbox_checkmark_color"],
                                                                variable=self.show_password,onvalue=True, offvalue=False,
                                                                checkbox_width=17, checkbox_height=17, font=("Arial", 11.5),
                                                                command=self.hide_password)
        self.show_password_checkbox.grid(row=3, padx=30, sticky="W")

        # Gives a note if username or password are incorrect
        self.note_label = customtkinter.CTkLabel(self.login_frame, font=("arial", 10), text_color="red")
        
        self.login_btn = customtkinter.CTkButton(self.login_frame, width=100,text=config.choosed_lang["login_button"],
                                                # fg_color=config.choosed_colors["sidebar_btn"],
                                                # hover_color=config.choosed_colors["button_hover_color"],
                                                # border_color=config.choosed_colors["button_border_color"],
                                                command=self.log_in)
        self.login_btn.grid(row=5, pady=20)

        # refrence to customize the box to suit Sign up
        self.signup_link_note = customtkinter.CTkLabel(self.login_frame, text=config.choosed_lang["signup_link_note"],  font=("Arial", 12, "underline"),
                                                            text_color="blue", cursor="hand2")
        self.signup_link_note.bind("<Button-1>", self.open_signup_frame)
        self.signup_link_note.grid(row=6)


    def log_in(self) -> None:
        """If the user is valid, opens the Home frame, else show a note for the user to check its user name and password"""
        try:
            user_id_request = db.isvalid_user(self.user_name_entry.get().lower().strip(), self.password_entry.get().strip())
        except:
            db.open_database("all")
            user_id_request = db.isvalid_user(self.user_name_entry.get().lower().strip(), self.password_entry.get().strip())


        if user_id_request not in ['not valid', 'not found']:
            self.destroy()
            self.master.load_app(user_id_request)
        
        else:
            self.note_label.configure(text=config.choosed_lang["invalid_user_note"])
            self.note_label.grid(row=4, sticky="NSEW")

    def sign_up(self) -> None:
        """checks if the user name is used before and check the calidity of password, if all true add to the database"""
        special_characters = "!@$%^&()/-+_|=<>?,'\" "
        try:
            if db.isreserved(self.user_name_entry.get().lower()):
                self.note_label.configure(text=config.choosed_lang["reserved_username_note"])
                self.note_label.grid(row=5)
                return
        except:
            db.open_database("all")
            if db.isreserved(self.user_name_entry.get().lower()):
                self.note_label.configure(text=config.choosed_lang["reserved_username_note"])
                self.note_label.grid(row=5)
                return


        if self.password_entry.get() == "":
            self.note_label.configure(text=config.choosed_lang["empty_password"])
            self.note_label.grid(row=5)
            return


        if self.password_entry.get() != self.confirm_password_entry.get():
            self.note_label.configure(text=config.choosed_lang["wrong_password_confirmation_note"])
            self.note_label.grid(row=5)
            return

        if not self.password_entry.get().isascii():
            self.note_label.configure(text=config.choosed_lang["non_english_characters"])
            self.note_label.grid(row=5)
            return

        if any(char in self.password_entry.get() for char in special_characters):
            self.note_label.configure(text=config.choosed_lang["special_character_note"])
            self.note_label.grid(row=5)
            return
        

        db.add_user(self.user_name_entry.get().strip().lower(), self.password_entry.get().strip().lower())
        user_id = db.isvalid_user(self.user_name_entry.get().strip().lower(), self.password_entry.get().strip().lower())
        self.destroy()
        self.master.load_app(user_id)
        
    def open_signup_frame(self, event) -> None:
        """perform some editing on the login frame to make it a sign up frame, without rebuilding a all widgets"""

        # changing the Title label
        self.lbl1.configure(text=config.choosed_lang["signup_label"])

        # Destroy the old entries for user name and password, to avoid anything writtin in them, delete() is not used as it removes the text placeholder
        self.user_name_entry.destroy()
        self.password_entry.destroy()
        self.note_label.grid_forget()
        
        # Reinitializing the username and password entries
        self.user_name_entry = customtkinter.CTkEntry(self.login_frame, width=300, placeholder_text=config.choosed_lang["username"],
                                                    fg_color="transparent",
                                                    # border_color=config.choosed_colors["entry_border_color"],
                                                    # placeholder_text_color=config.choosed_colors["entry_placeholder_color"]
                                                    )
        self.user_name_entry.grid(row=1, sticky="NSEW", pady=10, padx=30)
        self.password_entry = customtkinter.CTkEntry(self.login_frame, show="●", font=("Arial", 12),width=300,
                                                        placeholder_text=config.choosed_lang["password"], fg_color="transparent",
                                                        # placeholder_text_color=config.choosed_colors["entry_placeholder_color"],
                                                        # border_color=config.choosed_colors["entry_border_color"]
                                                        )
        self.password_entry.grid(row=2, sticky="NSEW", pady=10, padx=30)

        # Initializing confirm password entry
        self.confirm_password_entry = customtkinter.CTkEntry(self.login_frame, show="●", font=("Arial", 12), width=300,
                                                            placeholder_text=config.choosed_lang["confirm_password"], fg_color="transparent",
                                                            # placeholder_text_color=config.choosed_colors["entry_placeholder_color"],
                                                            # border_color=config.choosed_colors["entry_border_color"]
                                                            )
        self.confirm_password_entry.grid(row=3)

        self.show_password_checkbox.deselect()
        self.show_password_checkbox.grid(row=4)

        self.login_btn.configure(text=config.choosed_lang["signup_button"], command=self.sign_up)
        self.login_btn.grid(row=6)

        # Change the link note used to refrence to sign up box into a refrence to the log in box, by refreshing the frame
        self.signup_link_note.configure(text=config.choosed_lang["login_link_note"])
        self.signup_link_note.bind("<Button-1>", self.master.open_login_window)
        self.signup_link_note.grid(row=7)

    def hide_password(self) -> None:
        """hides characters of password while typing unless 'show password' check box is checked"""
        if self.show_password.get():
            self.password_entry.configure(show="", font=("Arial", 13))
            if hasattr(self, "confirm_password_entry"):
                self.confirm_password_entry.configure(show="", font=("Arial", 13))
        else:
            self.password_entry.configure(show="●", font=("Arial", 12))
            if hasattr(self, "confirm_password_entry"):
                self.confirm_password_entry.configure(show="●", font=("Arial", 12))
