import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd

import dashboard


ctk.set_appearance_mode("system")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

root = ctk.CTk()  # create CTk window like you do with the Tk window
root.geometry("700x500")
root.title("Property Transfer")
root.configure(fg_color = 'white')
root.resizable(False, False)



#login function
userID = tk.StringVar()
password = tk.StringVar()

def login_btn_clicked():
    other_window = dashboard()
    dashboard.mainloop()
    
#login frame
login_frame = ctk.CTkFrame(master=root, width=300, border_width=3, border_color='gray', corner_radius=20, fg_color='white')
login_frame.pack(padx = 50, pady = 50)

#app title
app_title = ctk.CTkLabel(login_frame,text='Login', font= ctk.CTkFont('Arial', size = 30, weight = "bold"))
app_title.pack(pady = 20)

#username
username_label = ctk.CTkLabel(login_frame, text='User ID', font=('Arial', 15))
username_label.pack()

username_entry = ctk.CTkEntry(login_frame, textvariable=userID, placeholder_text='Enter your ID', width= 300, height=35, font=ctk.CTkFont('Arial', 15) ,border_width=2, corner_radius=20)
username_entry.pack(padx = 50)

#password
password_label = ctk.CTkLabel(login_frame, text='Password', font=('Arial', 15))
password_label.pack()

password_entry = ctk.CTkEntry(login_frame, textvariable=password, placeholder_text='Enter your Password', width= 300, height=35, font=ctk.CTkFont('Arial', 15) ,border_width=2, corner_radius=20, show = '*')
password_entry.pack(padx = 50)

#forgot password
forgotPassword_label = ctk.CTkLabel(login_frame, text='Forgot Password', font=ctk.CTkFont('Arial', 15))
forgotPassword_label.pack(pady = 10)

#login button
login_btn = ctk.CTkButton(login_frame, border_width=0, height=35, text='Login', font=ctk.CTkFont('Arial', 15), corner_radius=20, command=login_btn_clicked)
login_btn.pack(pady = 20)

root.mainloop()