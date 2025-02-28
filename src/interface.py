import tkinter as tk
from tkinter import scrolledtext
from services.groq_api import consultar_groqcloud


def enviar_pergunta():
    pergunta = entrada_pergunta.get()
    if pergunta:
        resposta = consultar_groqcloud(pergunta)
        caixa_resposta.config(state='normal')
        caixa_resposta.delete(1.0, tk.END)
        caixa_resposta.insert(tk.END, resposta)
        caixa_resposta.config(state='disabled')


# Janela principal
janela = tk.Tk()
janela.title("🤖 Agente IA - GroqCloud")
janela.geometry("600x400")

# Entrada e rótulo de pergunta
tk.Label(janela, text="Digite sua pergunta:", font=("Arial", 14)).pack(pady=10)
entrada_pergunta = tk.Entry(janela, width=60, font=("Arial", 12))
entrada_pergunta.pack(pady=5)

# Botão para enviar pergunta
botao_enviar = tk.Button(janela, text="Perguntar", command=enviar_pergunta, font=("Arial", 12), bg="#4CAF50", fg="white")
botao_enviar.pack(pady=10)

# Área de resposta (texto rolável)
tk.Label(janela, text="Resposta da IA:", font=("Arial", 14)).pack(pady=10)
caixa_resposta = scrolledtext.ScrolledText(janela, width=70, height=10, font=("Arial", 12), state='disabled')
caixa_resposta.pack(pady=5)

# Inicia a interface gráfica
janela.mainloop()
