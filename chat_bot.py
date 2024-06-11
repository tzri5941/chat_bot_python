from tkinter import *
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import time

## chat bot ##

perguntas = [
    "Qual é a capital do Brasil?",
    "Qual é o maior planeta do sistema solar?",
    "Quem escreveu 'Dom Quixote'?",
    "Quantos continentes existem?",
    "Qual é o símbolo químico do ouro?",
    "Quem pintou a Mona Lisa?",
    "Quem foi o primeiro homem a pisar na lua?",
    "Quem escreveu 'O Pequeno Príncipe'?",
    "Qual é o maior oceano do mundo?",
    "Quem foi o primeiro presidente do Brasil?",
    "Qual é o símbolo químico da água?",
    "Quantos lados tem um triângulo?",
    "Quem descobriu a gravidade?",
    "Qual é o segundo maior país do mundo?",
    "Quem foi o pintor do teto da Capela Sistina?",
    "Quantos anos tem um século?",
    "Quem foi o primeiro rei do Brasil?",
    "Quem foi o criador da teoria da relatividade?",
    "Quem é conhecido como o 'pai da psicanálise'?",
    "Qual é a montanha mais alta do mundo?",
    "Qual o professor mais legal?",
    "Qual capital Franca",
    "capital Franca"
]

# Vetor de respostas
respostas = [
    "Brasília",
    "Júpiter",
    "Miguel de Cervantes",
    "Sete",
    "Au",
    "Leonardo da Vinci",
    "Neil Armstrong",
    "Antoine de Saint-Exupéry",
    "Oceano Pacífico",
    "Deodoro da Fonseca",
    "H2O",
    "Três",
    "Isaac Newton",
    "Canadá",
    "Michelangelo",
    "Cem anos",
    "Dom Pedro I",
    "Albert Einstein",
    "Sigmund Freud",
    "Monte Everest",
    "Yan Carlos",
    "Paris",
    "Paris"
]

base_treino_teste = []
for i in range(len(perguntas)):
    base_treino_teste.append(perguntas[i])
    base_treino_teste.append(respostas[i])


time.clock = time.time

bot = ChatBot('TW Chat Bot')
bot.storage.drop()

trainer = ListTrainer(bot)
trainer.train(base_treino_teste)
#pergunta = input("Qual a sua dúvida?: ")
#resposta = bot.get_response(pergunta)
#print(bot.get_response(pergunta))
#print(str(resposta.confidence*100) + "%")

conversa = []

## GUI ##

janela = Tk()

janela.geometry("400x350+540+360")


txt = Text(height=10, width=61, background="white")
txt.grid(row=0, column=0)
txt.configure(state=DISABLED)

txt_send = Text(height=3, width=61, background="grey")
txt_send.grid(row=2, column=0)

btn_send= Button(height=2, width=60, background="red", text="enviar", command= lambda : enviar())
btn_send.grid(row=3, column=0)


#pergunta = input("Qual a sua dúvida?: ")
#resposta = bot.get_response(pergunta)
#print(bot.get_response(pergunta))
#print(str(resposta.confidence*100) + "%")


def enviar():
    txt.configure(state=NORMAL)
    txt.insert(END, "eu disse: " + txt_send.get('1.0', END))
    pergunta = txt_send.get('1.0', END)
    txt_send.delete("1.0", END)
    txt.configure(state=DISABLED)
    resposta(pergunta)

def resposta(perg):
    txt.configure(state=NORMAL)
    txt.insert(END, "CHAT-BOT disse: " + str(bot.get_response(perg)) + "\n")
    txt.insert(END, str(bot.get_response(perg).confidence*100) + "%" + "\n" )
    txt_send.delete("1.0", END)
    txt.configure(state=DISABLED)


janela.mainloop()