#ChatBot .respond() implementation
from ChatBot import ChatBot
bot = ChatBot()
inp = raw_input("You- ")
print(bot.respond("hi", "hello", inp))
