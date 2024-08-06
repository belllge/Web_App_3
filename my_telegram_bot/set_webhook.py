import requests
import os

TOKEN = os.getenv('TOKEN')

def set_webhook():
    webhook_url = 'https://YOUR_GITHUB_USERNAME.github.io/YOUR_REPOSITORY_NAME/webhook'
    response = requests.get(f'https://api.telegram.org/bot{TOKEN}/setWebhook?url={webhook_url}')
    if response.status_code == 200:
        print('Webhook set successfully.')
    else:
        print('Failed to set webhook:', response.text)

if __name__ == '__main__':
    set_webhook()
