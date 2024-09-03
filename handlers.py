import re
from telebot import types
from config import URLS, user_data,user_states
from services import fetch_data
from plots import ploting_of_data
import threading
import time

# Regular expression for validating an Email
email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

STATE_EMAIL = 1
STATE_PASSWORD = 2
STATE_TRACK = 3

def start_handler(message, bot):
    bot.send_message(message.chat.id, 'Welcome to *Rollwala Attendance Visualizer*. \n\n *Send Email Address : *', parse_mode='Markdown')
    # bot.send_message(message.chat.id, '*Send Your Email Address and Then Password of Attendance System.*\n(attendence-system-1910.vercel.app) \n\n ', parse_mode='Markdown')
    # bot.send_message(message.chat.id, '🫶🏻BOT Created and Deployed BY : @jay_3103 \n Visualizing Script BY : @ironman_unofficial')
    # bot.send_message(message.chat.id, '*Send Email Address : *', parse_mode='Markdown')

    user_states[message.chat.id] = STATE_EMAIL

def message_handler_func(message, bot):
    user_id = message.chat.id
    user_message = message.text

    if user_id not in user_states:
        user_states[user_id] = STATE_EMAIL

    if user_states[user_id] == STATE_EMAIL:
        if re.match(email_regex, user_message):
            bot.reply_to(message, f'Your email-id : {user_message}.\n\n*Please send your password.*', parse_mode='Markdown')
            user_states[user_id] = STATE_PASSWORD
            user_data[user_id] = {'email': user_message.lower()}
        else:
            bot.reply_to(message, "Please send a valid email address.")

    elif user_states[user_id] == STATE_PASSWORD:
        user_data[user_id]['password'] = user_message

        markup = types.InlineKeyboardMarkup()
        markup.row(types.InlineKeyboardButton("ML & DL Track", callback_data='0'))
        markup.row(types.InlineKeyboardButton("WebDev Track", callback_data='1'))
        
        bot.reply_to(message, "*Please select your track:*", parse_mode='Markdown', reply_markup=markup)
        user_states[user_id] = STATE_TRACK

def callback_query_handler(call, bot):
    user_id = call.message.chat.id
    if user_id in user_states and user_states[user_id] == STATE_TRACK:
        track = None
        track_code = None
        if call.data == '0':
            track = 'ML & DL Track'
            track_code = 0
        elif call.data == '1':
            track = 'Web Track'
            track_code = 1

        if track:
            user_data[user_id]['track'] = track
            user_data[user_id]['track_code'] = track_code
            email = user_data[user_id]['email']
            password = user_data[user_id]['password']

            bot.send_message(user_id, f'Email: {email}\nPassword received.\nTrack: {track}')

            # TO Give the effect to the loading animation 
            loading_message = bot.send_message(user_id, "Loading...")
            loading_message_id = loading_message.message_id
            loading_flag = threading.Event()

            def update_loading_message(message_id, chat_id):
                counter = 1
                while not loading_flag.is_set():
                    try:
                        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f"Loading{'.' * counter}")
                        counter = (counter % 3) + 1
                        time.sleep(1)
                    except Exception:
                        break
            
            loading_thread = threading.Thread(target=update_loading_message, args=(loading_message_id, user_id))
            loading_thread.start()
            #until here

            login_data = {"email": email, "password": password}
            
            data = fetch_data(URLS, login_data, user_id, bot)

            try:
                if track_code == 0:
                    data.drop('Web Security', axis=1, inplace=True)
                    data.drop('Web Security - practical', axis=1, inplace=True)
                    data.drop('Full Stack Web Development', axis=1, inplace=True)
                    data.drop('Full Stack Web Development - practical', axis=1, inplace=True)
                elif track_code == 1:
                    data.drop('Deep Learning', axis=1, inplace=True)
                    data.drop('Deep Learning - Practical', axis=1, inplace=True)
                    data.drop('Computer Vision', axis=1, inplace=True)
                    data.drop('Computer Vision - practical', axis=1, inplace=True)

            except Exception:
                bot.send_message(user_id, "Sorry Unable To Fetch Track Details, Going with Total")

            def generate_and_send_plot():
                plot_buffer = ploting_of_data(data, login_data)
                bot.send_photo(call.message.chat.id, plot_buffer)

            threading.Thread(target=generate_and_send_plot).start()

            loading_flag.set()
            bot.edit_message_text(chat_id=user_id, message_id=loading_message_id, text="* Here is your PLOT *")
            loading_thread.join()

            #clearing the states
            user_states.pop(user_id, None)
            user_data.pop(user_id, None)

            bot.answer_callback_query(call.id, f'You selected {track}')
