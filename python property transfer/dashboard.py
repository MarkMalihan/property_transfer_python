import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter.messagebox import showinfo
from PIL import Image


ctk.set_appearance_mode("system")  # Modes: system (default), light, dark
#ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
        
#window
dashboard = ctk.CTk()
dashboard.geometry("1000x600")
dashboard.title("Property Transfer")
dashboard.configure(fg_color = 'white')
dashboard.state('zoomed')
dashboard.iconbitmap('python property transfer\images\icons8-data-transfer-483.ico')


# Define a function to change the color of the text when hovering over it
def on_enter1(event):
    sidenav_btn1.configure(fg_color="white", text_color = 'black', corner_radius = 20, width = 200)
    
# Define a function to change the color of the text when leaving the hover
def on_leave1(event):
    sidenav_btn1.configure(fg_color="transparent", text_color = 'white')
    
# Define a function to change the color of the text when hovering over it
def on_enter2(event):
    sidenav_btn2.configure(fg_color="white", text_color = 'black', corner_radius = 20, width = 200)
   
# Define a function to change the color of the text when leaving the hover
def on_leave2(event):
    sidenav_btn2.configure(fg_color="transparent", text_color = 'white')

# Define a function to change the color of the text when hovering over it
def on_enter3(event):
    sidenav_btn3.configure(fg_color="white", text_color = 'black', corner_radius = 20, width = 200)
   
# Define a function to change the color of the text when leaving the hover
def on_leave3(event):
    sidenav_btn3.configure(fg_color="transparent", text_color = 'white')

# Define a function to change the color of the text when hovering over it
def on_enter4(event):
    sidenav_btn4.configure(fg_color="white", text_color = 'black', corner_radius = 20, width = 200)
   
# Define a function to change the color of the text when leaving the hover
def on_leave4(event):
    sidenav_btn4.configure(fg_color="transparent", text_color = 'white')

# Define a function to change the color of the text when hovering over it
def on_enter5(event):
    sidenav_btn5.configure(fg_color="white", text_color = 'black', corner_radius = 20, width = 200)
   
# Define a function to change the color of the text when leaving the hover
def on_leave5(event):
    sidenav_btn5.configure(fg_color="transparent", text_color = 'white')

#window frame
window_frame = ctk.CTkFrame(dashboard, fg_color='white')
window_frame.pack(fill='both', expand=True)

#sidebar frame
sidebar_frame = ctk.CTkFrame(window_frame, fg_color='maroon', height=dashboard.winfo_height(), width=250, corner_radius=0)
sidebar_frame.pack(expand = False, fill = 'both', side='left')

#PUP Logo
PUP_logo = ctk.CTkImage(Image.open('python property transfer\images\PUPLogo.png'), size=(110, 110))
label = ctk.CTkLabel(sidebar_frame, image = PUP_logo, text=None)
label.pack(padx = 70, pady = 15)

#office name
office_name = ctk.CTkLabel(sidebar_frame, text="Property Plant and Equipment", font= ctk.CTkFont('Arial', size = 15, weight = "bold"), text_color='white')
office_name.pack(padx = 5)

#sidenav buttons
sidenav_btn1 = ctk.CTkButton(sidebar_frame, text='Dashboard', font= ctk.CTkFont('Arial', size = 20, weight = "bold"), fg_color='transparent')
sidenav_btn1.pack(pady = 20)
sidenav_btn1.bind("<Enter>", on_enter1)
sidenav_btn1.bind("<Leave>", on_leave1)

sidenav_btn2 = ctk.CTkButton(sidebar_frame, text='Equipment', font= ctk.CTkFont('Arial', size = 20, weight = "bold"), fg_color='transparent')
sidenav_btn2.pack(pady = 20)
sidenav_btn2.bind("<Enter>", on_enter2)
sidenav_btn2.bind("<Leave>", on_leave2)

sidenav_btn3 = ctk.CTkButton(sidebar_frame, text='Requests', font= ctk.CTkFont('Arial', size = 20, weight = "bold"), fg_color='transparent')
sidenav_btn3.pack(pady = 20)
sidenav_btn3.bind("<Enter>", on_enter3)
sidenav_btn3.bind("<Leave>", on_leave3)

sidenav_btn4 = ctk.CTkButton(sidebar_frame, text='Report', font= ctk.CTkFont('Arial', size = 20, weight = "bold"), fg_color='transparent')
sidenav_btn4.pack(pady = 20)
sidenav_btn4.bind("<Enter>", on_enter4)
sidenav_btn4.bind("<Leave>", on_leave4)

sidenav_btn5 = ctk.CTkButton(sidebar_frame, text='History', font= ctk.CTkFont('Arial', size = 20, weight = "bold"), fg_color='transparent')
sidenav_btn5.pack(pady = 20)
sidenav_btn5.bind("<Enter>", on_enter5)
sidenav_btn5.bind("<Leave>", on_leave5)


#header frame
header_frame = ctk.CTkFrame(window_frame, fg_color='#313131', height=50, width=dashboard.winfo_width(), corner_radius=0)
header_frame.pack(fill = 'both', side='top')

#app logo
app_logo = ctk.CTkImage(Image.open('python property transfer\images\icons8-data-transfer-483-white.png'), size=(25, 25))
app_logo_label = ctk.CTkLabel(header_frame, image= app_logo, text=None)
app_logo_label.pack(side = 'left', pady = 10, padx = 10)

#app name
app_name1 = ctk.CTkLabel(header_frame, text='PROPERTY', font= ctk.CTkFont('Arial', size = 22, weight = "bold"), text_color='white')
app_name1.pack(side = 'left', pady = 10, padx = 10)
app_name2 = ctk.CTkLabel(header_frame, text='TRANSFER', font= ctk.CTkFont('Arial', size = 22, weight = "bold"), text_color='#ee4444')
app_name2.pack(side = 'left', pady = 10)

dashboard.mainloop()