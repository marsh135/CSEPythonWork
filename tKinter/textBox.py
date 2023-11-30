import tkinter as tk        #Classic Widgets

window =  tk.Tk()  # MUST HAVE
window.destroy()

text_box =  tk.Text()
text_box.pack()
text_box.get("1.0")

window.mainloop() #MUST HAVE