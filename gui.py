from tkinter import *
from converter import convert

def on_convert():
    user_input = entry.get()
    parts = user_input.split()
    results = []

    for part in parts:
        results.append(convert(part))
    
    final_output = "\n\n".join(results)

    output.delete(1.0, END) # clear previous output
    output.insert(END, final_output)

# widgets = GUI elements like buttons, labels, images, text boxes
# windows = containers for widgets

# window
window = Tk() #instantiate an instance of a window
window.geometry("420x420") # set the size of the window
window.title("Hex-Binary-Converter") # set the title of the window
window.config(background="#3b3b3b") # set the background color of the window

# label
label = Label(window, text="Hex-Binary Converter", font=("Arial", 24), bg="#3b3b3b", fg="white")
label.pack()

# text entry box
entry = Entry(window, font=("Arial", 14), bg="#2b2b2b", fg="white", width=30)
entry.insert(0, "(enter number, hex, binary, or text)")
entry.pack(pady=20)

# convert button
button = Button(window, text="Convert", font=("Arial", 14), command=on_convert, bg="#ff0000", fg="black")
button.pack()

# output box
output = Text(window, font=("Arial", 14), bg="#2b2b2b", fg="white", height=10, width=40, wrap=WORD)
output.insert(END, "Output will be displayed here")
output.pack(pady=20)

window.mainloop() # place window on computer screen and listen for events



