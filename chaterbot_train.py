from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer 
import os

def setup():
    bot = ChatBot('Bot')
    
    for files in os.listdir('D:/minor project/chatterbot-corpus-maaster_KIIT\chatterbot_corpus\data\english/'):         #('C:/Users/chatterbot-corpus-master\chatterbot_corpus\data\english/'):
    
        data = open('D:/minor project/chatterbot-corpus-maaster_KIIT\chatterbot_corpus\data\english/'+ files,'r')         #('C:/Users/chatterbot-corpus-master\chatterbot_corpus\data\english/' + files,'r').readlines()
        bot.set_trainer(ListTrainer)
        bot.train(data)
        print("Training complete")

setup()
print("Trained")


    



