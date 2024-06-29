import logging      # Для логгирования сообщений
import requests     # Для http запросов
from telegram import Update # Для работы с телеграмом
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler  # Для выполнения комманд

token = '7118744845:AAHYAUe1-i7YuZIwaW6LhDxQdljzoK3YPoU'    # Токен бота

logging.basicConfig(    # Настройки логгирования
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Функция команды старт
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    user_name = user.first_name
    user_lastname = user.last_name
    start_text = (
        f"Hello, {user_name} {user_lastname}! I'm a bot that can provide information about currencies of different countries. \n"
        "Just send me the name of a country, and I'll tell you which currency is used in that country."
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=start_text)   # Отсылаем сообщение по команде старт

# Функция команды help
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "This bot provides information about currencies of different countries. \n\n"
        "You can use the following commands:\n"
        "/start - start interacting with the bot\n"
        "/help - display this help message\n\n"
        "Simply send the name of a country, and I'll tell you which currency is used in that country."
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)    # Отсылаем сообщение help

# Функция обработки текстовых сообщений
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    country = update.message.text

    # Получаем информацию о стране
    response = requests.get(f"https://restcountries.com/v3.1/name/{country}")
    data = response.json()
    data_list = list(data)

    # В зависимости от ответа на запрос выводим данные
    if data_list and 'currencies' in data_list[0]:
        currency_name = (list(data[0]['currencies'].values())[0]['name'])
        currency_symbol = (list(data[0]['currencies'].values())[0]['symbol'])
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Currency of {country} - {currency_name} {currency_symbol}")   
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, we could not find information about the currency of this country. You may have entered an incorrect name.")

if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build() # Создаём приложение
    
    # Добавляем обработчики сообщений и команд
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(echo_handler)

    application.run_polling()