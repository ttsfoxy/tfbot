# титсфоксибот
import wikipedia
import sys
from ImageParser import YandexImage
from random import random, randint
from tfx import Tfx, Gay_band, ChatSettings, MenuSettAdm, Menu, Dp_chan, DickChat
import requests
from bs4 import BeautifulSoup
import logging
import traceback
import time
import sqlite3
import string
from telebot import types
from PIL import Image, ImageFont, ImageDraw

import telebot

# ###audio recognition
import subprocess
import uuid
import os
import speech_recognition as sr

sys.path.insert(0, 'YandexImagesParser')
r = sr.Recognizer()
language = 'ru_RU'
x = 1
if os.name != 'nt':
    from settings_linx import start_dir, id_bot, database_db, lg_file, card_num, id_dick_pick
elif os.name == 'nt':
    from settings_win import start_dir, id_bot, database_db, lg_file, card_num, id_dick_pick
else:
    print('Error in system conw')
    exit()


def connectsql():                # коннект к базе
    try:
        db_path = start_dir + database_db
        conn_to_base = sqlite3.connect(db_path, timeout=15)
        return (conn_to_base)
    except Exception:
        conn_to_base.close()
        logging.error('CONNECTSQL ERROR ' + db_path + ' ' + str(traceback.format_exc()))


dick = 0
ban = []                    # лист банов в памяти (переделать)

glob_wrk = 0                # глобальный счетчик упоминаний работы (переделать в бд)

#          #################################################


def frases(message):            # функция с забавными фразами

    xxx = '@'+str(message.from_user.username)+' '+" ".join(
        frase[randint(0, 37)])
    if message.chat.id == id_dick_pick:
        return
    ress = bot.send_message(message.chat.id, xxx)
    time.sleep(10)
    bot.delete_message(message.chat.id, ress.message_id)


def sunczy(message):                     # отправляем соо из сунцзы
    xxx = " ".join(sund[randint(0, 204)])
    ress = bot.send_message(message.chat.id, xxx)
    time.sleep(10)
    bot.delete_message(message.chat.id, ress.message_id)


def karma(message):
    chsett = ChatSettings(logging, connectsql)
    if bot.get_chat(message.chat.id).type == 'private':
        return
    if (message.reply_to_message is not None and 'спасибо' in
        message.text.lower() or message.text.startswith('+')) or 'спc' in \
        message.text.lower() \
        or 'сяп' in message.text.lower() \
            and message.reply_to_message.from_user.id != message.from_user.id:
        if not chsett.get_sett_dict(message.chat.id)['karma']:
            x = bot.reply_to(message, 'Извините но администратор запретил карму в этом чате')
            time.sleep(3)
            bot.delete_message(x.chat.id, x.id)
            chsett = 0
            return
        krm_add(message.reply_to_message.from_user.id,
                message.reply_to_message.from_user.first_name, message.chat.id)

        msg_ret = str(krm_get(message.reply_to_message.from_user.id,
                              message.chat.id))

        if message.reply_to_message.from_user.username is None:
            user_to = message.reply_to_message.from_user.first_name
        else:
            user_to = message.reply_to_message.from_user.username
        if message.from_user.username is None:
            user_from = message.from_user.first_name
        else:
            user_from = message.from_user.username

        bot.send_message(message.chat.id, f'{user_to}\nУвеличение рейтинга на\
                                    1  🟢\nBсего: {msg_ret} \nот @{user_from} ')
    elif (message.reply_to_message is not None and
          message.text.startswith('-')) \
            and message.reply_to_message.from_user.id != message.from_user.id:
        krm_sub(message.reply_to_message.from_user.id,
                message.reply_to_message.from_user.first_name, message.chat.id)

        msg_ret = str(krm_get(message.reply_to_message.from_user.id,
                              message.chat.id))

        if message.reply_to_message.from_user.username is None:
            user_to = message.reply_to_message.from_user.first_name
        else:
            user_to = message.reply_to_message.from_user.username
        if message.from_user.username is None:
            user_from = message.from_user.first_name
        else:
            user_from = message.from_user.username

        bot.send_message(message.chat.id, f'{user_to}\nУменьшение рейтинга на \
                                             1  🔴\nBсего: {msg_ret} \nот \
                                             @{user_from} ')


def name_user(message):
    if message.from_user.username is None:
        user_from = message.from_user.first_name
    else:
        user_from = message.from_user.username
    return (user_from)


def krm_add(id, name, chat_id, flag=False):
    try:
        if flag:
            conn = connectsql()
            conn.execute("DELETE  from likes where  id=? AND chat_id=?",
                         (id, chat_id,))
            conn.commit()
            conn.close()
            return (True)
        conn = connectsql()
        info = conn.execute("SELECT * FROM likes where id=? AND chat_id=?",
                            (id, chat_id))
        if info.fetchone() is None:  # если нет в базе этого человека
            conn.execute("INSERT INTO likes(id,name,chat_id,points) \
            values(?,?,?,?)", (id, name, chat_id, 1))
            conn.commit()
            conn.close()
            return (True)
        else:
            conn.execute('UPDATE likes SET points=points + 1 where id=? \
                AND chat_id=?', (id, chat_id))
            conn.commit()
            conn.close()
            return (True)
    except Exception:
        logging.error('KRM ADD' + str(traceback.format_exc()))
        return (False)


def krm_sub(id, name, chat_id, flag=False):
    try:
        if flag:
            conn = connectsql()
            conn.execute("DELETE  from likes where  id=? AND chat_id=?", (id,
                         chat_id,))
            conn.commit()
            conn.close()
            return (True)
        conn = connectsql()
        info = conn.execute("SELECT * FROM likes where id=? AND chat_id=?",
                            (id, chat_id))
        if info.fetchone() is None:  # если нет в базе этого человека
            conn.execute("INSERT INTO likes(id,name,chat_id,points) \
                         values(?,?,?,?)", (id, name, chat_id, 0))
            conn.commit()
            conn.close()

            return (True)
        else:
            conn.execute('UPDATE likes SET points=points - 1 where id=? AND \
                chat_id=?', (id, chat_id))
            conn.commit()
            conn.close()
            return (True)
    except Exception:
        logging.error('KRM SUB' + str(traceback.format_exc()))
        return (False)


def krm_get(id, chat_id):
    conn = connectsql()
    info = conn.execute("SELECT * FROM likes where id=? AND chat_id=?",
                        (id, chat_id))
    date = info.fetchone()
    if date is None:
        return (False)
    conn.close()
    return (date[3])


def krm_get_top(message):
    if bot.get_chat(message.chat.id).type == 'private':
        return
    sett = ChatSettings(logging, connectsql)
    if not sett.get_sett_dict(message.chat.id)['karma']:
        x = bot.reply_to(message, 'Извините но администратор запретил карму в этом чате')
        time.sleep(3)
        bot.delete_message(x.chat.id, x.id)
        return
    conn = connectsql()
    info = conn.execute("SELECT * From likes where chat_id=? \
                        ORDER BY points DESC", (message.chat.id,))
    date = info.fetchmany(10)
    text_out = ''
    try:
        for tmp_d in date:
            text_out = text_out+'\n'+tmp_d[1]+'  '+str(tmp_d[3])
        file_name_full = krm_viev(date, 'wrk.jpg')
        img = open(file_name_full, 'rb')
        bot.send_photo(message.chat.id, img, reply_to_message_id=message.id)
        img.close()
        os.remove(file_name_full)
    except Exception:
        # print(str(traceback.format_exc()))
        logging.error('KRM GET_TOP ' + str(traceback.format_exc()))
        conn.close()
    conn.close()

# ################################################   РАЗДЕЛ СТАТИСТИКА


def statist(message):
    try:
        if bot.get_chat(message.chat.id).type == 'private':
            return
        # sett = ChatSettings(logging, connectsql)        # если запрет в бд на статку
        # if not sett.get_sett_dict(message.chat.id)['stat']:
        #     return
        name = message.from_user.first_name
        if message.from_user.username is None:
            name = message.from_user.first_name
        else:
            name = message.from_user.username
        if message.from_user.username is None:
            name = message.from_user.first_name
        else:
            name = message.from_user.username

        id_user = message.from_user.id
        id_chat = message.chat.id
        stat_add(name, id_user, id_chat)
    except Exception:
        logging.error('у меня ошибка в statist' + str(traceback.format_exc()))


def stat_add(name, id_user, id_chat):
    try:
        conn = connectsql()
        info = conn.execute("SELECT * FROM states where id_user=? AND id_chat=?",
                            (id_user, id_chat))
        if info.fetchone() is None:  # если нет в базе этого человека
            conn.execute("INSERT INTO states(id_user,name,id_chat,points) \
                        values(?,?,?,?)", (id_user, name, id_chat, 0))
            conn.commit()
        conn.execute('UPDATE states SET points=points + 1 where id_user=? \
                    AND id_chat=?', (id_user, id_chat))
        conn.commit()
        conn.close()
    except Exception:
        logging.error('у меня ошибка в stat add' + str(traceback.format_exc()))
    finally:
        conn.close()


def stat_get_top(message):
    if bot.get_chat(message.chat.id).type == 'private':
        return
    sett = ChatSettings(logging, connectsql)
    if not sett.get_sett_dict(message.chat.id)['stat']:
        x = bot.reply_to(message, 'Извините но администратор запретил карму в этом чате')
        time.sleep(3)
        bot.delete_message(x.chat.id, x.id)
        return
    conn = connectsql()
    info = conn.execute("SELECT * From states where id_chat=? \
                        ORDER BY points DESC", (message.chat.id,))
    date = info.fetchmany(10)
    try:
        file_name_full = krm_viev(date, 'wrk1.jpg')
        img = open(file_name_full, 'rb')
        bot.send_photo(message.chat.id, img, reply_to_message_id=message.id)
        img.close()
        os.remove(file_name_full)
    except Exception:
        logging.error('stat_get_top ' + str(traceback.format_exc()))
        conn.close()
    finally:
        conn.close()


def krm_viev(date, nme):
    img = Image.open(nme)
    # 20851.ttf
    font = ImageFont.truetype('20851.ttf', size=50)
    draw_text = ImageDraw.Draw(img)
    text_out = ''
    for tmp_d in date:
        text_out = text_out+'\n'+str(tmp_d[1])
    draw_text.text(
                    (150, 50),
                    text_out,
                    # Добавляем шрифт к изображению
                    font=font,
                    fill='#ffffff')
    text_out = ''
    for tmp_d in date:
        text_out = text_out+'\n'+str(tmp_d[3])
    draw_text.text(
                    (750, 50),
                    text_out,
                    # Добавляем шрифт к изображению
                    font=font,
                    fill='#ffffff')
    filename = str(uuid.uuid4())
    filename_full = filename+'.jpg'
    # os.remove(file_name_full)
    img.save(filename_full)
    img.close()
    return (filename_full)


# #############################################audio
def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return (rand_string)
# ######################################################  S recog


def recognise(filename):
    with sr.AudioFile(filename) as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text, language=language)
            return text
        except Exception:
            return "Sorry.. что-то пошло не так..."


def is_admin(message, id=0):
    if id == 0:
        if bot.get_chat_member(message.chat.id, message.from_user.id).status == \
                            'creator' or \
                            bot.get_chat_member(message.chat.id,
                                                message.from_user.id).status \
                            == 'administrator':
            return (True)
        else:
            return (False)
    else:
        if bot.get_chat_member(message.chat.id, id).status == 'creator' or \
                            bot.get_chat_member(message.chat.id, id).status == 'administrator':
            return (True)
        else:
            return (False)


def admin_comms(message):               # ##########
    if message.text == '/add_hello':
        msg = bot.reply_to(message, 'Введите приветственное сообщение')
        bot.register_next_step_handler(msg, process_hello_step)

    if message.text == '/tst_nm':
        try:
            if os.name == 'nt':
                MenSett = MenuSettAdm(bot, logging, connectsql)
                MenSett.set_fuckin_menu(message=message)
        except Exception:
            logging.error('у меня ошибка внутренняя adm comms' +
                          str(traceback.format_exc()))
            # print('у меня ошибка внутренняя' + str(traceback.format_exc()))
    if message.text == '/start_owner':
        if bot.get_chat_member(message.chat.id, message.from_user.id).status == 'creator':
            if Settings.set_settings_chat(message.chat.id, owner=message.from_user.id):
                x = bot.reply_to(message, 'Выполнено')
                MenSett = MenuSettAdm(bot, logging, connectsql)
                MenSett.start_comm_owner(message)
                time.sleep(5)
                bot.delete_message(message.chat.id, x.message_id)
                bot.delete_message(message.chat.id, message.message_id)
            else:
                x = bot.reply_to(message, 'ERROR')
                time.sleep(10)
                bot.delete_message(message.chat.id, x.message_id)
                bot.delete_message(message.chat.id, message.message_id)
        else:
            x = bot.reply_to(message, 'Вы не владелец чата')
            time.sleep(10)
            bot.delete_message(message.chat.id, x.message_id)
            bot.delete_message(message.chat.id, message.message_id)

    if message.text.lower() == 'кто это':
        get_all_by_message(message)
    elif message.text.lower() == 'кто такой':
        get_all_by_name(message)
    elif message.text.lower() == 'твои ники':
        aka_nicks(message)
    elif '12865355 update' in message.text.lower() and message.from_user.id == 1675780013:
        texts = message.text[16:]
        Tf_cl.changes_write(texts)
    elif '12865355 send' in message.text.lower():
        try:
            tmp_var = Tf_cl.changes_read_last()
            snd_text = f'{time.ctime(tmp_var[1][0][0])}  \n{tmp_var[1][0][1]}'
            for x in chat_list:
                try:
                    bot.send_message(x[0], snd_text)
                except Exception:
                    logging.error(f'ERROR send updates of bot  to {x[0]}' + str(traceback.format_exc()))

        except Exception:

            logging.error('ERROR send updates of bot ' + str(traceback.format_exc()))
    if message.text == 'tst_st':
        stat_get_top(message)


def process_hello_step(message):
    try:
        conn = connectsql()
        conn.execute("REPLACE INTO new_member_hello(id,mess) values(?,?)",
                     (message.chat.id, message.text))
        conn.commit()
        conn.close()
        x = bot.reply_to(message, 'Запрос выполнен!')
        time.sleep(5)
        bot.delete_message(x.chat.id, x.message_id)
    except Exception:
        logging.error('process_hello_step ' + str(traceback.format_exc()))
    finally:
        conn.close()


def send_hello_mess(message, text):
    keyboard = types.InlineKeyboardMarkup()

    callback_button_1 = types.InlineKeyboardButton(text="Я прочиталь",
                                                   callback_data=('cat'))
    keyboard.add(callback_button_1)
    bot.send_message(message.chat.id, f'Добро пожаловать \
        {message.from_user.first_name} \n{text}', reply_markup=keyboard)


def show_guyness(message, from_user=''):
    try:
        if bot.get_chat(message.chat.id).type == 'private':
            return
        sett = ChatSettings(logging, connectsql)
        if not sett.get_sett_dict(message.chat.id)['guiness']:
            x = bot.reply_to(message, 'Извините но администратор запретил меряться членами в этом чате')
            time.sleep(3)
            bot.delete_message(x.chat.id, x.id)
            return
        keyboard = types.InlineKeyboardMarkup()
        if from_user != '':
            callback_button_1 = types.InlineKeyboardButton(text="Узнать свой результат 🏳️‍🌈",
                                                           callback_data=('guyness'))
            keyboard.add(callback_button_1)
            gness = randint(0, 100)
            bot.send_message(message.chat.id, f'{from_user.first_name} гей на {gness}%  🏳️‍🌈',
                             reply_markup=keyboard)
        else:
            callback_button_1 = types.InlineKeyboardButton(text="Узнать свой результат 🏳️‍🌈",
                                                           callback_data=('guyness'))
            keyboard.add(callback_button_1)
            gness = randint(0, 100)
            bot.send_message(message.chat.id, f'{message.from_user.first_name} гей на {gness}% 🏳️‍🌈',
                             reply_markup=keyboard)

    except Exception:
        logging.error('SHOW GUYNESS ' + str(traceback.format_exc()))


def okg(message):
    try:
        if 'ok google' in message.text.lower() or 'okey google' \
            in message.text.lower() or message.text.lower() == 'ок' \
            or 'ок гугл' in message.text.lower() or 'окей гугл' \
                in message.text.lower() or 'гугл' == message.text.lower() \
                or 'google' in message.text.lower():
            sett = ChatSettings(logging, connectsql)
            if bot.get_chat(message.chat.id).type != 'private':
                if not sett.get_sett_dict(message.chat.id)['ok']:
                    x = bot.reply_to(message, 'Извините но администратор запретил OK поиск в этом чате')
                    time.sleep(3)
                    bot.delete_message(x.chat.id, x.id)
                    return
                x = Tf_cl.ok_google(message)
                if x == 0:
                    return
                if hasattr(message, 'photo'):
                    menu = Menu(bot, logging)
                    menu.menu_okg(x)
            else:
                x = Tf_cl.ok_google(message)
                if x == 0:
                    return
                if hasattr(message, 'photo'):
                    menu = Menu(bot, logging)
                    menu.menu_okg(x)
    except Exception:
        bot.reply_to(message, 'Извините но ничего не найдено, либо это баг 0')
        logging.error('у меня ошибка в okey goo' + str(traceback.format_exc()))


def para(message):      # пара дня
    try:
        sett = ChatSettings(logging, connectsql)
        if not sett.get_sett_dict(message.chat.id)['para']:
            x = bot.reply_to(message, 'Извините но администратор запретил пару дня в этом чате')
            time.sleep(3)
            bot.delete_message(x.chat.id, x.id)
            return
        conn = connectsql()
        info = conn.execute("SELECT * FROM para where id_chat=?",
                            (message.chat.id,))
        if info.fetchone() is None:  # если нет в базе этого чата
            info = conn.execute("SELECT * From last_seen where id_chat=? \
                ORDER BY RANDOM() LIMIT 2", (message.chat.id,))
            date = info.fetchmany(2)
            conn.execute("INSERT or REPLACE INTO para(id_chat,date,id_user_1,\
                id_user_2,name_user_1,name_user_2) values(?,?,?,?,?,?)",
                         (message.chat.id, time.time(), date[0][0], date[1][0],
                          date[0][2], date[1][2]))
            user_1 = date[0][0]
            user_2 = date[1][0]
            # '[Usverb](tg://user?id=1675780013)',parse_mode='MarkdownV2'
            username_1 = date[0][2]
            username_2 = date[1][2]
            snd_msg = f'Пара дня: [{username_1}](tg://user?id={user_1}) \+ [{username_2}]' +\
                      f'(tg://user?id={user_2}) Целуйтесь :\)'  # noqa
            try:
                bot.reply_to(message, snd_msg, parse_mode='MarkdownV2')
            except Exception:
                bot.reply_to(message, f'Пара дня: @{username_1} + @{username_2} \n  Целуйтесь :)')
            finally:
                conn.commit()
                conn.close()
        else:
            info = conn.execute("SELECT * FROM para where id_chat=?",
                                (message.chat.id,))
            date = info.fetchone()
            if date[1] > (time.time()-86400):  # Новая пара дня в else
                tmes = (86400-(time.time()-date[1]))//3600
                str_tmes = str(int(tmes))
                username_1 = date[4]
                userid_1 = date[2]
                username_2 = date[5]
                userid_2 = date[3]
                conn.close()
                snd_msg = f'Пара дня: [{username_1}](tg://user?id={userid_1}) \+ ' +\
                          f'[{username_2}](tg://user?id={userid_2}) перевыбор доступен через ' +\
                          f'{str_tmes} часа\(часов\) '  # noqa
                try:
                    bot.reply_to(message, snd_msg, parse_mode='MarkdownV2')
                except Exception:
                    bot.reply_to(message, f'Пара дня: @{username_1} + @{username_2} \n  Целуйтесь :)')
            else:
                conn.execute('DELETE FROM para where id_chat=?', (message.chat.id,))
                info = conn.execute("SELECT * From last_seen where id_chat=? \
                                    ORDER BY RANDOM() LIMIT 2", (message.chat.id,))
                date = info.fetchmany(2)
                conn.execute("REPLACE INTO para(id_chat,date,\
                    id_user_1,id_user_2,name_user_1,name_user_2) \
                        values(?,?,?,?,?,?)",
                             (message.chat.id, time.time(), date[0][0], date[1][0],
                              date[0][2], date[1][2]))
                conn.commit()
                conn.close()
                username_1 = date[0][2]
                username_2 = date[1][2]
                user_1 = date[0][0]
                user_2 = date[1][0]
                snd_msg = f'Новая пара дня: [{username_1}](tg://user?id={user_1}) \+ [{username_2}]' +\
                          f'(tg://user?id={user_2}) Целуйтесь :\)'  # noqa
                try:
                    bot.reply_to(message, snd_msg, parse_mode='MarkdownV2')
                except Exception:
                    bot.reply_to(message, f'Новая пара дня: @{username_1} + @{username_2} \n  Целуйтесь :)')
    except Exception:
        bot.reply_to(message, 'Error in para')
        logging.error('PARA ERROR ' + str(traceback.format_exc()))
        logging.error('\n' + snd_msg)


def last_seen(message):     # отсев тех кого давно не было
    try:
        if bot.get_chat(message.chat.id).type == 'private':
            return
        Tf_cl.chat_check(chat_list, message)  # проверка есть ли этот чат в списке чатов
        conn = connectsql()
        info = conn.execute("SELECT * From last_seen WHERE id_chat=? AND \
            id_user=?", (message.chat.id, message.from_user.id))
        if info.fetchone() is None:
            conn.execute("INSERT INTO last_seen(id_user,id_chat,Name,date)\
                 values (?,?,?,?)", (message.from_user.id, message.chat.id,
                                     name_user(message), time.time()))
            conn.commit()
            conn.close()
        else:
            info = conn.execute("SELECT * From last_seen WHERE id_chat=? \
                AND id_user=?", (message.chat.id, message.from_user.id))
            date = info.fetchone()
            his_time = date[3]
            if ((time.time()-his_time) > 86400):
                conn.execute("DELETE FROM last_seen where id_user=? and id_chat=?",
                             (message.from_user.id, message.chat.id))
                conn.execute("REPLACE INTO last_seen(id_user,id_chat,Name,\
                    date) values (?,?,?,?)",
                             (message.from_user.id, message.chat.id,
                              name_user(message), time.time()))
                conn.commit()
                conn.close()
            conn.close()
    except Exception:
        conn.close()
        logging.error(' ERROR last seen' + str(traceback.format_exc()))


def get_in(message):  # когда юзер зашел
    conn = connectsql()
    conn.execute("INSERT INTO get_in(id,id_chat,name,date_in) values(?,?,?,?)",
                 (message.from_user.id, message.chat.id, name_user(message),
                  time.time()))
    conn.commit()
    conn.close()


def get_out(message):  # когда юзер вышел
    conn = connectsql()
    conn.execute("INSERT INTO get_out(id,id_chat,name,date_out) values(?,?,?,?)",
                 (message.from_user.id, message.chat.id, name_user(message),
                  time.time()))
    conn.commit()
    conn.close()


def get_all_by_name(message):
    if message.reply_to_message:
        srch_txt = message.reply_to_message.text
        conn = connectsql()
        info = conn.execute("SELECT * FROM get_in where name=?", (srch_txt,))
        if info.fetchone() is None:

            try:
                bot.send_message(message.from_user.id, f'Извините ничего не \
                    найдено по запросу {srch_txt}')
            except Exception:
                bot.reply_to(message, 'Для успешной активации команды нужно \
                    написать боту в личку хотябы 1 раз')
        else:
            info = conn.execute("SELECT * FROM get_in where name=?", (srch_txt,))
            date = info.fetchone()
            info = conn.execute("SELECT * FROM get_in where id=?", (date[0],))
            date = info.fetchall()
            res = 'id // Nicknames // Присоеденялся к чату\n'
            for x in date:
                res = res+str(x[0])+' '+str(x[2]+'   '+str(time.ctime(x[3]))+'\n')

            res = res+'id // Nicknames // Выходил из чата\n'

            info = conn.execute("SELECT * FROM get_out where name=?", (srch_txt,))
            if info.fetchone() is None:
                res = res+(f'Извините выходов из чата не обнаружено по \
                            запросу {srch_txt}')
            else:
                info = conn.execute("SELECT * FROM get_out where name=?", (srch_txt,))
                date = info.fetchone()
                info = conn.execute("SELECT * FROM get_out where id=?", (date[0],))
                date = info.fetchall()
                for x in date:
                    res = res+str(x[0])+' '+str(x[2]+' '+str(time.ctime(x[3]))+'\n')

            try:
                bot.send_message(message.from_user.id, res)
            except Exception:
                bot.reply_to(message, 'Для успешной активации команды нужно\
                            написать боту в личку хотябы 1 раз')
        conn.close()
    else:
        bot.reply_to(message, 'Эта команда должна быть ответом на сообщение!')
    bot.delete_message(message.chat.id, message.id)


def get_all_by_message(message):
    if message.reply_to_message:
        srch_txt = message.reply_to_message.from_user.id
        conn = connectsql()
        info = conn.execute("SELECT * FROM get_in where id=?", (srch_txt,))
        if info.fetchone() is None:
            try:
                bot.send_message(message.from_user.id, f'Извините ничего \
                    не найдено по запросу {srch_txt}')
            except Exception:
                bot.reply_to(message, 'Для успешной активации команды нужно \
                                    написать боту в личку хотябы 1 раз')
        else:
            info = conn.execute("SELECT * FROM get_in where id=?", (srch_txt,))
            date = info.fetchall()
            res = 'id // Nicknames // Присоеденился к чату\n'
            for x in date:
                res = res+str(x[0])+' '+str(x[2]+'   '+str(time.ctime(x[3]))+'\n')

            res = res+'id // Nicknames // Выходил из чата\n'

            info = conn.execute("SELECT * FROM get_out where id=?", (srch_txt,))
            if info.fetchone() is None:
                res = res+(f'Извините выходов из чата не обнаружено запросу {srch_txt}')
            else:
                info = conn.execute("SELECT * FROM get_out where id=?", (srch_txt,))
                date = info.fetchall()
                for x in date:
                    res = res+str(x[0])+' '+str(x[2]+' '+str(time.ctime(x[3]))+'\n')
            # bot.reply_to(message,res)
            try:
                bot.send_message(message.from_user.id, res)
            except Exception:
                bot.reply_to(message, 'Для успешной активации команды нужно \
                    написать боту в личку хотябы 1 раз')
        conn.close()
    else:
        bot.reply_to(message, 'Эта команда должна быть ответом на сообщение!')
    bot.delete_message(message.chat.id, message.id)


def aka_nicks(message):
    if message.reply_to_message:
        srch_txt = message.reply_to_message.from_user.id
        conn = connectsql()
        info = conn.execute("SELECT * FROM get_in where id=?", (srch_txt,))
        if info.fetchone() is None:
            try:
                bot.send_message(message.from_user.id, f'Извините ничего не \
                    найдено по запросу {srch_txt}')
            except Exception:
                bot.reply_to(message, 'Для успешной активации команды нужно \
                    написать боту в личку хотябы 1 раз')
        else:
            info = conn.execute("SELECT * FROM get_in where id=?", (srch_txt,))
            date = info.fetchall()
            res = 'Nicknames ''aka''\n'
            for x in date:
                res = res+str(x[2]+'\n')

            info = conn.execute("SELECT * FROM get_out where id=?", (srch_txt,))
            if info.fetchone() is None:
                res = res+(f'Извините ничего не найдено по запросу {srch_txt}')
            else:
                info = conn.execute("SELECT * FROM get_out where id=?", (srch_txt,))
                date = info.fetchall()
                for x in date:
                    res = res+str(x[2]+'\n')
            # bot.reply_to(message,res)
            try:
                bot.send_message(message.from_user.id, res)
            except Exception:
                bot.reply_to(message, 'Для успешной активации команды нужно \
                    написать боту в личку хотябы 1 раз')
        conn.close()
    else:
        bot.reply_to(message, 'Эта команда должна быть ответом на сообщение!')
    bot.delete_message(message.chat.id, message.id)


def last_seen_query(message):
    if message.reply_to_message:
        conn = connectsql()
        info = conn.execute("SELECT * From last_seen WHERE id_chat=? \
            AND id_user=?", (message.chat.id,
                             message.reply_to_message.from_user.id))
        date = info.fetchone()
        res = 'Последняя активность пользователя:\n'
        res = res+date[2]+' '+str(time.ctime(date[3]))
        try:
            bot.send_message(message.from_user.id, res)
        except Exception:
            bot.reply_to(message, 'Для успешной активации команды нужно\
                 написать боту в личку хотябы 1 раз')
    else:
        bot.reply_to(message, 'Эта команда должна быть ответом на сообщение!')
    bot.delete_message(message.chat.id, message.id)


def long_sword(message, from_user='', id=0):
    try:
        if bot.get_chat(message.chat.id).type == 'private':
            return
        sett = ChatSettings(logging, connectsql)
        if not sett.get_sett_dict(message.chat.id)['guiness']:
            x = bot.reply_to(message, 'Извините но администратор запретил меряться членами в этом чате')
            time.sleep(3)
            bot.delete_message(x.chat.id, x.id)
            return
        # 1983664617 1675780013
        tme = time.time()
        if id == 0:
            gness = Tf_cl.longsword_strt(message.from_user.id, message.chat.id, message.from_user.first_name,
                                         tme)[0]
        else:
            gness = Tf_cl.longsword_strt(id, message.chat.id, from_user.first_name,
                                         tme)[0]

        if from_user != '':
            x = bot.send_message(message.chat.id, f'у @{from_user.first_name} член {str(gness)} ' +
                                                  'см на эти сутки')
            menu = Menu(bot, logging)
            menu.menu_dick(x)
        else:
            x = bot.send_message(message.chat.id, f'у @{message.from_user.first_name} член' +
                                                  f' {str(gness)} см 🏳️')
            menu = Menu(bot, logging)
            menu.menu_dick(x)
    except Exception:
        logging.error('LONG SWORD BUG' + str(traceback.format_exc()))


def dicker(message):
    global dick
    if dick == 10:
        long_sword(message)
        dick = 1
        return
    dick = dick+1
    return


def send_rnd_pin(message, nme=0):
    img = Tf_cl.send_rnd_from(message)
    if img:
        keyboard = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="хочу еще!",
                                                       callback_data=('rnd_pin'))
        keyboard.add(callback_button_1)
        if nme == 0:
            bot.send_photo(message.chat.id, img, caption=f'Ня @{message.from_user.username}',
                           reply_markup=keyboard)
        else:
            bot.send_photo(message.chat.id, img, caption=f'Ня @{nme}',
                           reply_markup=keyboard)
# #####################################################################################################


# #####################################################################################################
bot = telebot.TeleBot(id_bot)

Tf_cl = Tfx(bot, randint, time, BeautifulSoup, requests, YandexImage, os,
            uuid, traceback, connectsql, start_dir, logging, types)
Gay_bnd = Gay_band(bot, logging, connectsql)
Settings = ChatSettings(logging, connectsql)
Dick_picker = DickChat(bot, logging, connectsql)
if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO, filename=(start_dir + lg_file), format="%(asctime)s \
        - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")
    logging.info('Started')
    print('start')
    sund = Tf_cl.read_sunczi(start_dir)
    frase = Tf_cl.read_frases(start_dir)  # считываем фразы в лист
    Tf_cl.readbans(ban)
    chat_list = Tf_cl.chats()

    @bot.callback_query_handler(func=lambda call: True)
    def all_query(call):
        try:

            if call.data[1] == 0:
                # print('ошибка получения аргумента в callback query')
                logging.error('ошибка получения аргумента в callback query ' + str(traceback.format_exc()))

            elif call.data == 'cat':
                bot.delete_message(call.message.chat.id, call.message.message_id)
            elif call.data == 'guyness':
                show_guyness(call.message, call.from_user)
            elif call.data == 'longsword':
                long_sword(call.message, call.from_user, call.from_user.id)
            elif call.data == 'ls_game':
                Tf_cl.longsword_game(call.message)
            elif call.data == 'spons':
                bot.send_message(call.message.chat.id, f'@{call.from_user.first_name}' +
                                 f' номер карты {card_num} Спасибо! ')
                bot.send_message(call.message.chat.id, '❤️‍🔥')
                # ❤️‍🔥

            elif call.data == 'rnd_pin':
                send_rnd_pin(call.message, call.from_user.first_name)
            elif call.data == 'pin_message':            # пиним по кнопке (переделать)

                if call.message.reply_to_message.from_user.id == call.from_user.id:
                    Tf_cl.get_file_pinned(call.message.reply_to_message)
                    x = bot.send_message(call.message.chat.id, 'Закреплено!',
                                         reply_to_message_id=call.message.reply_to_message.id)
                    # bot.delete_message(call.message.chat.id, call.message.id)
                    time.sleep(3)
                    bot.delete_message(x.chat.id, x.message_id)
                elif call.from_user.id == 1675780013:
                    Tf_cl.get_file_pinned(call.message.reply_to_message)
                    x = bot.send_message(call.message.chat.id, 'Закреплено by Tf!',
                                         reply_to_message_id=call.message.reply_to_message.id)
                    time.sleep(3)
                    bot.delete_message(x.chat.id, x.message_id)
                else:
                    x = bot.send_message(call.message.chat.id, f'Извините @{call.from_user.first_name} ' +
                                                               'но это не ваше фото')
                    time.sleep(3)
                    bot.delete_message(x.chat.id, x.message_id)
            elif call.data == 'set_add_bot' or call.data == 'unset_add_bot':
                MenSett = MenuSettAdm(bot, logging, connectsql)
                MenSett.recognize_callback(call)
                # bot.edit_message_reply_markup(call.chat.id,call.message.id,reply_markup=)
            # elif
            elif call.data == 'set_ok_bot_off' or call.data == 'set_ok_bot_on':
                MenSett = MenuSettAdm(bot, logging, connectsql)
                MenSett.recognize_callback(call)
            elif call.data == 'None':
                pass
            else:
                menu = Menu(bot, logging)
                menu.recognize_menu_comms(call)
                Dick_picker.recognize_callback(call)

        except Exception:
            # print('error in cap_query\n' + str(traceback.format_exc()))
            logging.error('error in cap_query ' + str(traceback.format_exc()))

    @bot.message_handler(content_types=['new_chat_members'])
    def new_member(message):
        try:
            get_in(message)  # записываем всех новых персонажей
            conn = connectsql()
            chat_id = message.chat.id
            info = conn.execute("SELECT * FROM new_member_hello where id=?",
                                (chat_id,))
            date = info.fetchone()
            if date is None:
                return (False)
            conn.close()
            send_hello_mess(message, date[1])

        except Exception:
            logging.error('error in new member ' + str(traceback.format_exc()))
        bot.delete_message(message.chat.id, message.message_id)

    @bot.chat_member_handler(content_types=['left_chat_member'])
    def left_member(message):
        try:
            get_out(message)  # записываем всех убегших персонажей
            bot.reply_to(message, f'{name_user(message)} Сбежал от нас')
            bot.delete_message(message.chat.id, message.message_id)
        except Exception:
            # print('Error in left member ' + str(traceback.format_exc()))
            logging.error('error in left member ' + str(traceback.format_exc()))

    # left_chat_member

    @bot.message_handler(content_types=["photo"])
    def get_photo(message):
        Dick_picker.start(message)
        sett = ChatSettings(logging, connectsql)  # если в базе запрещено возврат назад
        if not sett.get_sett_dict(message.chat.id)['menu']:
            return
        x = bot.reply_to(message, 'Меню автора фото')
        menu = Menu(bot, logging)
        menu.menu_pict(x)

    @bot.message_handler(content_types=["pinned_message"])
    def get_pinned(message):
        ChSett = ChatSettings(logging, connectsql)  # если в базе запрещено возврат назад
        if ChSett.get_settings(message.chat.id)[4]:
            keyboard = types.InlineKeyboardMarkup()
            callback_button_1 = types.InlineKeyboardButton(text="Добавить",
                                                           callback_data=('pin_message'))
            keyboard.add(callback_button_1)

            bot.send_message(message.chat.id, 'Добавить эту фотоську в бота?', reply_markup=keyboard,
                             reply_to_message_id=message.pinned_message.id)

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):

        try:
            if message.via_bot:
                x = bot.reply_to(message, ' Инлайн боты запрещены в этом чате')
                time.sleep(5)
                bot.delete_message(message.chat.id, message.message_id)
                bot.delete_message(x.chat.id, x.message_id)

            karma(message)
            statist(message)
            last_seen(message)
            okg(message)
            Dick_picker.check_start(message)
            Dick_picker.start(message)
            Tf_cl.acсio(message)
            if is_admin(message):
                admin_comms(message)
            if message.text == '/krm_top' or message.text == '/krm_top@tfoxy_bot':
                krm_get_top(message)
            elif message.text == '/stat_chan@tfoxy_bot':
                stat_get_top(message)
            if Tf_cl.banans(ban, message):
                return
            if '!ро' in message.text.lower():
                dp = Dp_chan(bot, logging)
                dp.mute_usr(message)
            Tf_cl.hellos(message, glob_wrk)
            if message.text == '/gay' or message.text == '/gay@tfoxy_bot' or 'я гей' in \
                    message.text.lower() or 'z utq' in message.text.lower():
                show_guyness(message)
            elif message.text == '/dick' or message.text == '/dick@tfoxy_bot' or 'хую' in \
                    message.text.lower() or '[eq' in message.text.lower():
                long_sword(message)
            elif 'хуй' in message.text.lower():
                dicker(message)
            elif 'пара дня' in message.text.lower() or message.text == '/shipping@SHIPPERINGbot':
                para(message)
            elif 'пидор дня' in message.text.lower() or message.text == '/pidr@tfoxy_bot':
                if bot.get_chat(message.chat.id).type == 'private':
                    return
                sett = ChatSettings(logging, connectsql)
                if not sett.get_sett_dict(message.chat.id)['gayday']:
                    x = bot.reply_to(message, 'Извините но администратор запретил эту команду в этом чате')
                    time.sleep(3)
                    bot.delete_message(x.chat.id, x.id)
                    return
                Gay_bnd.gay_select(message.chat.id)

            elif message.text == '/onime' or message.text == '/onime@tfoxy_bot' or \
                    message.text.lower() == '/онимэ' or message.text.lower() == '/анимэ' or \
                    message.text.lower() == '/ониме' or message.text.lower() == '/аниме':
                if bot.get_chat(message.chat.id).type != 'private':
                    sett = ChatSettings(logging, connectsql)
                    if not sett.get_sett_dict(message.chat.id)['ok']:
                        x = bot.reply_to(message, 'Извините но администратор запретил эту команду ' +
                                         'в этом чате')
                        time.sleep(3)
                        bot.delete_message(x.chat.id, x.id)
                        return
                    Tf_cl.ok_google(message)
                else:
                    Tf_cl.ok_google(message)
            elif ('вики' in message.text.lower()) and (message.reply_to_message is not None):
                if bot.get_chat(message.chat.id).type != 'private':
                    sett = ChatSettings(logging, connectsql)
                    if not sett.get_sett_dict(message.chat.id)['wiki']:
                        x = bot.reply_to(message, 'Извините но администратор запретил эту ' +
                                         'команду в этом чате')
                        time.sleep(3)
                        bot.delete_message(x.chat.id, x.id)
                        return
                    wikipedia.set_lang("ru")
                    tmp_mess = message.reply_to_message.text
                    tmp_mess = wikipedia.search(tmp_mess, results=1)
                    if tmp_mess:
                        tmp_wiki = wikipedia.summary(tmp_mess[0])
                    else:
                        tmp_wiki = wikipedia.summary(wikipedia.suggest(message.reply_to_message.text))
                    ress = bot.reply_to(message, tmp_wiki)
                    time.sleep(60)
                    bot.delete_message(message.chat.id, ress.message_id)
                else:
                    wikipedia.set_lang("ru")
                    tmp_mess = message.reply_to_message.text
                    tmp_mess = wikipedia.search(tmp_mess, results=1)
                    if tmp_mess:
                        tmp_wiki = wikipedia.summary(tmp_mess[0])
                    else:
                        tmp_wiki = wikipedia.summary(wikipedia.suggest(message.reply_to_message.text))
                    ress = bot.reply_to(message, tmp_wiki)
                    time.sleep(60)
                    bot.delete_message(message.chat.id, ress.message_id)

            elif message.text == '/get_photo@tfoxy_bot' or message.text == '/get_photo':  # ####
                if bot.get_chat(message.chat.id).type != 'private':
                    sett = ChatSettings(logging, connectsql)
                    if not sett.get_sett_dict(message.chat.id)['ok']:
                        x = bot.reply_to(message, 'Извините но администратор запретил поиск в этом чате')
                        time.sleep(3)
                        bot.delete_message(x.chat.id, x.id)
                        return
                    Tf_cl.ok_google(message)
                else:
                    Tf_cl.ok_google(message)
            elif message.text == '/foxy' or message.text == '/foxy@tfoxy_bot' or \
                'хочу сиськи' in message.text.lower() or 'акцио сиськи' in message.text.lower() or\
                    message.text.lower() == 'сиськи':
                if bot.get_chat(message.chat.id).type == 'private':
                    return
                sett = ChatSettings(logging, connectsql)
                if not sett.get_sett_dict(message.chat.id)['foxy']:
                    x = bot.reply_to(message, 'Извините но администратор запретил слать сиськи' +
                                              ' @titsfoxy в этом чате')
                    time.sleep(3)
                    bot.delete_message(x.chat.id, x.id)
                    return
                send_rnd_pin(message)

            elif '/gamedick' in message.text.lower():
                Tf_cl.longsword_game(message)
            elif message.text == '/sunczi' or message.text == '/sunczi@tfoxy_bot' or \
                    message.text.lower() == '/сунцзы':
                if bot.get_chat(message.chat.id).type == 'private':
                    return
                sett = ChatSettings(logging, connectsql)
                if not sett.get_sett_dict(message.chat.id)['sunczi']:
                    x = bot.reply_to(message, 'Извините но администратор запретил эту команду в этом чате')
                    time.sleep(3)
                    bot.delete_message(x.chat.id, x.id)
                    return
                xxx = " ".join(sund[randint(0, 204)])
                ress = bot.reply_to(message, xxx)
                time.sleep(30)
                bot.delete_message(message.chat.id, ress.message_id)
    # ## ответ на соо бота
            elif message.from_user.id == 5120846605 or message.from_user.username == 'Titsfoxy' \
                    or message.from_user.username == 'ARoboton' \
                    or message.from_user.username == 'MotokoKusanagiMajor':
                if hasattr(message.reply_to_message, 'text'):
                    if message.reply_to_message.from_user.first_name == 'titsfoxy_botik':
                        ress = bot.send_message(message.chat.id, '@'+str(message.from_user.username) +
                                                ' спасибо ))))')
                        time.sleep(10)
                        bot.delete_message(message.chat.id, ress.message_id)
                    elif message.reply_to_message.from_user.first_name == 'titsfoxy_botik':
                        frases(message)
            elif hasattr(message.reply_to_message, 'text'):
                if message.reply_to_message.from_user.first_name == 'titsfoxy_botik':
                    frases(message)
        except Exception:
            logging.error('у меня ошибка внутренняя' + str(traceback.format_exc()))

    @bot.message_handler(content_types=['voice'])
    def voice_processing(message):
        try:
            filename = start_dir + str(uuid.uuid4())
            # filename ='12345'
            file_name_full = filename+".ogg"
            file_name_full_converted = filename+".wav"
            file_info = bot.get_file(message.voice.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            with open(file_name_full, 'wb') as new_file:
                new_file.write(downloaded_file)
            # stdout = subprocess.DEVNULL
            subprocess.call(['ffmpeg', '-nostdin', '-loglevel', '+quiet', '-i', file_name_full,
                             file_name_full_converted])

            text = recognise(file_name_full_converted)
            bot.reply_to(message, f'Переведено TF-bot:\n{text}')

            os.remove(file_name_full)
            os.remove(file_name_full_converted)
        except Exception:
            logging.error('у меня ошибка Voice process' + str(traceback.format_exc()))
            logging.error(f'Voice process \n{filename} \n{file_name_full} \n{file_name_full_converted}')

    while True:
        try:

            bot.polling(none_stop=True, interval=1, allowed_updates='chat_member')

            # Предполагаю, что бот может мирно завершить работу, поэтому
            # даем выйти из цикла

        except Exception:
            logging.error('у меня ошибка внутренняя' + str(traceback.format_exc()))
            bot.stop_polling()
            time.sleep(10)
