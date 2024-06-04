from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

import time
time.clock = time.time

bot = ChatBot('TW Chat Bot')
bot.storage.drop()

trainer = ListTrainer(bot)
trainer.train(conversa)
pergunta = 
resposta = bot.get_response(pergunta)
taxa_acerto = resposta.confidence*100

conversa = []