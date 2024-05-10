import tkinter as tk
import customtkinter


class CustomTkinterWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x240")
        self.title("CustomTkinter Test")

        # Definindo uma função para o botão
        def button_function():
            print("Button pressed")

        # Usando CTkButton em vez de Button padrão do tkinter
        button = customtkinter.CTkButton(
            master=self, corner_radius=10, command=button_function
        )
        button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


if __name__ == "__main__":
    # Criando uma instância da sua janela personalizada
    window = CustomTkinterWindow()

    # Iniciando o loop principal da interface gráfica
    window.mainloop()
