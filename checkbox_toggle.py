from tkinter import IntVar
import ttkbootstrap as ttk
from ttkbootstrap import constants

# Main Window
root = ttk.Window(
    title="Checkbox and Toggle",
    themename="superhero",
    minsize=(800, 400),
)

# Variables
toggle = IntVar()

# Functions
def toggler():
    if toggle.get() == 1:
        label.config(text="Checked!")
    else:
        label.config(text="Unchecked!")

# Widgets
label = ttk.Label(
    text="Click the checkbutton bellow"
)

checkbox = ttk.Checkbutton(
    bootstyle=(constants.PRIMARY, 'round-toggle'),
    text="Check Me Out!",
    variable=toggle,
    onvalue=1,
    offvalue=0,
    command=toggler
)


# Attach widgets
label.pack(pady=(40, 10))
checkbox.pack(pady=(10, 10))


root.mainloop()
