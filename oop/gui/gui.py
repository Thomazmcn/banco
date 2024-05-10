import tkinter
import customtkinter  # <- import the CustomTkinter module


class window(tkinter.Tk):  # create the Tk window like you normally do
    def __init__(self, geometry, title):
        self.geometry = "400x240"
        self.title = "CustomTkinter Test"

    def button_function(self):
        print("button pressed")


# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(
    master=root_tk, corner_radius=10, command=button_function
)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

window.mainloop(self)
