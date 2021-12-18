import random
import telebot
from telebot import types

token = '2105305288:AAFRlMCI6z2N5d8DRRcbR8EPKBH5LQzY9XQ'
bot = telebot.TeleBot(token)

first = [
    "Желаю хорошего, продуктивного, прекрасного дня! Пусть день пройдет легко, в хорошем настроении и расположении духа, а также без проблем и раздражений. Побольше улыбок и позитива в новом дне!",
    "От души желаю приятного, успешного и хорошего дня. Пусть он будет плодотворным и насыщенным. Пусть удастся воплотить все планы и желания. Пусть этот день принесет только радость, удачу и добрые эмоции.",
    "Хороший день — это отличная заявка на успех в любом деле! Поэтому я тебе от души желаю теплого, удачного денечка!",
    "Желаю тебе чудесного, волшебного, невероятно позитивного дня. Пусть в тебе кипит энергия, пусть все обстоятельства складываются удачно для тебя, пускай каждая мелочь приносит огромную удачу! Радостных тебе эмоций и блестящих успехов!",
    "Для слов не нужно повода! Хочу от всего сердца пожелать тебе хорошего дня. Пусть он удивит тебя своей легкостью, новостями и приятными сюрпризами.",
    "Пусть наступивший день будет наполнен положительными эмоциями и великолепным настроением. Пусть энергия и ритм сделают его знаменательным. Всего самого наилучшего!"]


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help", "/wishes", "/animals", "/music ")
    bot.send_message(message.chat.id, 'Привет! Напиши /help ,чтобы узнать о моих возможностях.', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею:')
    bot.send_message(message.chat.id, 'Присылать пожелания на день, чтобы у тебя было прекрасное настроение: /wishes')
    bot.send_message(message.chat.id, 'Могу поделиться классными фотографиями животных /animals')
    bot.send_message(message.chat.id, 'А также могу предложить успокаивающую мелодию, чтобы расслабиться /music ')
    bot.send_message(message.chat.id, 'А еще ты можешь со мной немного пообщаться, написать "Привет", спросить "Как дела?" и я с радостью тебе отвечу, и можешь мне написать "хочу" и тебя ждет кое-что интересненькое')


@bot.message_handler(commands=['wishes'])
def wish_message(message):
    bot.send_message(message.chat.id, random.choice(first))


@bot.message_handler(commands=['animals'])
def get_text_messages(message):
    keyboard = types.InlineKeyboardMarkup()
    # По очереди готовим текст и обработчик для каждого знака зодиака
    key_cat = types.InlineKeyboardButton(text='Котята', callback_data='cats')
    # И добавляем кнопку на экран
    keyboard.add(key_cat)
    key_dog = types.InlineKeyboardButton(text='Щенята', callback_data='dogs')
    keyboard.add(key_dog)
    key_bird = types.InlineKeyboardButton(text='Птички', callback_data='birds')
    keyboard.add(key_bird)
    key_another = types.InlineKeyboardButton(text='Другое', callback_data='another')
    keyboard.add(key_another)
    bot.send_message(message.from_user.id, text='Выбери одно животное', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "cats":
        photo = open('photo.jpg', 'rb')
        bot.send_photo(call.from_user.id, photo)
    elif call.data == "dogs":
        photo = open('photo1.jfif', 'rb')
        bot.send_photo(call.from_user.id, photo)
    elif call.data == "birds":
        photo = open('photo2.jpg', 'rb')
        bot.send_photo(call.from_user.id, photo)
    elif call.data == "another":
        photo = open('photo3.jpg', 'rb')
        bot.send_photo(call.from_user.id, photo)


@bot.message_handler(commands=['music'])
def wish_message(message):
    bot.send_audio(message.chat.id, open("audio5.mp3", 'rb'))


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, 'Привет! Рад тебя видеть!')
    if message.text.lower() == "как дела?" or message.text.lower() == "как дела":
        bot.send_message(message.chat.id, 'Все замечательно! А у тебя?')
    if message.text.lower() == "хорошо" or message.text.lower() == "отлично" or message.text.lower() == "нормально":
        bot.send_message(message.chat.id, 'Это здорово! Рад был пообщаться!!! Можешь посмотреть, что я умею при помощи команды /help.')
    if message.text.lower() == "music":
        bot.send_audio(message.chat.id, open("audio5.mp3", 'rb'))
    if message.text.lower() == "хочу":
        bot.send_animation(message.chat.id, open("photo0.gif", 'rb'), None, 'Я не придумала ничего интересного, так что держи прикольную гифку)')


bot.polling()
