# TIMETABLE BOT
A telegram bot displaying the schedule of classes for each day and week, even/odd week, a link to the university website


Python version: Python 3.9


Python Packages were used: pyTelegramBotAPI, psycopg2, datetime


What was used:

```Python
# Определение недели нижняя/верхняя
def for_weeks():
   
# Начало работы бота и задание кнопок
@bot.message_handler(commands=['start'])
def start(message):
    
# Вывод недели
@bot.message_handler(commands=['week'])
def start_message(message):
    

# Вывод кнопки /help
@bot.message_handler(commands=['help'])
def start_message(message):
    
# Вывод кнопки /mtuci
@bot.message_handler(commands=['mtuci'])
def start_message(message):
    

# Вывод расписания по дням недели и на неделю
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    
# Запрос бд для одного дня
def print_timetable(day, num_week):
```
**Resalt my work**

![image](https://user-images.githubusercontent.com/90320554/146654527-17390a69-6d5a-4e6f-beb4-e278b2a45623.png)
