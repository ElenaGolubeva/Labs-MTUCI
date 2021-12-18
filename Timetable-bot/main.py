import psycopg2
import telebot
from datetime import datetime
from telebot import types

token = '2051231108:AAESnLNX0f72viirR5uWM_I8ommbky_pBAM'
bot = telebot.TeleBot(token)

# Задание переменных для определения недели
upper = 'Сейчас идет верхняя неделя'
low = 'Сейчас идет нижняя неделя'
for_week = low
date = datetime(2021, 9, 1)

# Подключение к бд
conn = psycopg2.connect(database="timetable",
                        user="postgres",
                        password="8962240",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()

# Определение недели нижняя/верхняя
def for_weeks():
    global for_week
    time = datetime.now()
    t = int((str(time - date)).split())
    if (t // 7 + 1) % 2 ==0:
        for_week = low
    else:
        for_week = upper

# Начало работы бота и задание кнопок
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help", "/week", "/mtuci")
    keyboard.row("Понедельник", "Вторник", "Среда")
    keyboard.row("Четверг", "Пятница")
    keyboard.row("Расписание на текущую неделю")
    keyboard.row("Расписание на следующую неделю")
    bot.send_message(message.chat.id, 'Здравствуйте! Напишите /help ,чтобы узнать о моих возможностях.', reply_markup=keyboard)

# Вывод недели
@bot.message_handler(commands=['week'])
def start_message(message):
    bot.send_message(message.chat.id, for_week)

# Вывод кнопки /help
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я могу:')
    bot.send_message(message.chat.id, 'Рассказать вам расписание группы БФИ2102 как на один день, так и на всю неделю. Выберите одну из кнопок.')
    bot.send_message(message.chat.id, 'Соориентировать вас в том, какая неделя сейчас идет верхняя или нижняя: /week')
    bot.send_message(message.chat.id, 'А также прислать ссылку на сайт МТУСИ /mtuci ')

# Вывод кнопки /mtuci
@bot.message_handler(commands=['mtuci'])
def start_message(message):
    bot.send_message(message.chat.id, 'https://mtuci.ru')

# Вывод расписания по дням недели и на неделю
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if for_week == low and message.text.lower() == 'понедельник':
        num_week =1
        day = 'Понедельник'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
    elif for_week == upper and message.text.lower() == 'понедельник':
        num_week =0
        day = 'Понедельник'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
    elif for_week == low and message.text.lower() == 'вторник':
        num_week =1
        day = 'Вторник'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
    elif for_week == upper and message.text.lower() == 'вторник':
        num_week =0
        day = 'Вторник'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
    elif for_week == low and message.text.lower() == 'среда':
        num_week =1
        day = 'Среда'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
    elif for_week == upper and message.text.lower() == 'среда':
        num_week =0
        day = 'Среда'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
    elif for_week == low and message.text.lower() == 'четверг':

        bot.send_message(message.chat.id, 'В этот день пар нет')
    elif for_week == upper and message.text.lower() == 'четверг':
        num_week =1
        day = 'Четверг'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
    elif for_week == low and message.text.lower() == 'пятница':
        num_week =1
        day = 'Пятница'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
    elif for_week == upper and message.text.lower() == 'пятница':
        num_week =0
        day = 'Пятница'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
    elif for_week == low and message.text.lower() == 'расписание на текущую неделю':
        num_week = 1
        day = 'Понедельник'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
        day = 'Вторник'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
        day = 'Среда'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
        bot.send_message(message.chat.id, 'Четверг \n В этот день пар нет')
        day = 'Пятница'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
    elif for_week == upper and message.text.lower() == 'расписание на текущую неделю':
        num_week = 0
        day = 'Понедельник'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
        day = 'Вторник'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
        day = 'Среда'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
        day = 'Четверг'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
        day = 'Пятница'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
    elif for_week == upper and message.text.lower() == 'расписание на следующую неделю':
        num_week = 1
        day = 'Понедельник'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
        day = 'Вторник'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
        day = 'Среда'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
        bot.send_message(message.chat.id, 'Четверг \n В этот день пар нет')

        day = 'Пятница'
        bot.send_message(message.chat.id, print_timetable(day, num_week))

    elif for_week == low and message.text.lower() == 'расписание на следующую неделю':
        num_week = 0
        day = 'Понедельник'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
        day = 'Вторник'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
        day = 'Среда'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
        day = 'Четверг'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
        day = 'Пятница'
        bot.send_message(message.chat.id, print_timetable(day, num_week))
    # Исключение на ввод неизвестной команды
    else:
        if message.text == "Привет":
            bot.send_message(message.from_user.id, "Здравствуйте, хотите узнать расписание группы БФИ2102? Выберите одну из кнопок.")
        else:
            bot.send_message(message.from_user.id, "Я вас не понимаю. Напишите /help.")

# Запрос бд для одного дня
def print_timetable(day, num_week):
    cursor.execute("SELECT teacher.subject,teacher.full_name, timetable.num_room, timetable.start_time FROM teacher INNER JOIN timetable ON teacher.subject = timetable.subject WHERE day=%s and num_week=%s", (str(day), str(num_week)))
    mass = list(cursor.fetchall())
    massage = day
    for i in range(len(mass)):
        local_line ='\n'+'<'+ mass[i][0] + '> ' +' <' + mass[i][1]+'> ' + ' <'+ mass[i][2]+'> ' + ' <'+mass[i][3]+'> ' + '\n'
        massage += local_line
    return massage


bot.polling()