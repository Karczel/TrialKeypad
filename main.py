from tkinter import Button

import tkinter as tk


def handle_digit(*args):
    pass


window = tk.Tk()

# Frame (container) for digits

keypad = tk.Frame(window)

keypad_row1 = tk.Frame(keypad)
keypad_row2 = tk.Frame(keypad)
keypad_row3 = tk.Frame(keypad)
keypad_row4 = tk.Frame(keypad)

def digit_button(string,row, *args):
    return Button(row, text=string, command=handle_digit)


digit1 = Button(keypad_row1, text="1", command=handle_digit)

digit2 = Button(keypad_row1, text="2", command=handle_digit)

digit3 = Button(keypad_row1, text="3", command=handle_digit)


digit4 = digit_button("4",keypad_row2)
digit5 = digit_button("5",keypad_row2)
digit6 = digit_button("6",keypad_row2)
digit7 = digit_button("7",keypad_row3)
digit8 = digit_button("8",keypad_row3)
digit9 = digit_button("9",keypad_row3)
no_digit1 = digit_button("",keypad_row4)
digit0 = digit_button("0",keypad_row4)
no_digit2 = digit_button("",keypad_row4)


def digit_button_pack(button, *args):
    button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

digit1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

digit2.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

digit3.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

digit_button_pack(digit4)
digit_button_pack(digit5)
digit_button_pack(digit6)
digit_button_pack(digit7)
digit_button_pack(digit8)
digit_button_pack(digit9)
digit_button_pack(no_digit1)
digit_button_pack(digit0)
digit_button_pack(no_digit2)

# Frame (container) for operators using Buttons

operator_pad = tk.Frame(window)
rownum = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for op in ['+', '-', '*', '/', '^', '=']:
    op_key = Button(operator_pad, text=op, command=...)
    op_key.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

# Layout frames in window

keypad_row1.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
keypad_row2.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
keypad_row3.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
keypad_row4.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

keypad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

operator_pad.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# grid doesnot track new window size automatically
# basically freeze it to the size when it opened
# keypad.grid(row=0, column=0, sticky=tk.EW)
# operator_pad.grid(row=0,column=1, sticky=tk.EW)

window.mainloop()
