import customtkinter as ctk
import psutil

janela = ctk.CTk()
janela.title("CPUeMEMORIA")
janela.geometry("400x250")

cpu_texto = ctk.CTkLabel(janela, text="CPU: 0%")
cpu_texto.pack(pady=(20, 5))

cpu_barra = ctk.CTkProgressBar(janela, width=250)
cpu_barra.pack()

mem_texto = ctk.CTkLabel(janela, text="Memória: 0%")
mem_texto.pack(pady=(20, 5))

mem_barra = ctk.CTkProgressBar(janela, width=250)
mem_barra.pack()


def atualizar():
    cpu = psutil.cpu_percent()
    memoria = psutil.virtual_memory().percent

    cpu_texto.configure(text=f"CPU: {cpu:.1f}%")
    mem_texto.configure(text=f"Memória: {memoria:.1f}%")

    cpu_barra.set(cpu / 100)
    mem_barra.set(memoria / 100)

    janela.after(1000, atualizar)


atualizar()
janela.mainloop()