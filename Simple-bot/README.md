# SIMPLE TELEGRAM BOT
Telegram bot on any topic

Python version: Python 3.9


Python Packages were used: pyTelegramBotAPI


What was used:

```Python
# Обработка кнопки /start
@bot.message_handler(commands=['start'])
def start(message):

 # Обработка кнопки /help   
@bot.message_handler(commands=['help'])
def start_message(message):
   
# Обработка кнопки /wishes
@bot.message_handler(commands=['wishes'])
def wish_message(message):
    
# Обработка кнопки /animals
@bot.message_handler(commands=['animals'])
def get_text_messages(message):
    
# Обработка кнопок для вывода одного из нескольких изображений
@bot.callback_query_handler(func=lambda call: True)

# Обработка кнопки /music
@bot.message_handler(commands=['music'])
def wish_message(message):
    
# Обработка сообщений введенных пользователем
@bot.message_handler(content_types=['text'])
def answer(message):
   
```
**Resalt my work**

![image](https://user-images.githubusercontent.com/90320554/146654726-11bf51d7-5828-4565-9cab-6368d5359bc6.png)
