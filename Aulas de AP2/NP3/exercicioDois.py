
import tkinter as tk
from tkinter import Entry, Label, Button

def salvar_dados():
    # Aqui você pode adicionar lógica para salvar os dados
    print("Dados salvos")

def limpar_campos():
    # Aqui você pode adicionar lógica para limpar os campos de entrada
    nome_entry.delete(0, 'end')
    idade_entry.delete(0, 'end')
    matricula_entry.delete(0, 'end')

# Criar janela principal
root = tk.Tk()
root.title("Aula de Algoritmos - Python Desktop!")

# Definir esquema de cores
cor_de_fundo = "#f2f2f2"
cor_label = "#333333"
cor_botoes = "#4CAF50"

root.configure(bg=cor_de_fundo)

# Labels
Label(root, text="Nome do Aluno:", bg=cor_de_fundo, fg=cor_label, font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=5, sticky='w')
Label(root, text="Idade:", bg=cor_de_fundo, fg=cor_label, font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=5, sticky='w')
Label(root, text="Matrícula:", bg=cor_de_fundo, fg=cor_label, font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=5, sticky='w')

# Entradas de Texto
nome_entry = Entry(root, font=("Helvetica", 12))
nome_entry.grid(row=0, column=1, padx=10, pady=5)
idade_entry = Entry(root, font=("Helvetica", 12))
idade_entry.grid(row=1, column=1, padx=10, pady=5)
matricula_entry = Entry(root, font=("Helvetica", 12))
matricula_entry.grid(row=2, column=1, padx=10, pady=5)

# Botão de Salvar
Button(root, text="Salvar", command=salvar_dados, bg=cor_botoes, fg="white", font=("Helvetica", 12)).grid(row=3, column=0, pady=10, padx=10, columnspan=2, sticky='ew')

# Botão de Limpar
Button(root, text="Limpar", command=limpar_campos, bg=cor_botoes, fg="white", font=("Helvetica", 12)).grid(row=4, column=0, pady=10, padx=10, columnspan=2, sticky='ew')

# Adicionar imagem de exemplo para a logo do Programa
# logo_img = tk.PhotoImage(file='exemplo_logo.png')
# logo_label = tk.Label(root, image=logo_img, bg=cor_de_fundo)
# logo_label.grid(row=5, columnspan=2, pady=10)

# Loop principal
root.mainloop()