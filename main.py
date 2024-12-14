import ttkbootstrap as ttk
from ttkbootstrap import constants

# Main Window
root = ttk.Window(
    title="DGW Spartan Support",
    themename="superhero",
    minsize=(800, 400),
)

# Functions
def change_label_text() -> None:
    if label.cget("text") == "Hello, World!":
        label.config(text="Goodbye, World!")
    else:
        label.config(text="Hello, World!")

# Widgets
label = ttk.Label(
    text="Hello, World!",
    font=("Helvetica", 24),
    bootstyle=(constants.DANGER, constants.INVERSE),
)

button = ttk.Button(
    text="Toggle",
    command=change_label_text,
)

label.pack(pady=50)
button.pack()

root.mainloop()
