from tkinter import *
from tkinter import ttk

# COLORS
color1 = '#000000'  # black
color2 = '#273a59'  # blue
color3 = '#ff870f'  # orange
color4 = '#ffffff'  # white


# WINDOW
window = Tk()
window.title('SmiiLe Calculator')
window.geometry('320x450')
window.minsize(320, 450)
window.maxsize(320, 450)
window.config(bg=color1)


# DISPLAY
display_frame = Frame(window, width=320, height=100, bg=color2)
display_frame.grid(row=0, column=0)

# BODY
body_frame = Frame(window, width=320, height=350)
body_frame.grid(row=1, column=0)


input_values = '0'

# FUNCTIONS
def display_values(event=None):
    global input_values
    signals = '%/*+-'

    if len(input_values) > 1 and event in signals and input_values[-1] in signals:
        input_values = input_values[:-1]
    
    if input_values == '0' and event not in signals:
        input_values = input_values[:-1]

    if event == "C":
        input_values = input_values[:-1]
    elif event == 'CE':
        input_values = ''
    else:
        input_values += str(event)
    
    if input_values == '':
        input_values = '0'
    display_label.config(text=input_values)


def calculate():
    global input_values
    result = str(eval(input_values))
    display_label.config(text=result)
    input_values = result

def negate():
    global input_values
    input_values = int(input_values)
    input_values *= -1
    input_values = str(input_values)
    display_label.config(text=input_values)


# LABELS

display_label = Label(
    display_frame,
    text='0',
    width=13,
    height=2,
    relief=FLAT,
    anchor='e',
    justify=RIGHT,
    font=('Arial', 30, 'bold'),
    bg=color2,
    fg=color4,
)
display_label.place(x=0, y=0)


# BUTTONS
button_CE = Button(
    body_frame,
    text='CE',
    width=10,
    height=4,
    font=('Arial', 9, 'bold'),
    relief=RAISED,
    overrelief=RIDGE,
    command=lambda: display_values("CE")
)
button_CE.place(x=0, y=0)

button_C = Button(
    body_frame,
    text='C',
    width=10,
    height=4,
    font=('Arial', 9, 'bold'),
    relief=RAISED,
    overrelief=RIDGE,
    command=lambda: display_values("C")
)
button_C.place(x=80, y=0)

button_mod = Button(
    body_frame,
    text='%',
    width=10,
    height=4,
    font=('Arial', 9, 'bold'),
    relief=RAISED,
    overrelief=RIDGE,
    command=lambda: display_values("%")
)
button_mod.place(x=160, y=0)

button_division = Button(
    body_frame,
    text='/',
    width=10,
    height=4,
    bg=color3,
    fg=color4,
    font=('Arial', 9, 'bold'),
    relief=RAISED,
    overrelief=RIDGE,
    command=lambda: display_values("/")
)
button_division.place(x=240, y=0)

button_7 = Button(
    body_frame,
    text='7',
    width=10,
    height=4,
    font=('Arial', 9, "bold"),
    relief=RAISED,
    overrelief=RIDGE,
    command=lambda: display_values("7")
)
button_7.place(x=0, y=70)

button_8 = Button(
    body_frame,
    text='8',
    width=10,
    height=4,
    font=('Arial', 9, 'bold'),
    relief=RAISED,
    overrelief=RIDGE,
    command=lambda: display_values("8")
)
button_8.place(x=80, y=70)

button_9 = Button(
    body_frame,
    text='9',
    width=10,
    height=4,
    font=('Arial', 9, 'bold'),
    relief=RAISED,
    overrelief=RIDGE,
    command=lambda: display_values("9")
)
button_9.place(x=160, y=70)

button_times = Button(
    body_frame,
    text='*',
    width=10,
    height=4,
    bg=color3,
    fg=color4,
    font=('Arial', 9, 'bold'),
    relief=RAISED,
    overrelief=RIDGE,
    command=lambda: display_values("*")
)
button_times.place(x=240, y=70)

button_4 = Button(
    body_frame,
    text='4',
    width=10,
    height=4,
    font=('Arial', 9, 'bold'),
    relief=RAISED,
    overrelief=RIDGE,
    command=lambda: display_values("4")
)
button_4.place(x=0, y=140)

button_5 = Button(
    body_frame,
    text='5',
    width=10,
    height=4,
    font=('Arial', 9, 'bold'),
    relief=RAISED,
    overrelief=RIDGE,
    command=lambda: display_values("5")
)
button_5.place(x=80, y=140)

button_6 = Button(
    body_frame,
    text='6',
    width=10,
    height=4,
    font=('Arial', 9, 'bold'),
    relief=RAISED,
    overrelief=RIDGE,
    command=lambda: display_values("6")
)
button_6.place(x=160, y=140)

button_minus = Button(
    body_frame,
    text='-',
    width=10,
    height=4,
    bg=color3,
    fg=color4,
    font=('Arial', 9, 'bold'),
    relief=RAISED,
    overrelief=RIDGE,
    command=lambda: display_values("-")
)
button_minus.place(x=240, y=140)

button_1 = Button(
    body_frame,
    text='1',
    width=10,
    height=4,
    font=('Arial', 9, 'bold'),
    relief=RAISED,
    overrelief=RIDGE,
    command=lambda: display_values("1")
)
button_1.place(x=0, y=210)

button_2 = Button(
    body_frame,
    text='2',
    width=10,
    height=4,
    font=('Arial', 9, 'bold'),
    relief=RAISED,
    overrelief=RIDGE,
    command=lambda: display_values("2")
)
button_2.place(x=80, y=210)

button_3 = Button(
    body_frame,
    text='3',
    width=10,
    height=4,
    font=('Arial', 9, 'bold'),
    relief=RAISED,
    overrelief=RIDGE,
    command=lambda: display_values("3")
)
button_3.place(x=160, y=210)

button_plus = Button(
    body_frame,
    text='+',
    width=10,
    height=4,
    bg=color3,
    fg=color4,
    font=('Arial', 9, 'bold'),
    relief=RAISED,
    overrelief=RIDGE,
    command=lambda: display_values("+")
)
button_plus.place(x=240, y=210)

button_negate = Button(
    body_frame,
    text='+/-',
    width=10,
    height=4,
    font=('Arial', 9, 'bold'),
    relief=RAISED,
    overrelief=RIDGE,
    command= negate
)
button_negate.place(x=0, y=280)

button_0 = Button(
    body_frame,
    text='0',
    width=10,
    height=4,
    font=('Arial', 9, 'bold'),
    relief=RAISED,
    overrelief=RIDGE,
    command=lambda: display_values("0")
)
button_0.place(x=80, y=280)

button_comma = Button(
    body_frame,
    text='.',
    width=10,
    height=4,
    font=('Arial', 9, 'bold'),
    relief=RAISED,
    overrelief=RIDGE,
    command=lambda: display_values(".")
)
button_comma.place(x=160, y=280)

button_equals = Button(
    body_frame,
    text='=',
    width=10,
    height=4,
    bg=color3,
    fg=color4,
    font=('Arial', 9, 'bold'),
    relief=RAISED,
    overrelief=RIDGE,
    command=calculate
)
button_equals.place(x=240, y=280)

window.bind("<Key-Return>", lambda x: calculate)
window.bind("<KP_0>", lambda x: display_values('0'))
window.bind("<KP_1>", lambda x: display_values('1'))

window.mainloop()
