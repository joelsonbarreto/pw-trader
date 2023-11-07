import tkinter as lg
from tkinter import messagebox
import sys

# Função para verificar as credenciais
def verificar_credenciais():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    # Verifique as credenciais (substitua com sua lógica de verificação de usuário/senha)
    if usuario == "joelson" and senha == "1010":
        messagebox.showinfo("Login", "Login bem-sucedido!")
        login.destroy()
        
    else:
        messagebox.showerror("Login", "Credenciais inválidas. Tente novamente.")

# Criar a janela principal
login = lg.Tk()
login.title("Tela de Login")
largura = 200  # Largura da janela em pixels
altura = 300   # Altura da janela em pixels
login.geometry(f"{largura}x{altura}")

# Widgets
label_usuario = lg.Label(login, text="Usuário:")
label_usuario.pack()
entry_usuario = lg.Entry(login)
entry_usuario.pack()

label_senha = lg.Label(login, text="Senha:")
label_senha.pack()
entry_senha = lg.Entry(login, show="*")
entry_senha.pack()

botao_login = lg.Button(login, text="Login", command=verificar_credenciais)
botao_login.pack()


# Iniciar o loop principal
login.mainloop()

