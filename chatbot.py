from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer 
import os

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

#since training has done we  can scip the trained part 
while True:
     message = input('You :')
     if message.strip()!='Bye':
         
         reply =  bot.get_response(message)
         print('ChatBot : ',reply)
     if message.strip() == 'Bye':
          print('ChatBot : Bye')
          break
         
