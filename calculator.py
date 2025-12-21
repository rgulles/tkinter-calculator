from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('320x480')

# Colors and Fonts
font = ('Courier', 18, 'bold')
bg_color = '#333333'
fg_color = '#ffffff'
numbers_bg_color = '#4d4d4d'

# Function for button clicks
def value_clicked(value):
    display.config(state="normal")
    display.insert(END, value)
    display.config(state="readonly")

def num1_clicked():
    value_clicked(1)
def num2_clicked():
    value_clicked(2)
def num3_clicked():
    value_clicked(3)
def num4_clicked():
    value_clicked(4)
def num5_clicked():
    value_clicked(5)   
def num6_clicked():
    value_clicked(6)
def num7_clicked():
    value_clicked(7)
def num8_clicked():
    value_clicked(8)
def num9_clicked():
    value_clicked(9)
def num0_clicked():
    value_clicked(0)

def add_clicked():
    value_clicked('+')
def sub_clicked():
    value_clicked('-')
def mul_clicked():
    value_clicked('*')
def div_clicked():
    value_clicked('/')

def delete_clicked():
    display.config(state="normal")
    display.delete(0, END)
    display.config(state="readonly")

def equal_clicked():
    try:
        display.config(state="normal")
        result = eval(display.get())
        display.delete(0, END)
        display.insert(0, result)
        display.config(state="readonly")
    except:
        display.config(state="normal")
        display.delete(0, END)
        display.insert(0, "Error")
        display.config(state="readonly")

# Frame
frame = Frame(root)
frame.pack(fill='both', expand=True) 
 
# Loops allows columns and rows to expand
for i in range(4):
    frame.grid_columnconfigure(i, weight=1)

for i in range(5):
    frame.grid_rowconfigure(i, weight=1)

# Display
display = Entry(frame, font=('Courier', 24), readonlybackground='#333333', fg=fg_color, justify='right', state="readonly")

# Buttons
num1 = Button(frame, text="1", font=font, bg=numbers_bg_color, fg=fg_color, command=num1_clicked)
num2 = Button(frame, text="2", font=font, bg=numbers_bg_color, fg=fg_color, command=num2_clicked)
num3 = Button(frame, text="3", font=font, bg=numbers_bg_color, fg=fg_color, command=num3_clicked)
num4 = Button(frame, text="4", font=font, bg=numbers_bg_color, fg=fg_color, command=num4_clicked)
num5 = Button(frame, text="5", font=font, bg=numbers_bg_color, fg=fg_color, command=num5_clicked)
num6 = Button(frame, text="6", font=font, bg=numbers_bg_color, fg=fg_color, command=num6_clicked)
num7 = Button(frame, text="7", font=font, bg=numbers_bg_color, fg=fg_color, command=num7_clicked)
num8 = Button(frame, text="8", font=font, bg=numbers_bg_color, fg=fg_color, command=num8_clicked)
num9 = Button(frame, text="9", font=font, bg=numbers_bg_color, fg=fg_color, command=num9_clicked)
num0 = Button(frame, text="0", font=font, bg=numbers_bg_color, fg=fg_color, command=num0_clicked)
add = Button(frame, text="+", font=font, bg=bg_color, fg=fg_color, command=add_clicked)
sub = Button(frame, text="-", font=font, bg=bg_color, fg=fg_color, command=sub_clicked)
mul = Button(frame, text="x", font=font, bg=bg_color, fg=fg_color, command=mul_clicked)
div = Button(frame, text="/", font=font, bg=bg_color, fg=fg_color, command=div_clicked)
equal = Button(frame, text="=", font=font, bg="#444444", fg=fg_color, command=equal_clicked)
delete = Button(frame, text="C", font=font, bg='#444444', fg=fg_color, command=delete_clicked)

# Row 0
display.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Row 1
num7.grid(row=1, column=0, sticky="nsew")
num8.grid(row=1, column=1, sticky="nsew")
num9.grid(row=1, column=2, sticky="nsew")
div.grid(row=1, column=3, sticky="nsew")

# Row 2
num4.grid(row=2, column=0, sticky="nsew")
num5.grid(row=2, column=1, sticky="nsew")
num6.grid(row=2, column=2, sticky="nsew")
mul.grid(row=2, column=3, sticky="nsew")

# Row 3
num1.grid(row=3, column=0, sticky="nsew")
num2.grid(row=3, column=1, sticky="nsew")
num3.grid(row=3, column=2, sticky="nsew")
sub.grid(row=3, column=3, sticky="nsew")

# Row 4
delete.grid(row=4, column=0, sticky="nsew")
num0.grid(row=4, column=1, sticky="nsew")
equal.grid(row=4, column=2, sticky="nsew")
add.grid(row=4, column=3, sticky="nsew")


root.mainloop()