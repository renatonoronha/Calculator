from tkinter import *
from tkinter import ttk

#colors
color1 = "#000000"  # black
color2 = "#273a59"  # blue


#calculator
window = Tk()
window.title('SmiiLe Calculator')
window.geometry("320x485")
window.config(bg=color1)


#display
display_frame = Frame(window, width=320, height=150, bg=color2)
display_frame.grid(row=0, column=0)

#body
body_frame = Frame(window, width=320, height=335)
body_frame.grid(row=1, column=0)


window.mainloop()