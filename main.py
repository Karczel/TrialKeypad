from tkinter import Button

import tkinter as tk


def handle_digit(*args):
    pass


window = tk.Tk()

# Frame (container) for digits

keypad = tk.Frame(window)


def digit_button(string, *args):
    return Button(keypad, text=string, command=handle_digit)


digit1 = Button(keypad, text="1", command=handle_digit)

digit2 = Button(keypad, text="2", command=handle_digit)

digit3 = Button(keypad, text="3", command=handle_digit)

digit4 = digit_button("4")
digit5 = digit_button("5")
digit6 = digit_button("6")
digit7 = digit_button("7")
digit8 = digit_button("8")
digit9 = digit_button("9")
digit0 = digit_button("0")


def digit_button(button, row, column, *args):
    button.grid(row=row, column=column,sticky=tk.EW)
    button.pack()

digit1.grid(row=0, column=0,sticky=tk.EW)
digit1.pack()

digit2.grid(row=0, column=1,sticky=tk.EW)
digit2.pack()

digit3.grid(row=0, column=2,sticky=tk.EW)
digit3.pack()

digit_button(digit4, 1, 0)
digit_button(digit5, 1, 1)
digit_button(digit6, 1, 2)
digit_button(digit7, 2, 0)
digit_button(digit8, 2, 1)
digit_button(digit9, 2, 2)
digit_button(digit0, 3, 1)

# Frame (container) for operators using Buttons

operator_pad = tk.Frame(window)
rownum = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for op in ['+', '-', '*', '/', '^', '=']:
    op_key = Button(operator_pad, text=op, command=...)
    op_key.grid(row=next(rownum), column=0, sticky=tk.EW)
    op_key.pack()

# Layout frames in window

keypad.pack(side=tk.LEFT, expand=True, fill=tk.X)

operator_pad.pack(side=tk.RIGHT, expand=True, fill=tk.X)

# grid doesnot track new window size automatically
# basically freeze it to the size when it opened
# keypad.grid(row=0, column=0, sticky=tk.EW)
# operator_pad.grid(row=0,column=1, sticky=tk.EW)

window.mainloop()
