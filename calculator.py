from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('320x480')

frame = Frame(root)
frame.pack(fill='both', expand=True) 


# Loops allows columns and rows to expand
for i in range(4):
    frame.grid_columnconfigure(i, weight=1)

for i in range(5):
    frame.grid_rowconfigure(i, weight=1)


# Display
display = Entry(frame)

# Buttons
num1 = Button(frame, text="1")
num2 = Button(frame, text="2")
num3 = Button(frame, text="3")
num4 = Button(frame, text="4")
num5 = Button(frame, text="5")
num6 = Button(frame, text="6")
num7 = Button(frame, text="7")
num8 = Button(frame, text="8")
num9 = Button(frame, text="9")
num0 = Button(frame, text="0")
add = Button(frame, text="+")
sub = Button(frame, text="-")
mul = Button(frame, text="x")
div = Button(frame, text="/")
equal = Button(frame, text="=")
delete = Button(frame, text="C")

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