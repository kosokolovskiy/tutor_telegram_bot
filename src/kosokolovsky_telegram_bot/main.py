import requests
from telegram.ext import ApplicationBuilder, CommandHandler
from telegram.helpers import escape_markdown

class MyBot:

    @staticmethod
    def send_notification(username, chat_id, api_url=None):
        if api_url:
            message = f'Homework is added successfully for {username}'
            requests.post(api_url, data={'chat_id': chat_id, 'text': message})
        else:
            print("Chat ID is not found!")

    @staticmethod
    def send_notification_free(chat_id, api_url, message):
        if api_url:
            requests.post(api_url, data={'chat_id': chat_id, 
                                         'text': message,
                                         'parse_mode': 'MarkdownV2'
                                         })
        else:
            print("Chat ID is not found!")
        

    @staticmethod
    async def get_id(update, context):
        chat_id = update.effective_chat.id
        await context.bot.send_message(chat_id=chat_id, text=f'Your chat_id: {chat_id}')

    @staticmethod
    async def check(update, context):
        chat_id = update.effective_chat.id
        message = context.bot_data.get(f"custom_message_{chat_id}", "✅ Everything is done, take your time!")
        
        # safe_message = escape_markdown(message, version=2)
        
        await context.bot.send_message(chat_id=chat_id, text=message, parse_mode='MarkdownV2')
        await context.bot.send_message(chat_id=972843253, text=message, parse_mode='MarkdownV2')

    @staticmethod
    def send_formatted_message(app, chat_id, message):
        key = f"custom_message_{chat_id}"
        app.bot_data[key] = message



    @staticmethod
    def run_bot(token):
        print("Starting Telegram bot...")
        app = ApplicationBuilder().token(token).build()
        app.add_handler(CommandHandler('get_id', MyBot.get_id))
        app.add_handler(CommandHandler('check', MyBot.check))
        # app.run_polling()
        return app
