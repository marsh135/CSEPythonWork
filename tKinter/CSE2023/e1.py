#exercise1

import tkinter as tk

def action():
    greeting["text"] = "Goodbye, Students!"

font_tuple = ("Comic Sans MS", 100, "italic")

window =  tk.Tk()
#window.destroy()
greeting = tk.Label(
    text="Hello, Students!", 
    font=font_tuple,
    background = "tan",
    foreground =  "#556b2f"
    )

btn_clickme =  tk.Button(
    text= "Click me!",
    width=25,
    height=5,
    bg= "yellow",
    fg = "red",
    command =  action
).pack()
greeting.pack()

window.mainloop()



