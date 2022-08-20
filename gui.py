import customtkinter as ctk
import tkinter
import tkinter.messagebox

ctk.set_appearance_mode("light")
class App(ctk.CTk):
    w = 1180 #get user computer resolution
    h = 620
    def __init__(self, bot, database, queries):
        super().__init__()
        self.state("zoomed")
        self.title("Instagram BOT")
        self.geometry(f"{App.w}x{App.h}")
        self.bot = bot
        self.database = database
        self.queries = queries
        
        self.grid_rowconfigure(1, weight=1)
        self.top_frame = ctk.CTkFrame(master=self)
        self.top_frame.grid(row=0,column=0,columnspan=2,padx=5, pady=5, sticky="we")
        self.left_frame = ctk.CTkFrame (master=self, height=App.h-100)
        self.left_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nswe")
        self.right_frame = ctk.CTkFrame (master=self, height=App.h-100)
        self.right_frame.grid(row=1, column=1,pady=5,padx=5,ipadx=150, sticky="nswe")
        self.right_frame.propagate(False)
        self.left_frame.propagate(False)

        self.login_label = ctk.CTkLabel(master=self.top_frame, text="User", anchor="e")
        self.login_label.grid(row=0,column=0, padx=15, pady=5)
        self.login_entry = ctk.CTkEntry(master=self.top_frame, width=250)
        self.login_entry.grid(row=0,column=1, ipadx=70)
        self.password_label = ctk.CTkLabel(master=self.top_frame, text="Password", anchor="e")
        self.password_label.grid(row=0,column=2, padx = 15)
        self.password_entry = ctk.CTkEntry(master=self.top_frame,show="*")
        self.password_entry.grid(row=0,column=3, ipadx=50)
        self.login_button = ctk.CTkButton(master=self.top_frame, text="Log in",command=self.login)
        self.login_button.grid(row=0,column=4,padx=30)
        self.login_button.grid()

        self.user_label = ctk.CTkLabel(master=self.left_frame, text="Related Users")
        self.user_label.grid(row=0,column=0,pady=5)
        self.user_entry = ctk.CTkEntry(master=self.left_frame)
        self.user_entry.grid(row=0,column=1, ipadx=40)
        self.add_button = ctk.CTkButton(master=self.left_frame, text="Add", command=self.insert_account)
        self.add_button.grid(row=1,column=1,pady=2)
        self.list_label = ctk.CTkLabel(master=self.left_frame, text="List")
        self.list_label.grid(row=2,column=0, padx=10, sticky="ne",pady=2)
        self.related_list = tkinter.Listbox(master=self.left_frame)
        self.related_list.grid(row=2,column=1,ipadx=40, ipady=150,pady=2)
        self.remove_button = ctk.CTkButton(master=self.left_frame, text="Remove", command=self.delete_account)
        self.remove_button.grid(row=3, column=1,pady=2)
        self.since_label = ctk.CTkLabel(master=self.left_frame, text="Check since")
        self.since_label.grid(row=4,column=0,pady=2)
        self.since_entry = ctk.CTkEntry(master=self.left_frame)
        self.since_entry.grid(row=4,column=1,pady=10)
        self.search_button = ctk.CTkButton(master=self.left_frame, text="Search")
        self.search_button.grid(row=5, column=1,pady=2)
        self.num_users_label = ctk.CTkLabel(master=self.left_frame, text="Number of Users")
        self.num_users_label.grid(row=0,column=2,padx=10)
        self.num_users_entry = ctk.CTkEntry(master=self.left_frame)
        self.num_users_entry.grid(row=0, column=3,padx=5)
        self.runbot_button = ctk.CTkButton(master=self.left_frame, text="Run BOT")
        self.runbot_button.grid(row=0,column=4,padx=5)
        self.main_users_list = tkinter.Listbox(master=self.left_frame)
        self.main_users_list.grid(row=1, column=3,columnspan=2,rowspan=4, ipadx=120,ipady=250)

        self.right_frame.grid_rowconfigure(1,weight=1)
        self.unfollow_since_label = ctk.CTkLabel(master=self.right_frame, text="Since")
        self.unfollow_since_label.grid(row=0,column=0,pady=5)
        self.unfollow_since_entry = ctk.CTkEntry(master=self.right_frame)
        self.unfollow_since_entry.grid(row=0,column=1)
        self.unfollow_button = ctk.CTkButton(master=self.right_frame, text='Unfollow All')
        self.unfollow_button.grid(row=0,column=2,padx=10)
        self.unfollow_list = tkinter.Listbox(master=self.right_frame)
        self.unfollow_list.grid(row=1,column=0,columnspan=3,sticky="ns", pady=20,ipadx=60)

    def login(self):
        self.bot.login(self.login_entry.get(),self.password_entry.get())
        follwing_list = self.bot.get_following(self.login_entry.get())
        followers_list = self.bot.get_followers(self.login_entry.get())
        print(followers_list)
        print(len(followers_list))
        print(follwing_list)
        print(len(follwing_list))
    
    def insert_account(self):
        self.related_list.insert(tkinter.END, self.user_entry.get())
        self.user_entry.delete(0,tkinter.END)
    
    def delete_account(self):
        self.related_list.delete(tkinter.ANCHOR)