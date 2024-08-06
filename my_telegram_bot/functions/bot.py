import os
import json
from flask import Flask, request
import telegram

TOKEN = os.getenv('TOKEN')
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    message_id = update.message.message_id

    text = update.message.text.encode('utf-8').decode()
    bot.sendMessage(chat_id=chat_id, text="Hello! You said: {}".format(text), reply_to_message_id=message_id)

    return 'ok'

def handler(event, context):
    with app.app_context():
        response = webhook()
    return {
        'statusCode': 200,
        'body': response
    }
