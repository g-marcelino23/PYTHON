from tkinter import *
import psycopg2


def cadastrar():
    conectar = psycopg2.connect(database="postgres", user="postgres", password="123", host="localhost")
    cur = conectar.cursor()

    nome = str(inNome.get()).strip().title()
    idade = int(inIdade.get())
    matricula = str(inMatricula.get()).strip().title()

    cur.execute(f"INSERT INTO alunos(nome, idade, matricula) VALUES ('{nome}', {idade}, '{matricula}')")

    conectar.commit()
    cur.close()
    conectar.close()
    confirma()


def confirma():
    novaJanela = Tk()
    novaJanela.title("Sucesso")
    novaJanela.geometry("200x80")
    Label(novaJanela, text="Cadastro feito com Sucesso").place(x=10, y =10,)
    novo = Button(novaJanela, text="OK", command=lambda: novaJanela.destroy())
    novo.place(x=80, y=30)


def limpar():
    inNome.delete(0, END)
    inIdade.delete(0, END)
    inMatricula.delete(0, END)


janela = Tk()
janela.title("Formulário de Cadastro")
janela.geometry("500x500")
#janela.resizable(False, False)

resLabel = StringVar()
cadastro_frame = Frame(janela)


bemvindoLabel = Label(janela, text="Bem Vindo ao Programa Desktop - Python!", font="Arial 15")

#Labels
nomeLabel = Label(cadastro_frame, text="Nome:", font="Arial 15")
idadeLabel = Label(cadastro_frame, text="Idade:", font="Arial 15")
matriculaLabel = Label(cadastro_frame, text="Matricula:", font="Arial 15")
resultadoLabel = Label(cadastro_frame, textvariable=resLabel)
botaoCadastro = Button(janela, text="Cadastrar", command=cadastrar, borderwidth=3, height=1, width=10)
botaoLimpa = Button(janela, text="Limpar", command=limpar, borderwidth=3, height=1, width=10)

bemvindoLabel.grid(padx=70, pady=50)

'''
nomeLabel.grid(row=3, column=0)
idadeLabel.grid(row=4, column=0)
matriculaLabel.grid(row=5, column=0)
resultadoLabel.grid(row=6, column=0)
botaoCadastro.place(x=50, y=200)
botaoLimpa.place(x=150, y=200)
'''
#Formatação das Labels
nomeLabel.grid(row=0, column=0, padx=10, pady=5, sticky='w')
idadeLabel.grid(row=1, column=0, padx=10, pady=5, sticky='w')
matriculaLabel.grid(row=2, column=0, padx=10, pady=5, sticky='w')


#Entradas de Texto
inNome = Entry(cadastro_frame)
inIdade = Entry(cadastro_frame)
inMatricula = Entry(cadastro_frame)

#Formatação das Entradas de Texto
inNome.grid(row=0, column=1, padx=10, pady=5)
inIdade.grid(row=1, column=1, padx=10, pady=5)
inMatricula.grid(row=2, column=1, padx=10, pady=5)


'''
inNome.grid(row=3, column=1)
inIdade.grid(row=4, column=1)
inMatricula.grid(row=5, column=1)
'''

#Formatação dos Botões
resultadoLabel.grid(row=3, column=0, padx=10, pady=5, sticky='w')
botaoCadastro.place(x=20, y=250)
botaoLimpa.place(x=150, y=250)


cadastro_frame.place(y=100)
janela.mainloop()