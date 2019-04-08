from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer 
import os

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)
for files in os.listdir('D:/minor project/chatterbot-corpus-maaster_KIIT\chatterbot_corpus\data\english/'):      #('C:/Users/chatterbot-corpus-master\chatterbot_corpus\data\english/'):
    
    data = open('D:/minor project/chatterbot-corpus-maaster_KIIT\chatterbot_corpus\data\english/' + files, 'r').readlines()          #('C:/Users/chatterbot-corpus-master\chatterbot_corpus\data\english/' + files,'r').readlines()
    bot.train(data)
    print("Training")
print("completly trained")
while True:
     message = input('You :')
     if message.strip()!='Bye':
         
         reply =  bot.get_response(message)
         print('ChatBot : ',reply)
     if message.strip() == 'Bye':
          print('ChatBot : Bye')
          break
         
     
        
  
 
