from flask import Flask, request
from pymessenger.bot import Bot
import random

app = Flask(__name__)
ACCESS_TOKEN = 'EAAQCQLXFEIkBAIFZAeZCmjkZCLlFLuGZAvvgEZAkND93YtMWQZCr8swNbO6AKMluZBupQmqUUbTJGumZCDLI5al824krUuW6UxlheqM4NogGlPRZCK8rvzXKHagj1XyvhLx6qk0Vo8FZAYrHLZAPk5TRZC4APKWnPwI3O1gx0v8TzPjbGcH3EqIrCbN1Aat4mEEfZCRgZD'
VERIFY_TOKEN = 'VERIFY_TOKEN'
bot = Bot(ACCESS_TOKEN)


# Take token sent by Facebook and verify if it matches the token I sent
# If they match, allow the request, if not throw 'Invalid verification token'
def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "Success"


def get_message():
    sample_responses = ["Dżem bobry", "Przykładowa wiadomość nr. 832", "Za 38 dni wiosna!"]
    return random.choice(sample_responses)


@app.route('/', methods=['GET', 'POST'])
def receive_message():
    # handling GET request to allow Facebook to checks the bot's verify token
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)

    # handling POST request to proceed Facebook to sent to bot message sent by user
    if request.method == 'POST':
        output = request.get_json()

        for event in output['entry']:
            messaging = event['messaging']

            for message in messaging:

                if message.get('message'):
                    # Facebook Messenger ID for user so we know where to send response
                    recipient_id = message['sender']['id']

                    # Handling text messages
                    if message['message'].get('text'):
                        response_sent_text = get_message()
                        send_message(recipient_id, response_sent_text)

                    # Handling non-text messages
                    if message['message'].get('attachments'):
                        response_sent_notext = get_message()
                        send_message(recipient_id, response_sent_notext)
    return "Message Proceed"


if __name__ == '__main__':
    app.run()
