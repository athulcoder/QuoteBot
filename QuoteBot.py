import requests
import datetime


class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    #url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update


F = 'https://www.pinterest.com/blissquote/friendship-quotes-and-sayings/'
token = "1903906828:AAGdBHc5AIkDTdIvqCSlkjU2DtJbyenaeEk"
magnito_bot = BotHandler(token)
Quotes = 'https://verybestquotes.com/'


def main():
    new_offset = 0
    c = "QuoteBot Is Online ..."
    print(c.upper())

    while True:
        all_updates = magnito_bot.get_updates(new_offset)

        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)
                first_update_id = current_update['update_id']
                if 'text' not in current_update['message']:

                    first_chat_text = 'Old member'
                else:
                    first_chat_text = current_update['message']['text']
                first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat'][
                        'first_name']
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message'][
                        'new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from'][
                        'first_name']
                else:
                    first_chat_name = "unknown"

                if first_chat_text in ("Hi", "Hello", "Hai", "Hello QuoteBot",
                                       "Hello QuoteBot", "hi", "hai",
                                       "Hello QuoteBot!", "Hi Quoter",
                                       'Hi Quoter.', "Hi QuoteBot!"):

                    magnito_bot.send_message(
                        first_chat_id,
                        'Hello ' + first_chat_name,
                    )
                    new_offset = first_update_id + 1
                if first_chat_text == '/start':
                    magnito_bot.send_message(
                        first_chat_id,
                        "   Hi !My Name is QuoteBot  How Are you " +
                        first_chat_name)
                    new_offset = first_update_id + 1
                if first_chat_text == 'Love':
                    magnito_bot.send_message(
                        first_chat_id,
                        'Love http://www.planetofsuccess.com/blog/2016/short-love-quotes/'
                    )
                    new_offset = first_update_id + 1

                if first_chat_text == 'Friendship':
                    magnito_bot.send_message(
                        first_chat_id,
                        'Frendship Quotes https://www.pinterest.com/blissquote/friendship-quotes-and-sayings/'
                    )
                    new_offset = first_update_id + 1

                if first_chat_text in ("I am Fine", "I am Good", "I am fine",
                                       'I am Fine.', 'I am good', 'I am good.',
                                       'I am Good.', 'I am Well', 'I am Well.',
                                       'Well', 'Going Good', 'Good', 'good.',
                                       'good', 'Good.', "I'm fine",
                                       "I'm fine.", "I'm Good.", "I'm Good",
                                       "I'm Fine", "I'm Fine.", "Fine", "fine",
                                       "Fine.", "fine."):
                    magnito_bot.send_message(
                        first_chat_id,
                        'Well, What type of Quote you need? "Friendship" , "Love", "Attitude","Famous Quotes"  For this Type Extactly What I have sent'
                    )
                    new_offset = first_update_id + 1
                if first_chat_text == 'Attitude':
                    magnito_bot.send_message(
                        first_chat_id,
                        'Attitude  Quotes https://quotesjin.com/attitude-quotes/'
                    )
                    new_offset = first_update_id + 1
                if first_chat_text == 'Famous Quotes':
                    magnito_bot.send_message(
                        first_chat_id,
                        'Famous Quotes https://blog.hubspot.com/sales/famous-quotes'
                    )
                    new_offset = first_update_id + 1
                if first_chat_text in ('Thankyou', 'Thank you', 'Thankyou.',
                                       'Thanks', 'thanks', 'thankyou'):
                    magnito_bot.send_message(
                        first_chat_id,
                        'Your Welcome ' + first_chat_name,
                    )
                    new_offset = first_update_id + 1


if __name__ == '__main__':

    try:

        main()

    except KeyboardInterrupt:

        exit()
