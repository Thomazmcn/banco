import customtkinter as cstk


cstk.set_default_color_theme("dark-blue")
cstk.set_appearance_mode("dark")


class CustomTkinterWindow(cstk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x240")
        self.title("CustomTkinter Test")

        self.button = cstk.CTkButton(
            master=self, corner_radius=10, command=self.button_function
        )
        self.button.place(relx=0.5, rely=0.5, anchor=cstk.CENTER)

    def button_function(self):
        print("Button pressed")


if __name__ == "__main__":
    window = CustomTkinterWindow()

    window.mainloop()
