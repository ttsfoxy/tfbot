from random import gauss
from time import time as time_now
from time import sleep
import traceback as trback
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from uuid import uuid4
import os
if os.name != 'nt':
    from settings_linx import start_dir as strtdr
    from settings_linx import id_dick_pick, me
elif os.name == 'nt':
    from settings_win import start_dir as strtdr
    from settings_win import id_dick_pick, me


class Tfx():
    def __init__(self, bot, randint, time, BeautifulSoup, requests, YandexImage, os,
                 uuid, traceback, connectsql, start_dir, logging, types) -> None:
        self.bot = bot
        self.randint = randint
        self.time = time
        self.BeautifulSoup = BeautifulSoup
        self.requests = requests
        self.YandexImage = YandexImage
        self.os = os
        self.uuid = uuid
        self.traceback = traceback
        self.connectsql = connectsql
        self.start_dir = start_dir
        self.logging = logging
        self.types = types
        pass

    def brint(self, message):
        self.bot.reply_to(message, 'TESTEST')

    def readbans(self, ban):
        try:
            with open(self.start_dir + 'ban.txt', 'r') as filehandle:
                for line in filehandle:
                    # удалим заключительный символ перехода строки
                    currentPlace = line[:-1]
                    # добавим элемент в конец списка
                    ban.append(int(currentPlace))
        except Exception:
            self.logging.error('ERROR tfx.readbans ' + str(self.traceback.format_exc()))

    def read_frases(self, start_dir):
        frase = []
        with open(start_dir + 'frase.txt', encoding='utf_8') as f:
            for line in f:
                tmp = line.strip().split()
                frase.append(tmp)
        return (frase)

    def read_sunczi(self, start_dir):   # открываем файл, раскидываем значение
        sund = []
        sun_txt = start_dir + 'sun.txt'
        with open(sun_txt, encoding='utf_8') as f:
            for line in f:
                tmp = line.strip().split()
                sund.append(tmp)
        return (sund)

    def banans(self, ban, message):
        try:
            if (message.from_user.id in ban):
                if message.text == '/unban_me@tfoxy_bot':
                    self.bot.send_message(message.chat.id, ' @'+str(message.from_user.username) +
                                          ' You was unbanned')
                    ban.remove(message.from_user.id)
                    with open(self.start_dir + 'ban.txt', 'w') as filehandle:
                        for listitem in ban:
                            filehandle.write('%s\n' % listitem)
                    return
                else:
                    return True

            if message.text == '/ban_me@tfoxy_bot':
                ban.append(message.from_user.id)
                self.bot.send_message(message.chat.id, ' @'+str(message.from_user.username) +
                                      ' You was banned')
                # print(ban)
                with open(self.start_dir + 'ban.txt', 'w') as filehandle:
                    for listitem in ban:
                        filehandle.write('%s\n' % listitem)
            if message.text == '/unban_me@tfoxy_bot':
                self.bot.send_message(message.chat.id, '@'+str(message.from_user.username) +
                                      ' Ты не в списке банов')
        except Exception:
            self.logging.error('ERROR tfx.banans ' + str(self.traceback.format_exc()))

    def hellos(self, message, glob_wrk):
        try:
            hell = ['привет', 'мыхуютро!', 'хай', 'мыхуютро', 'всем привет', 'привет всем',
                    "дарова", "всем драсьте", "драсьте", "дарова", "всем ку", "куку",
                    "дратути", "hello", "hi all", "приветик", "здравствуйте",
                    "добрый вечер", "доброе утро", "доброго дня", "доброй ночи",
                    "приветики", "здарова", "всем здарова", "приветствую", "добрый",
                    "хелло"]
            helloz = ['привет', "дарова", "приветик", "добрый вечер",
                      "приветствую", "хелло"]
            # # wrk = ['работа зло ', "работать много - зло ",
            #        "всего не заработаешь, только здоровье потратишь! ",
            #        'Роботы за безработный мир!',
            #        "убить всех человеков, убить всех человеков..."]
            # wrk_lst = ['/wrk', 'работу', 'работе', 'работы', 'работа']
            lapa = ['я как Алиса, только круче, у меня есть сиськи! а ты милашка ', 'Ути пути, лапочка']
            if '/titty' in message.text.lower() or 'титти' in message.text.lower():
                ress = self.bot.send_message(message.chat.id, lapa[self.randint(0, 1)] +
                                             ' @'+str(message.from_user.username))

            # autoclear(ress.message_id,message.chat.id,ress.date)

            if hasattr(message.reply_to_message, 'text'):
                if message.text.lower() in hell:
                    ress = self.bot.send_message(message.chat.id, (helloz[self.randint(0, 4)]) +
                                                 ' @'+str(message.from_user.username))
                    self.time.sleep(10)
                    self.bot.delete_message(message.chat.id, ress.message_id)

            elif not hasattr(message.reply_to_message, 'text'):
                if message.text.lower() in hell:
                    ress = self.bot.send_message(message.chat.id, (helloz[self.randint(0, 4)]) +
                                                 ' @'+str(message.from_user.username))
                    self.time.sleep(10)
                    self.bot.delete_message(message.chat.id, ress.message_id)
            # global glob_wrk
        except Exception:
            self.logging.error('ERROR tfx.hellos ' + str(self.traceback.format_exc()))
        # ################################################

    def ok_google(self, message, srching_txt=0):
        try:

            if (((message.reply_to_message) and srching_txt == 0) or
               ('/get_photo@tfoxy_bot' == message.text.lower())):
                urlez = []
                parser = self.YandexImage()
                if message.reply_to_message:
                    srch_txt = message.reply_to_message.text
                if '/get_photo@tfoxy_bot' == message.text.lower():
                    srch_txt = 'сиськи блондинка'
                # print(srch_txt)

                tmp_output = parser.search(srch_txt, parser.size.large)
                if tmp_output != []:
                    for item in tmp_output:
                        urlez.append(item.url)
                else:
                    tmp_output = parser.search(srch_txt, parser.size.large)
                    if tmp_output != []:
                        for item in tmp_output:
                            urlez.append(item.url)
                    else:
                        self.bot.reply_to(message, 'Извините но ничего не найдено, либо слишком много' +
                                          ' запросов')
                        return
                tstamp = self.randint(0, (len(urlez)-1))
                # print(urlez[tstamp])
                try:
                    p = self.requests.get(urlez[tstamp])
                except Exception:
                    self.bot.reply_to(message, 'Извините но сайт выдал ошибку при попытке скачать картинку')
                    return
                filename = str(self.uuid.uuid4())
                filename = self.start_dir + filename + '.jpg'
                try:
                    out = open(filename, "wb")
                    out.write(p.content)
                    out.close()
                except Exception:
                    self.os.remove(filename)
                    return (False)
                urlez.clear()
                try:
                    img = open(filename, 'rb')
                    retry = self.bot.send_photo(message.chat.id, img, caption='Ня @' +
                                                str(message.from_user.username))
                    img.close()
                    self.os.remove(filename)
                    return (retry)
                except Exception:
                    self.bot.reply_to(message, 'Ошибка в обработке и посылке файла')
                    self.os.remove(filename)
                    return (False)
            else:
                urlez = []
                parser = self.YandexImage()
                if srching_txt == 0:
                    srch_txt = 'эротика аниме рисованная сиськи'
                else:
                    srch_txt = srching_txt
                # print(srch_txt)
                tmp_output = parser.search(srch_txt, parser.size.large)
                if tmp_output != []:
                    for item in tmp_output:
                        urlez.append(item.url)
                else:
                    tmp_output = parser.search(srch_txt, parser.size.large)
                    if tmp_output != []:
                        for item in tmp_output:
                            urlez.append(item.url)
                    else:
                        self.bot.reply_to(message, 'Извините но ничего не найдено, либо слишком много' +
                                          ' запросов ')
                        return
                tstamp = self.randint(0, (len(urlez)-1))
                try:
                    p = self.requests.get(urlez[tstamp])
                except Exception:
                    self.bot.reply_to(message, 'Извините но сайт выдал ошибку при попытке скачать картинку')
                    return
                filename = str(self.uuid.uuid4())
                filename = self.start_dir + filename + '.jpg'
                try:
                    out = open(filename, "wb")
                    out.write(p.content)
                    out.close()
                except Exception:
                    self.os.remove(filename)
                    return (False)
                urlez.clear()
                try:
                    img = open(filename, 'rb')
                    retry = self.bot.send_photo(message.chat.id, img, caption='Ня @' +
                                                str(message.from_user.username))
                    img.close()
                    self.os.remove(filename)
                    return (retry)
                except Exception:
                    self.os.remove(filename)
                    return (False)
        except Exception:
            self.bot.reply_to(message, 'Извините но ничего не найдено, либо это баг 2' + tmp_output)
            self.logging.error('ERROR tfx.ok goo ' + str(self.traceback.format_exc()))

    def para(self, message):
        None

    def chats(self):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * from chats")
            date = info.fetchall()
            if date is not None:
                ret_list = []
                for x in date:
                    ret_list.append([x[0], x[1]])

                conn.close()
                return (ret_list)
            else:
                conn.close()
                return ([])
        except Exception:
            # conn.close() # херня какая то не хапускается тут на роутере
            self.logging.error('ERROR tfx.chats ' + str(self.traceback.format_exc()))

    def chat_check(self, chat_lst, message):
        try:
            if chat_lst == []:
                tip = self.bot.get_chat(message.chat.id).type
                # print(tip)
                if tip == 'group' or tip == 'supergroup':
                    self.chat_add(message.chat.id, message.chat.title)
                    chat_lst.append([message.chat.id, message.chat.title])
                    sett = ChatSettings(self.logging, self.connectsql)
                    sett.set_settings_chat(message.chat.id, name=message.chat.title)

            else:
                for x in chat_lst:
                    if message.chat.id in x:
                        has_chat = True
                        return (True)
                    else:
                        has_chat = False

                if has_chat is False:
                    tip = self.bot.get_chat(message.chat.id).type

                    if tip == 'group' or tip == 'supergroup':
                        self.chat_add(message.chat.id, message.chat.title)
                        chat_lst.append([message.chat.id, message.chat.title])
                        sett = ChatSettings(self.logging, self.connectsql)
                        sett.set_settings_chat(message.chat.id, name=message.chat.title)
                        # print('here2')

        except Exception:
            # print('Error in chat check ' + str(self.traceback.format_exc()))
            self.logging.error('ERROR tfx.chat check ' + str(self.traceback.format_exc()))

    def chat_add(self, chat_id, name):
        try:
            conn = self.connectsql()
            conn.execute("INSERT or REPLACE INTO chats(id, name) values(?,?)", (chat_id, name))
            conn.commit()
        except Exception:
            conn.close()
            # print('Error in chat chat_add ' + str(self.traceback.format_exc()))
            self.logging.error('ERROR tfx.chat add ' + str(self.traceback.format_exc()))

    def changes_write(self, text):
        try:
            conn = self.connectsql()
            times = self.time.time()
            # print(times)
            conn.execute("INSERT INTO changes (date, text) values(?, ?)", (times, text))
            conn.commit()
            conn.close()
            return (times, text)

        except Exception:
            conn.close()
            # print('Error in chat chang write ' + str(self.traceback.format_exc()))
            self.logging.error('ERROR tfx.chang write ' + str(self.traceback.format_exc()))
            return (False)

    def changes_read_last(self):  # читаем последние обновы из бд
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM changes WHERE date=(SELECT MAX(date) from changes)")
            date = info.fetchone()
            ret_lst = []
            if date is None:
                return (False, 0)
            else:
                ret_lst.append([date[0], date[1]])
                return (True, ret_lst)

        except Exception:
            # print('Error in chat chang read ' + str(self.traceback.format_exc()))
            self.logging.error('ERROR tfx.chang read lst ' + str(self.traceback.format_exc()))
            return (False)
            # SELECT * FROM db WHERE ochki=(select max(ochki) from db)

    def test_changes_del(self, time):
        try:
            conn = self.connectsql()
            conn.execute("DELETE  FROM changes WHERE date=?", (time,))
            conn.commit()
            conn.close()
            return (True)
        except Exception:
            # print('Error in chat test del read ' + str(self.traceback.format_exc()))
            self.logging.error('ERROR tfx.chang del ' + str(self.traceback.format_exc()))
            return (False)

    def longsword_push(self, id, id_chat, name, long, time):
        try:
            conn = self.connectsql()
            conn.execute("REPLACE INTO longsword (id, chat, name, long, date) values(?,?,?,?,?)",
                         (id, id_chat, name, long, time))
            conn.commit()
            conn.close()
            return (True)
        except Exception:
            conn.close()
            # print('Error in longsword_push ' + str(self.traceback.format_exc()))
            self.logging.error('ERROR tfx.LS push ' + str(self.traceback.format_exc()))
            return (False)

    def longsword_check(self, id, id_chat, time):
        try:
            conn = self.connectsql()
            date = conn.execute("SELECT * FROM longsword WHERE id=? and chat=?",
                                (id, id_chat))
            info = date.fetchone()
            if info is None:  # нет в базе
                conn.close()
                return (False)
            else:
                conn.close()
                return (info[3], info[4])  # размер дата
        except Exception:
            conn.close()
            # print('Error in longsword_check ' + str(self.traceback.format_exc()))
            self.logging.error('ERROR tfx.ls check ' + str(self.traceback.format_exc()))
            return (False)

    def longsword_del(self, id, chat):
        try:
            conn = self.connectsql()
            conn.execute("DELETE  FROM longsword WHERE id=? and chat=?",
                         (id, chat))
            conn.commit()
            conn.close()
            return (True)
        except Exception:
            # print('Error in chat test del read ' + str(self.traceback.format_exc()))
            self.logging.error('ERROR tfx.ls del ' + str(self.traceback.format_exc()))
            return (False)

    def longsword_strt(self, id, id_chat, name, time):
        try:
            res = self.longsword_check(id, id_chat, time)
            if res is False:                    # если нет в базе

                gness = self.gaussed(23, 5, 49)

                self.longsword_push(id, id_chat, name, gness, time)
                return (gness, True)            # возвращаем размер сгенерированный
            elif res[1] < (time - 86400):       # енсли есть но страше суток
                # gness = self.randint(0, 49)
                gness = self.gaussed(23, 5, 49)
                self.longsword_del(id, id_chat)
                self.longsword_push(id, id_chat, name, gness, time)
                return (gness, True)            # возвращаем размер сгенерированный
            else:
                gness = res[0]
                return (gness, False)           # ЕСЛИ ЕСТЬ И НЕ СТАРШЕ СУТОК ТО возвр из базы
        except Exception:
            self.logging.error('ERROR tfx.ls strt ' + str(self.traceback.format_exc()))

    def gaussed(self, mu, sigma, max):  # sssssssssssssssssssss
        resu = -1
        while resu < 0 or resu > 49:
            resu = int(gauss(23, 5))
        return (resu)

    def longsword_game(self, message):
        try:
            if self.bot.get_chat(message.chat.id).type == 'private':
                self.bot.reply_to(message, 'Извините, в личке игра не работает )))')
                return
            lst_dicks = self.longsword_game_get(message.chat.id, self.time.time())
            if lst_dicks is False:
                self.bot.reply_to(message, 'Что то пошло не так')
                return (False)
            snd_str = '```\nРекордсмены сегодня:\n'
            for x in lst_dicks:
                snd_str = snd_str + x[0] + '    ' + str(x[1]) + '\n'
            snd_str = snd_str + '\nСамый красивый у @' + lst_dicks[0][0] + ' 🤩```'

            self.bot.reply_to(message, snd_str, parse_mode='MarkdownV2')
        except Exception:
            self.bot.reply_to(message, 'Что то пошло не так')
            self.logging.error('ERROR tfx.ls game ' + str(self.traceback.format_exc()))

    def longsword_game_get(self, id_chat, time):
        try:
            time = time - 86400
            conn = self.connectsql()
            info = conn.execute("SELECT name, long FROM longsword WHERE chat=? AND date > ?",
                                (id_chat, time))
            date = info.fetchall()
            conn.close()
            srt_date = sorted(date, key=lambda date: date[1], reverse=True)
            srt_ret = []
            i = 0
            for x in srt_date:
                if i > 10:
                    break
                srt_ret.append(x)
                i = i + 1
            return (srt_ret)
        except Exception:
            # conn.close()
            # print('ERROR tfx.ls game get ' + str(self.traceback.format_exc()))
            return (False)

    def clear_base(self):
        try:
            print('start clear')
            conn = self.connectsql()
            info = conn.execute("SELECT * from last_seen")
            date = info.fetchall()
            for x in date:
                tmp_info = conn.execute("SELECT * from last_seen WHERE id_user=? and id_chat=? \
                    ORDER BY date DESC",
                                        (x[0], x[1]))
                date_tmp = tmp_info.fetchone()
                conn.execute("DELETE FROM last_seen where id_user=? and id_chat=? and date <?",
                             (date_tmp[0], date_tmp[1], date_tmp[3]))
            conn.commit()
            conn.close()
            print("ended clear")
        except Exception:
            print('ERROR clearbase ' + str(self.traceback.format_exc()))
            self.logging.error('ERROR clearbase ' + str(self.traceback.format_exc()))

    def clear_msg(self, to_del):
        for x in to_del:
            try:
                self.bot.delete_message(x[0], x[1])
            except Exception:
                self.bot.send_message(1675780013, f'Error del mess {x[0]} {x[1]}')

    def acсio(self, message):
        try:
            if "акцио" in message.text.lower():             #
                if self.bot.get_chat(message.chat.id).type != 'private':
                    sett = ChatSettings(self.logging, self.connectsql)
                    if not sett.get_sett_dict(message.chat.id)['ok']:
                        x = self.bot.reply_to(message, 'Извините но администратор запретил акцио поиск в ' +
                                                       'этом чате')
                        sleep(3)
                        self.bot.delete_message(x.chat.id, x.id)
                        return
                # print(message.text.lower())
                txt = message.text.lower()                  #
                txt = txt.split()                           # превращаем в лист
                txt = txt[txt.count("акцио"):]              # отделяем все до акцио не включая
                txt = ' '.join(txt)
                # print(txt)
                x = self.ok_google(message, srching_txt=txt)
                menu = Menu(self.bot, self.logging)
                menu.menu_okg(x)
        except Exception:
            self.bot.send_message(1675780013, f'Error accio {txt}')

    def is_admin(self, message):
        if self.bot.get_chat_member(message.chat.id, message.from_user.id).status == \
                            'creator' or \
                            self.bot.get_chat_member(message.chat.id,
                                                     message.from_user.id).status \
                            == 'administrator':
            return (True)
        else:
            return (False)

    def get_file(self, message):
        try:
            if message.text == 'пуш' and hasattr(message, 'reply_to_message') and self.is_admin(message):
                filename = str(self.uuid.uuid4())
                filename = self.start_dir + 'phots/' + filename + '.jpg'
                id_photo = message.reply_to_message.photo[-1].file_id
                file_info = self.bot.get_file(id_photo)
                downloaded_file = self.bot.download_file(file_info.file_path)
                with open(filename, 'wb') as new_file:
                    new_file.write(downloaded_file)
                self.push_file_to_base(message.chat.id, filename)
                # img = open(filename, 'rb')
                # self.bot.send_photo(message.chat.id, img)
        except Exception:
            self.logging.error('ERROR get_file ' + str(trback.format_exc()))

    def get_file_pinned(self, message):
        try:
            if hasattr(message.pinned_message, 'photo'):  # если автопин или пин по комде пин
                filename = str(self.uuid.uuid4())
                filename = self.start_dir + 'phots/' + filename + '.jpg'
                id_photo = message.pinned_message.photo[-1].file_id
                file_info = self.bot.get_file(id_photo)
                downloaded_file = self.bot.download_file(file_info.file_path)
                with open(filename, 'wb') as new_file:
                    new_file.write(downloaded_file)
                self.push_file_to_base(message.chat.id, filename)
            elif hasattr(message, 'photo'):                 # пин по кнопке калбака
                filename = str(self.uuid.uuid4())
                filename = self.start_dir + 'phots/' + filename + '.jpg'
                id_photo = message.photo[-1].file_id
                file_info = self.bot.get_file(id_photo)
                downloaded_file = self.bot.download_file(file_info.file_path)
                with open(filename, 'wb') as new_file:
                    new_file.write(downloaded_file)
                self.push_file_to_base(message.chat.id, filename)
        except Exception:
            self.logging.error('ERROR get_file_pinned ' + str(trback.format_exc()))

    def push_file_to_base(self, id_chat, name):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM phots WHERE id_chat = ? and namefile = ?",
                                (id_chat, name))
            date = info.fetchone()
            # print(date)
            if date is None:
                conn.execute("INSERT INTO phots(id_chat,namefile) values(?,?)",
                             (id_chat, name))
                conn.commit()
                conn.close()
        except Exception:
            self.bot.send_message(1675780013, 'Error push_file_to_base')
        finally:
            conn.close()
# id_chat namefile

    def send_rnd_from(self, message):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM phots WHERE id_chat=? ORDER BY RANDOM() LIMIT 1",
                                (message.chat.id,))
            date = info.fetchone()
            conn.close()
            if date is None:
                self.bot.reply_to(message, 'Извините, пин чата пуст')
                return (False)
            else:
                img = open(date[1], 'rb')
                return (img)
                # self.bot.send_photo(message.chat.id, img, caption=f'Ня @{message.from_user.username}')
        except Exception:
            self.bot.reply_to(message, 'Извините, произошла ошибка')
            self.logging.error('ERROR send_rnd_from ' + str(self.traceback.format_exc()))
        finally:
            conn.close()


class Dp_chan():
    def __init__(self, bot, logging) -> None:
        self.bot = bot
        self.logging = logging
        pass

    def mute_usr(self, message):
        if hasattr(message, 'reply_to_message'):

            if (self.bot.get_chat_member(message.chat.id, message.from_user.id).can_restrict_members or
               self.bot.get_chat_member(message.chat.id, message.from_user.id).status == 'creator'):
                lst_command = message.text.lower().split(' ')
                if len(lst_command) == 1:
                    x = self.bot.reply_to(message, 'Запрос неправильно сформирован, пишите !РО число ' +
                                          'часы/минуты/дни')
                    sleep(3)
                    self.bot.delete_message(x.chat.id, x.message_id)
                try:
                    ro_index = lst_command.index('!ро')
                except Exception:
                    try:
                        ro_index = lst_command.index('!ro')
                    except Exception:
                        x = self.bot.reply_to(message, 'Запрос неправильно сформирован, пишите !РО ' +
                                                       'число ч/м/д')
                        sleep(3)
                        self.bot.delete_message(x.chat.id, x.message_id)
                time_x = lst_command[ro_index+1]
                if not time_x.isdigit():
                    x = self.bot.reply_to(message, 'Запрос неправильно сформирован, пишите !РО число ч/м/д')
                    sleep(3)
                    self.bot.delete_message(x.chat.id, x.message_id)

                day_minit = lst_command[ro_index+2]

                if 'ч' in day_minit:
                    insert_time = 3600*int(time_x)
                elif 'м' in day_minit:
                    insert_time = 60*int(time_x)+120
                elif 'д' in day_minit:
                    insert_time = 86400*int(time_x)
                else:
                    x = self.bot.reply_to(message, 'Запрос неправильно сформирован, пишите !РО число ч/м/д')
                    sleep(3)
                    self.bot.delete_message(x.chat.id, x.message_id)
                try:
                    # print(time_now())
                    self.bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                                  until_date=time_now()+insert_time)
                except Exception:
                    x = self.bot.reply_to(message, 'Не получилось, либо бот не имеет прав, либо вы ' +
                                                   'пытаетесь замутить админа')
                    sleep(3)
                    self.bot.delete_message(x.chat.id, x.message_id)
                delmess1 = self.bot.reply_to(message, 'request complete')
                sleep(10)
                self.bot.delete_message(delmess1.chat.id, delmess1.message_id)
            else:
                x = self.bot.reply_to(message, 'У вас нет прав на мут пользователей, обратитесь к админу')
                sleep(5)
                self.bot.delete_message(x.chat.id, x.message_id)
        else:
            x = self.bot.reply_to(message, 'Команда должна быть ответом на сообщение')
            sleep(5)
            self.bot.delete_message(x.chat.id, x.message_id)


class Gay_band():
    def __init__(self, bot, logging, connectsql) -> None:
        self.bot = bot
        self.logging = logging
        self.connectsql = connectsql
        pass

    def get_rnd_gay(self, chat_id, time_now):
        try:
            date_minus = time_now - 604800
            # date_minus = 1668007576.42758
            conn = self.connectsql()
            info = conn.execute("SELECT * From last_seen where id_chat=? AND date > ? \
                                 ORDER BY RANDOM() LIMIT 1", (chat_id, date_minus))
            date = info.fetchone()

            if date is None:
                conn.close()
                return (False)
            # return (True)  # 12121312312
            conn.close()
            return (date)
        except Exception:
            conn.close()
            # print('Error in longsword_check ' + str(self.traceback.format_exc()))
            self.logging.error('ERROR Gayband get rnd gay' + str(self.traceback.format_exc()))
            return (False)

    def gay_check(self, chat_id):
        try:
            conn = self.connectsql()
            date = conn.execute("SELECT * FROM gayday WHERE chat_id=?",
                                (chat_id,))
            info = date.fetchone()
            if info is None:  # нет в базе
                conn.close()
                return (False)
            else:
                conn.close()
                return (info)  # возврат всего гея если есть
        except Exception:
            conn.close()
            # print('Error in longsword_check ' + str(self.traceback.format_exc()))
            self.logging.error('ERROR Gayband check ' + str(trback.format_exc()))
            return (False)

    def gay_select(self, chat_id):
        # print(chat_id)
        gay = self.gay_check(chat_id)
        if gay:  # gay [user_id, chat_id, name, date]
            if gay[3] < (time_now() - 86400):  # если гей старше суток
                gay = self.get_rnd_gay(chat_id, time_now())

                self.bot.send_message(chat_id, 'Если вас оскорбил гей, не стоит становиться в позу' +
                                               ' - может получиться ещё хуже...')
                self.bot.send_message(chat_id, f'На сегодня Пидор дня @{gay[2]}')
                self.gay_push(gay)
            else:

                self.bot.send_message(chat_id, f'Сегодня пидор это @{gay[2]}')
        else:
            gay = self.get_rnd_gay(chat_id, time_now())
            self.gay_push(gay)
            self.bot.send_message(chat_id, 'Натурал - это пидр нетрадиционной ориентации.')
            self.bot.send_message(chat_id, 'как происходит у геев осознание того, что они геи?\n-' +
                                           'Во время просмотра порнухи вдруг понимают, что болеют ' +
                                           'не за ту команду?!')
            self.bot.send_message(chat_id, f'ииии сегодня пидор это @{gay[2]}')

    def gay_push(self, gay):

        try:
            if self.gay_check(gay[1]):
                conn = self.connectsql()
                conn.execute("DELETE FROM gayday WHERE chat_id=?", (gay[1],))
                conn.commit()
                conn.close()
            conn = self.connectsql()
            conn.execute("REPLACE into gayday (user_id, chat_id, name, date) values(?,?,?,?)",
                         (gay[0], gay[1], gay[2], gay[3]))
            conn.commit()
            conn.close()
        except Exception:
            self.logging.error('ERROR Gayband check ' + str(trback.format_exc()))
            return (False)
        finally:
            conn.close()

    def gay_push_stat(self, gay):  # пушим статку в бд, чтоб знать сколько кого выбрали
        # "gay_stat" ("id" INTEGER, "id_chat" INTEGER, "name" TEXT,"points" INTEGER)
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM gay_stat where id = ? AND id_chat = ?",
                                (gay[0], gay[1]))
            date = info.fetchone()
            if date is not None:
                conn.execute("UPDATE gay_stat SET points = points + 1 where id = ? AND id_chat = ?",
                             (gay[0], gay[1]))
                conn.commit()
                conn.close()
                return (True)
            else:
                conn.execute("INSERT INTO gay_stat (id, id_chat, name, points) values(?,?,?,?)",
                             (gay[0], gay[1], gay[2], 1))
                conn.commit()
                conn.close()
                return (True)
        except Exception:
            self.logging.error('ERROR gay_push_stat ' + str(trback.format_exc()))
            return (False)
            # conn.execute("DELETE FROM gay_stat where id = ? AND id_chat = ?",
            #              (gay[0], gay[1]))

    def gay_get_stat_one(self, id, id_chat):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM gay_stat where id = ? AND id_chat = ?",
                                (id, id_chat))
            date = info.fetchone()
            if date is not None:
                conn.close()
                return (date)   # если есть то возвращаем лист
            else:
                conn.close()
                return (True)   # если нет в бд то возвращаем true
        except Exception:
            self.logging.error('ERROR gay_get_stat_one ' + str(trback.format_exc()))
            return (False)      # если ошибка то False

    def gay_stat_del(self, id, id_chat):
        try:
            conn = self.connectsql()
            conn.execute("DELETE FROM gay_stat where id = ? AND id_chat = ?",
                         (id, id_chat))
            conn.commit()
            conn.close()
            return (True)
        except Exception:
            self.logging.error('ERROR gay_stat_del ' + str(trback.format_exc()))
            return (False)      # если ошибка то False


class ChatSettings():
    def __init__(self, logging, connectsql) -> None:
        self.logging = logging
        self.connectsql = connectsql
        pass
    # settings "id"	INTEGER,"name" TEXT,"owner"	TEXT,"menu"	NUMERIC,"pinned_mess" NUMERIC

    def new_chat(self, id):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM settings WHERE id=?", (id,))
            date = info.fetchone()
            if date:
                conn.close()
                return (False)
            conn.execute("""INSERT INTO settings (id, name, owner, menu, pinned_mess, ok, auto_answer,
                         sunczi, karma, stat, recognize, hello_mess, guyness, para, dick, foxy, gayday, wiki)
                         values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                         (id, 'nme', 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
            conn.commit()
            conn.close()
            return (True)
        except Exception:
            self.logging.error('ERROR new_chat ' + str(trback.format_exc()))
        finally:
            conn.close()

    def change_name_chat(self, id, name):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM settings WHERE id=?", (id,))
            date = info.fetchone()
            if date:
                conn.execute("UPDATE settings SET name=? where id=?", (name, id))
                conn.commit()
                conn.close()
                return (True)
            conn.close()
            return (False)
        except Exception:
            self.logging.error('ERROR change_name_chat ' + str(trback.format_exc()))
        finally:
            conn.close()

    def delete_settings(self, id):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM settings WHERE id=?", (id,))
            date = info.fetchone()
            if date:
                conn.execute("DELETE FROM settings WHERE id=?", (id,))
                conn.commit()
                conn.close()
                return (True)
            else:
                conn.close()
                return (False)
        except Exception:
            self.logging.error('ERROR delete_settings ' + str(trback.format_exc()))
        finally:
            conn.close()

    def get_settings(self, id):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM settings WHERE id=?", (id,))
            date = info.fetchone()
            if date:
                conn.close()
                return (date)
            else:
                conn.close()
                return (False)
        except Exception:
            self.logging.error('ERROR get_settings ' + str(trback.format_exc()))
        finally:
            conn.close()

    def get_sett_dict(self, id):
        try:
            lst = self.get_settings(id)
            ret_dict = {'id': lst[0], 'name': lst[1], 'owner': lst[2], 'menu': int(lst[3]),
                        'pinned_mess': int(lst[4]), 'ok': int(lst[5]), 'auto_answer': int(lst[6]),
                        'sunczi': int(lst[7]), 'karma': int(lst[8]), 'stat': int(lst[9]),
                        'recognize': int(lst[10]), 'hello_mess': int(lst[11]), 'guiness': int(lst[12]),
                        'para': int(lst[13]), 'dick': int(lst[14]), 'foxy': int(lst[15]),
                        'gayday': int(lst[16]), 'wiki': int(lst[17])}
            return (ret_dict)
        except Exception:
            self.logging.error('ERROR get_sett dict ' + str(trback.format_exc()))

    def change_owner_chat(self, id, owner):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM settings WHERE id=?", (id,))
            date = info.fetchone()
            if date:
                conn.execute("UPDATE settings SET owner=? where id=?", (owner, id))
                conn.commit()
                conn.close()
                return (True)
            conn.close()
            return (False)
        except Exception:
            self.logging.error('ERROR change_owner_chat ' + str(trback.format_exc()))
        finally:
            conn.close()

    def change_menu_chat(self, id, menu):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM settings WHERE id=?", (id,))
            date = info.fetchone()
            if date:
                conn.execute("UPDATE settings SET menu=? where id=?", (menu, id))
                conn.commit()
                conn.close()
                return (True)
            conn.close()
            return (False)
        except Exception:
            self.logging.error('ERROR change_menu_chat ' + str(trback.format_exc()))
        finally:
            conn.close()

    def change_pinned_mess_chat(self, id, pinned):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM settings WHERE id=?", (id,))
            date = info.fetchone()
            if date:
                conn.execute("UPDATE settings SET pinned_mess=? where id=?", (pinned, id))
                conn.commit()
                conn.close()
                return (True)
            conn.close()
            return (False)
        except Exception:
            self.logging.error('ERROR change_pinned_mess_chat ' + str(trback.format_exc()))
        finally:
            conn.close()

    def change_ok(self, id, ok):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM settings WHERE id=?", (id,))
            date = info.fetchone()
            if date:
                conn.execute("UPDATE settings SET ok=? where id=?", (ok, id))
                conn.commit()
                conn.close()
                return (True)
            conn.close()
            return (False)
        except Exception:
            self.logging.error('ERROR change_ok ' + str(trback.format_exc()))
        finally:
            conn.close()

    def change_auto_answer(self, id, aa):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM settings WHERE id=?", (id,))
            date = info.fetchone()
            if date:
                conn.execute("UPDATE settings SET auto_answer=? where id=?", (aa, id))
                conn.commit()
                conn.close()
                return (True)
            conn.close()
            return (False)
        except Exception:
            self.logging.error('ERROR auto_answer ' + str(trback.format_exc()))
        finally:
            conn.close()

    def change_sunczi(self, id, sz):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM settings WHERE id=?", (id,))
            date = info.fetchone()
            if date:
                conn.execute("UPDATE settings SET sunczi=? where id=?", (sz, id))
                conn.commit()
                conn.close()
                return (True)
            conn.close()
            return (False)
        except Exception:
            self.logging.error('ERROR change sunczi ' + str(trback.format_exc()))
        finally:
            conn.close()

    def change_karma(self, id, karma):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM settings WHERE id=?", (id,))
            date = info.fetchone()
            if date:
                conn.execute("UPDATE settings SET karma=? where id=?", (karma, id))
                conn.commit()
                conn.close()
                return (True)
            conn.close()
            return (False)
        except Exception:
            self.logging.error('ERROR change_karma ' + str(trback.format_exc()))
        finally:
            conn.close()

    def change_stat(self, id, stat):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM settings WHERE id=?", (id,))
            date = info.fetchone()
            if date:
                conn.execute("UPDATE settings SET stat=? where id=?", (stat, id))
                conn.commit()
                conn.close()
                return (True)
            conn.close()
            return (False)
        except Exception:
            self.logging.error('ERROR change_stat ' + str(trback.format_exc()))
        finally:
            conn.close()

    def change_recognize(self, id, recognize):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM settings WHERE id=?", (id,))
            date = info.fetchone()
            if date:
                conn.execute("UPDATE settings SET recognize=? where id=?", (recognize, id))
                conn.commit()
                conn.close()
                return (True)
            conn.close()
            return (False)
        except Exception:
            self.logging.error('ERROR change_recognize ' + str(trback.format_exc()))
        finally:
            conn.close()

    def change_hello_mess(self, id, hello_mess):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM settings WHERE id=?", (id,))
            date = info.fetchone()
            if date:
                conn.execute("UPDATE settings SET hello_mess=? where id=?", (hello_mess, id))
                conn.commit()
                conn.close()
                return (True)
            conn.close()
            return (False)
        except Exception:
            self.logging.error('ERROR change_hello_mess ' + str(trback.format_exc()))
        finally:
            conn.close()

    def change_guiness(self, id, guiness):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM settings WHERE id=?", (id,))
            date = info.fetchone()
            if date:
                conn.execute("UPDATE settings SET guyness=? where id=?", (guiness, id))
                conn.commit()
                conn.close()
                return (True)
            conn.close()
            return (False)
        except Exception:
            self.logging.error('ERROR change_guiness ' + str(trback.format_exc()))
        finally:
            conn.close()

    def change_para(self, id, para):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM settings WHERE id=?", (id,))
            date = info.fetchone()
            if date:
                conn.execute("UPDATE settings SET para=? where id=?", (para, id))
                conn.commit()
                conn.close()
                return (True)
            conn.close()
            return (False)
        except Exception:
            self.logging.error('ERROR change_para ' + str(trback.format_exc()))
        finally:
            conn.close()

    def change_dick(self, id, dick):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM settings WHERE id=?", (id,))
            date = info.fetchone()
            if date:
                conn.execute("UPDATE settings SET dick=? where id=?", (dick, id))
                conn.commit()
                conn.close()
                return (True)
            conn.close()
            return (False)
        except Exception:
            self.logging.error('ERROR change_dick ' + str(trback.format_exc()))
        finally:
            conn.close()

    def change_foxy(self, id, foxy):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM settings WHERE id=?", (id,))
            date = info.fetchone()
            if date:
                conn.execute("UPDATE settings SET foxy=? where id=?", (foxy, id))
                conn.commit()
                conn.close()
                return (True)
            conn.close()
            return (False)
        except Exception:
            self.logging.error('ERROR change_foxy ' + str(trback.format_exc()))
        finally:
            conn.close()

    def change_gayday(self, id, gayday):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM settings WHERE id=?", (id,))
            date = info.fetchone()
            if date:
                conn.execute("UPDATE settings SET gayday=? where id=?", (gayday, id))
                conn.commit()
                conn.close()
                return (True)
            conn.close()
            return (False)
        except Exception:
            self.logging.error('ERROR change_gayday ' + str(trback.format_exc()))
        finally:
            conn.close()

    def change_wiki(self, id, wiki):
        try:
            conn = self.connectsql()
            info = conn.execute("SELECT * FROM settings WHERE id=?", (id,))
            date = info.fetchone()
            if date:
                conn.execute("UPDATE settings SET wiki=? where id=?", (wiki, id))
                conn.commit()
                conn.close()
                return (True)
            conn.close()
            return (False)
        except Exception:
            self.logging.error('ERROR change_wiki ' + str(trback.format_exc()))
        finally:
            conn.close()
# (id, name=None, owner=None,meny=None,pinned_mess=None)
# если id то создаем новую запись

    def set_settings_chat(self, id, name=None, owner=None, menu=None, pinned_mess=None, ok=None,
                          auto_answer=None, sunczi=None, karma=None, stat=None, recognize=None,
                          hello_mess=None, guiness=None, para=None, dick=None, foxy=None, gayday=None,
                          wiki=None):
        try:
            if (id and name is None and owner is None and menu is None and pinned_mess is None and ok is None
               and auto_answer is None and sunczi is None and karma is None and stat is None
               and recognize is None and hello_mess is None and guiness is None and para is None
               and dick is None and foxy is None and gayday is None and wiki is None):
                if self.new_chat(id):
                    return (True)           # если только id chat
                else:
                    return (False)
            elif id and (name or owner or menu is not None or pinned_mess is not None):
                self.new_chat(id)
            if name:
                if self.change_name_chat(id, name):
                    pass
                else:
                    return (False)
            if owner:
                if self.change_owner_chat(id, owner):
                    pass
                else:
                    return (False)
            if menu is not None:
                if self.change_menu_chat(id, menu):
                    pass
                else:
                    return (False)
            if pinned_mess is not None:
                if self.change_pinned_mess_chat(id, pinned_mess):
                    pass
                else:
                    return (False)
            if ok is not None:
                if self.change_ok(id, ok):
                    pass
                else:
                    return (False)
            if auto_answer is not None:
                if self.change_auto_answer(id, auto_answer):
                    pass
                else:
                    return (False)
            if sunczi is not None:
                if self.change_sunczi(id, sunczi):
                    pass
                else:
                    return (False)
            if karma is not None:
                if self.change_karma(id, karma):
                    pass
                else:
                    return (False)
            if stat is not None:
                if self.change_stat(id, stat):
                    pass
                else:
                    return (False)
            if recognize is not None:
                if self.change_recognize(id, recognize):
                    pass
                else:
                    return (False)
            if hello_mess is not None:
                if self.change_hello_mess(id, hello_mess):
                    pass
                else:
                    return (False)
            if guiness is not None:
                if self.change_guiness(id, guiness):
                    pass
                else:
                    return (False)
            if para is not None:
                if self.change_para(id, para):
                    pass
                else:
                    return (False)
            if dick is not None:
                if self.change_dick(id, dick):
                    pass
                else:
                    return (False)
            if foxy is not None:
                if self.change_foxy(id, foxy):
                    pass
                else:
                    return (False)
            if gayday is not None:
                if self.change_gayday(id, gayday):
                    pass
                else:
                    return (False)
            if wiki is not None:
                if self.change_wiki(id, wiki):
                    pass
                else:
                    return (False)
            return (True)
        except Exception:
            self.logging.error('ERROR set_settings_chat ' + str(trback.format_exc()))
            return (False)


class MenuSettAdm():
    def __init__(self, bot, logging, connectsql) -> None:
        self.bot = bot
        self.logging = logging
        self.connectsql = connectsql
        pass
    # from telebot import types as tpes

    def test(self, message):
        try:
            callback_button_1 = InlineKeyboardButton(text="Узнать свой результат 🏳️‍🌈",
                                                          callback_data=('guyness'))

            keyboard = InlineKeyboardMarkup()
            keyboard.add(callback_button_1)
            # keyboard = tpes.keyboard
            self.bot.send_message(message.chat.id, '3242342',
                                  reply_markup=keyboard)
            # ChatSett = ChatSettings(self.logging, self.connectsql)
            # ChatSett.set_settings_chat(message.chat.id)
        except Exception:
            self.logging.error('ERROR test ' + str(trback.format_exc()))

    def set_fuckin_menu(self, chat_id_to_send, chat_id_rewr):
        try:
            callback_button_1 = InlineKeyboardButton(text="Разрешить меню(бета)",
                                                          callback_data=('set_menu'))
            callback_button_2 = InlineKeyboardButton(text="Разрешить добавление в бота",
                                                          callback_data=('set_add_bot'))
            callback_button_3 = InlineKeyboardButton(text="Запретить поиск через ок и акцио",
                                                          callback_data=('set_ok_bot_off'))

            keyboard = InlineKeyboardMarkup()
            keyboard.add(callback_button_1)
            keyboard.add(callback_button_2)
            keyboard.add(callback_button_3)
            self.bot.send_message(chat_id_to_send, f'меню настроек бота для чата {chat_id_rewr}',
                                  reply_markup=keyboard)

        except Exception:
            self.logging.error('ERROR set_fuckin_menu ' + str(trback.format_exc()))

    def set_menu(self, chat_id_to_send, chat_id_rewr):
        chsett = ChatSettings(self.logging, self.connectsql)
        dict_sett = chsett.get_sett_dict(chat_id_rewr)
        # print(dict_sett)
        if dict_sett['menu']:
            txt = 'Автоматические меню ✅'  # 🛑✅
            btn_1 = InlineKeyboardButton(text=txt, callback_data=('set_menu_off'))
        else:
            txt = 'Автоматические меню 🛑'
            btn_1 = InlineKeyboardButton(text=txt, callback_data=('set_menu_on'))

        if dict_sett['pinned_mess']:
            txt = 'Добавление закрепов ✅'  # 🛑✅
            btn_2 = InlineKeyboardButton(text=txt, callback_data=('pinned_mess_off'))
        else:
            txt = 'Добавление закрепов 🛑'
            btn_2 = InlineKeyboardButton(text=txt, callback_data=('pinned_mess_on'))

        if dict_sett['ok']:
            txt = 'Поиск через ок и акцио ✅'  # 🛑✅
            btn_3 = InlineKeyboardButton(text=txt, callback_data=('set_ok_bot_off'))
        else:
            txt = 'Поиск через ок и акцио 🛑'
            btn_3 = InlineKeyboardButton(text=txt, callback_data=('set_ok_bot_on'))

        if dict_sett['auto_answer']:
            txt = 'Автоболталка бота ✅'  # 🛑✅ #############################
            btn_4 = InlineKeyboardButton(text=txt, callback_data=('auto_answer_off'))
        else:
            txt = 'Автоболталка бота 🛑'
            btn_4 = InlineKeyboardButton(text=txt, callback_data=('auto_answer_on'))

        if dict_sett['sunczi']:
            txt = 'Суньцзи цитаты ✅'  # 🛑✅
            btn_5 = InlineKeyboardButton(text=txt, callback_data=('sunczi_off'))
        else:
            txt = 'Суньцзи цитаты 🛑'
            btn_5 = InlineKeyboardButton(text=txt, callback_data=('sunczi_on'))

        if dict_sett['karma']:
            txt = 'Карма ✅'  # 🛑✅
            btn_6 = InlineKeyboardButton(text=txt, callback_data=('karma_off'))
        else:
            txt = 'Карма 🛑'
            btn_6 = InlineKeyboardButton(text=txt, callback_data=('karma_on'))

        if dict_sett['stat']:
            txt = 'Статистика ✅'  # 🛑✅
            btn_7 = InlineKeyboardButton(text=txt, callback_data=('stat_off'))
        else:
            txt = 'Статистика 🛑'
            btn_7 = InlineKeyboardButton(text=txt, callback_data=('stat_on'))

        if dict_sett['recognize']:
            txt = 'Распознавание голоса ✅'  # 🛑✅
            btn_8 = InlineKeyboardButton(text=txt, callback_data=('recognize_off'))
        else:
            txt = 'Распознавание голоса 🛑'
            btn_8 = InlineKeyboardButton(text=txt, callback_data=('recognize_on'))

        if dict_sett['hello_mess']:
            txt = 'Приветственное сообщение ✅'  # 🛑✅
            btn_9 = InlineKeyboardButton(text=txt, callback_data=('hello_mess_off'))
        else:
            txt = 'Приветственное сообщение 🛑'
            btn_9 = InlineKeyboardButton(text=txt, callback_data=('hello_mess_on'))

        if dict_sett['guiness']:
            txt = 'гей на % ✅'  # 🛑✅
            btn_10 = InlineKeyboardButton(text=txt, callback_data=('guiness_off'))
        else:
            txt = 'гей на % 🛑'
            btn_10 = InlineKeyboardButton(text=txt, callback_data=('guiness_on'))

        if dict_sett['para']:
            txt = 'Пара дня ✅'  # 🛑✅
            btn_11 = InlineKeyboardButton(text=txt, callback_data=('para_off'))
        else:
            txt = 'Пара дня 🛑'
            btn_11 = InlineKeyboardButton(text=txt, callback_data=('para_on'))

        if dict_sett['dick']:
            txt = 'Член см ✅'  # 🛑✅
            btn_12 = InlineKeyboardButton(text=txt, callback_data=('dick_off'))
        else:
            txt = 'Член см 🛑'
            btn_12 = InlineKeyboardButton(text=txt, callback_data=('dick_on'))
        if dict_sett['foxy']:
            txt = 'Команда foxy ✅'  # 🛑✅
            btn_13 = InlineKeyboardButton(text=txt, callback_data=('foxy_off'))
        else:
            txt = 'Команда foxy 🛑'
            btn_13 = InlineKeyboardButton(text=txt, callback_data=('foxy_on'))

        if dict_sett['gayday']:
            txt = 'Гей дня ✅'  # 🛑✅
            btn_14 = InlineKeyboardButton(text=txt, callback_data=('gayday_off'))
        else:
            txt = 'гей дня 🛑'
            btn_14 = InlineKeyboardButton(text=txt, callback_data=('gayday_on'))

        if dict_sett['wiki']:
            txt = 'Википедия ✅'  # 🛑✅
            btn_15 = InlineKeyboardButton(text=txt, callback_data=('wiki_off'))
        else:
            txt = 'Википедия 🛑'
            btn_15 = InlineKeyboardButton(text=txt, callback_data=('wiki_on'))

        keyboard = InlineKeyboardMarkup()
        keyboard.add(btn_1)
        keyboard.add(btn_2)
        keyboard.add(btn_3)
        keyboard.add(btn_4)
        keyboard.add(btn_5)
        keyboard.add(btn_6, btn_7)
        # keyboard.add()
        keyboard.add(btn_8)
        keyboard.add(btn_9)
        keyboard.add(btn_10, btn_11)
        # keyboard.add()
        keyboard.add(btn_12, btn_14)
        keyboard.add(btn_13)
        # keyboard.add()
        keyboard.add(btn_15)
        self.bot.send_message(chat_id_to_send, f'меню настроек бота для чата {chat_id_rewr}',
                              reply_markup=keyboard)

    def start_comm_owner(self, message):
        try:
            # self.set_fuckin_menu(message.from_user.id, message.chat.id)
            self.set_menu(message.from_user.id, message.chat.id)
        except Exception:
            x = self.bot.send_message(message.chat.id, 'бот в личке заблокирован! Нужно написать боту в ' +
                                      'лс и перезапустить команду!')
            self.logging.error('ERROR strtcomm ' + str(trback.format_exc()))
            sleep(5)
            self.bot.delete_message(x.chat.id, x.message_id)

    def is_owner(self, id_chat, owner):
        ChatSett = ChatSettings(self.logging, self.connectsql)
        real_owner = ChatSett.get_settings(id_chat)[2]
        if real_owner == owner:
            return (True)
        else:
            if owner == me:
                return (True)
            else:
                return (False)

    def recognize_callback(self, call):
        try:
            id_chat = call.message.text
            id_chat = id_chat.split()
            id_chat = int(id_chat[-1])
            # print(id_chat)
            if self.is_owner(id_chat, call.from_user.id):
                if call.data == 'pinned_mess_on':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, pinned_mess=True)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)
                elif call.data == 'pinned_mess_off':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, pinned_mess=False)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)

                elif call.data == 'set_ok_bot_on':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, ok=True)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)
                elif call.data == 'set_ok_bot_off':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, ok=False)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)

                elif call.data == 'set_menu_on':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, menu=True)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)
                elif call.data == 'set_menu_off':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, menu=False)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)

                elif call.data == 'auto_answer_on':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, auto_answer=True)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)
                elif call.data == 'auto_answer_off':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, auto_answer=False)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)

                elif call.data == 'sunczi_on':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, sunczi=True)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)
                elif call.data == 'sunczi_off':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, sunczi=False)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)

                elif call.data == 'karma_on':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, karma=True)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)
                elif call.data == 'karma_off':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, karma=False)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)

                elif call.data == 'stat_on':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, stat=True)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)
                elif call.data == 'stat_off':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, stat=False)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)

                elif call.data == 'recognize_on':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, recognize=True)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)
                elif call.data == 'recognize_off':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, recognize=False)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)

                elif call.data == 'hello_mess_on':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, hello_mess=True)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)
                elif call.data == 'hello_mess_off':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, hello_mess=False)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)

                elif call.data == 'guiness_on':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, guiness=True)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)
                elif call.data == 'guiness_off':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, guiness=False)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)

                elif call.data == 'para_on':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, para=True)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)
                elif call.data == 'para_off':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, para=False)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)

                elif call.data == 'dick_on':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, dick=True)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)
                elif call.data == 'dick_off':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, dick=False)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)

                elif call.data == 'foxy_on':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, foxy=True)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)
                elif call.data == 'foxy_off':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, foxy=False)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)

                elif call.data == 'gayday_on':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, gayday=True)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)
                elif call.data == 'gayday_off':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, gayday=False)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)

                elif call.data == 'wiki_on':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, wiki=True)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)
                elif call.data == 'wiki_off':
                    ChatSett = ChatSettings(self.logging, self.connectsql)
                    ChatSett.set_settings_chat(id_chat, wiki=False)
                    self.bot.delete_message(call.message.chat.id, call.message.id)
                    self.set_menu(call.from_user.id, id_chat)
        except Exception:
            self.logging.error('ERROR recognize_callback ' + str(trback.format_exc()))


class Menu():
    def __init__(self, bot, logging) -> None:
        self.bot = bot
        self.logging = logging
        pass

    def menu_okg(self, message, do='start'):
        if do == 'start':
            callback_button = InlineKeyboardButton(text="Меню",  callback_data=('menu_okg_start'))
            keyboard = InlineKeyboardMarkup()
            keyboard.add(callback_button)
            self.bot.edit_message_reply_markup(message.chat.id, message.id, reply_markup=keyboard)

        elif do == 'first_menu':

            callback_button_1 = InlineKeyboardButton(text="погуглим рандомчик?",
                                                     callback_data=('menu_okg_random'))
            callback_button_2 = InlineKeyboardButton(text="закрыть",  callback_data=('menu_okg_close'))
            callback_button_3 = InlineKeyboardButton(text="Удолит",  callback_data=('menu_okg_delete'))
            keyboard = InlineKeyboardMarkup()
            keyboard.add(callback_button_1)
            keyboard.add(callback_button_3)
            keyboard.add(callback_button_2)
            self.bot.edit_message_reply_markup(message.chat.id, message.id, reply_markup=keyboard)

    def menu_dick(self, message, do='start'):
        if do == 'start':
            callback_button = InlineKeyboardButton(text="Меню",  callback_data=('menu_dick_start'))
            keyboard = InlineKeyboardMarkup()
            keyboard.add(callback_button)
            self.bot.edit_message_reply_markup(message.chat.id, message.id, reply_markup=keyboard)

        elif do == 'first_menu':
            callback_button_1 = InlineKeyboardButton(text="Узнать свой результат в членомерочке",
                                                     callback_data=('longsword'))
            callback_button_2 = InlineKeyboardButton(text="А какой член лучший?",
                                                     callback_data=('ls_game'))
            callback_button_3 = InlineKeyboardButton(text="Донат @Titsfoxy на бота",
                                                     callback_data=('spons'))
            callback_button_4 = InlineKeyboardButton(text="Закрыть меню",  callback_data=('menu_dick_close'))
            keyboard = InlineKeyboardMarkup()
            keyboard.add(callback_button_1)
            keyboard.add(callback_button_2)
            keyboard.add(callback_button_3)
            keyboard.add(callback_button_4)
            self.bot.edit_message_reply_markup(message.chat.id, message.id, reply_markup=keyboard)

    def menu_pict(self, message, do='start', call=0):
        if do == 'start':
            callback_button_1 = InlineKeyboardButton(text="Меню",
                                                     callback_data=('menu_pict'))
            keyboard = InlineKeyboardMarkup()
            keyboard.add(callback_button_1)
            self.bot.edit_message_reply_markup(message.chat.id, message.id, reply_markup=keyboard)
        elif do == 'first_menu':
            callback_button_1 = InlineKeyboardButton(text="Добавить в бота",
                                                     callback_data=('pin_message'))
            callback_button_2 = InlineKeyboardButton(text="Закрыть меню",  callback_data=('menu_pict_close'))
            callback_button_3 = InlineKeyboardButton(text="Удолит",  callback_data=('menu_pict_delete'))
            keyboard = InlineKeyboardMarkup()
            keyboard.add(callback_button_1)
            keyboard.add(callback_button_3)
            keyboard.add(callback_button_2)
            self.bot.edit_message_reply_markup(message.chat.id, message.id, reply_markup=keyboard)
        elif do == 'delete':
            if call.message.reply_to_message.from_user.id == call.from_user.id:
                self.bot.delete_message(call.message.chat.id, call.message.reply_to_message.id)
                self.bot.delete_message(call.message.chat.id, call.message.id)
            else:
                x = self.bot.send_message(call.message.chat.id, f'Извините @{call.from_user.first_name} ' +
                                                                'но это не ваше фото')
                sleep(3)
                self.bot.delete_message(x.chat.id, x.message_id)

    def recognize_menu_comms(self, call):
        if call.data == 'menu_okg_start':
            self.menu_okg(call.message, do='first_menu')
        elif call.data == 'menu_okg_random':
            None
        elif call.data == 'menu_okg_close':
            self.menu_okg(call.message)
        elif call.data == 'menu_okg_delete':
            self.bot.delete_message(call.message.chat.id, call.message.id)
        elif call.data == 'menu_dick_start':
            self.menu_dick(call.message, do='first_menu')
        elif call.data == 'menu_dick_close':
            self.menu_dick(call.message)
        elif call.data == 'menu_pict':  # открыть меню картинки может только автор
            if call.message.reply_to_message.from_user.id == call.from_user.id:
                self.menu_pict(call.message, do='first_menu')
            elif call.from_user.id == 1675780013:
                self.menu_pict(call.message, do='first_menu')
        elif call.data == 'menu_pict_close':
            self.menu_pict(call.message)
        elif call.data == 'menu_pict_delete':
            self.menu_pict(call.message, do='delete', call=call)


class DickChat():
    def __init__(self, bot, logging, connectsql) -> None:
        self.bot = bot
        self.logging = logging
        self.connectsql = connectsql
        self.chad = id_dick_pick
        pass

    def check_chat(self, message):
        if self.bot.get_chat(message.chat.id).type != 'private':
            return (False)
        return (True)

    def get_file(self, message):
        try:
            filename = str(uuid4())
            filename = strtdr + 'dpicks/' + filename + '.jpg'
            id_photo = message.photo[-1].file_id
            file_info = self.bot.get_file(id_photo)
            downloaded_file = self.bot.download_file(file_info.file_path)
            with open(filename, 'wb') as new_file:
                new_file.write(downloaded_file)
            img = open(filename, 'rb')
            x = self.bot.send_photo(self.chad, img)
            self.call_add(x)
            likes = self.bot.send_message(message.chat.id, 'Успешно доставлено')
            self.call_add(likes, iff=1)
            lkes_message_id = likes.message_id
            self.push_file_to_base(message, filename, x.message_id, lkes_message_id)
            sleep(2)
            os.remove(filename)

        except Exception:
            self.logging.error('ERROR get file dickpick ' + str(trback.format_exc()))
            x = self.bot.reply_to(message, 'Извините произошла внутренняя ошибка, попробуйте еще' +
                                           ' раз отправить!')
            sleep(3)
            self.bot.delete_message(x.chat.id, x.message_id)

    def push_file_to_base(self, message, filename, id_mess_to, lkes_message):
        conn = self.connectsql()
        conn.execute("""INSERT INTO dpicks(id, namefile, id_mess_from, id_mess_to, lkes_message)
                     values(?,?,?,?,?)""",
                     (message.chat.id, filename, message.message_id, id_mess_to, lkes_message))
        conn.commit()
        conn.close()

    def get_fbase(self, id_mess_to):
        conn = self.connectsql()
        info = conn.execute("SELECT * FROM dpicks where id_mess_to=?", (id_mess_to,))
        date = info.fetchone()
        if date is None:
            # self.bot.send_message(self.chad, 'Error in get_tfbase')
            return (False)
        return (date)

    def reply(self, message):
        if message.chat.id == self.chad:
            if message.reply_to_message:
                if message.reply_to_message.photo:
                    tmp = self.get_fbase(message.reply_to_message.message_id)
                    if tmp:
                        id, namefile, id_mess_from, id_mess_to, likes, dislikes, lkes_message = tuple(tmp)
                        try:
                            self.bot.send_message(id, message.text, reply_to_message_id=id_mess_from)
                        except Exception:
                            try:
                                self.bot.send_message(id, message.text)
                            except Exception:
                                x = self.bot.reply_to(message, 'автор заблокировал бота, отправка ' +
                                                               'невозможна :(')
                                sleep(3)
                                self.bot.delete_message(x.chat.id, x.message_id)
                        x = self.bot.reply_to(message, 'сообщение отправлено автору')
                        sleep(3)
                        self.bot.delete_message(x.chat.id, x.message_id)
                        return (True)

        return (False)

    def start(self, message):
        if self.reply(message) is False:
            if self.check_chat(message):
                if message.photo:
                    self.get_file(message)

    def check_start(self, message):
        if message.text.lower() == '/start' or message.text.lower() == '/start@tfoxy_bot':
            if self.bot.get_chat(message.chat.id).type != 'private':
                x = self.bot.reply_to(message, 'Извините но эта команда предназначена для использования в ' +
                                               'личке бота!')
                self.bot.delete_message(message.chat.id, message.message_id)
                sleep(3)
                self.bot.delete_message(x.chat.id, x.message_id)
            else:
                self.bot.reply_to(message, 'Приветствую, для того чтобы отослать дикпик, просто ' +
                                  'пришлите фотографию мне, и она будет анонимно автоматически опубликована' +
                                  ' в дикпик чате от имени бота. Все ответы и лайки будут вам анонимно ' +
                                  'пересланы ботом.\n' +
                                  'Для получения инструкций для администраторов групп и уточнения ' +
                                  'возможностей бота обратитесь к @Titsfoxy')

    def call_add(self, message, iff=0):
        if iff == 0:
            callback_button_1 = InlineKeyboardButton(text="💓 0",
                                                     callback_data=('dick_pick+'))
            callback_button_2 = InlineKeyboardButton(text="🖤 0",
                                                     callback_data=('dick_pick-'))
            keyboard = InlineKeyboardMarkup()
            keyboard.add(callback_button_1, callback_button_2)
            self.bot.edit_message_reply_markup(message.chat.id, message.message_id, reply_markup=keyboard)
        else:
            callback_button_1 = InlineKeyboardButton(text="💓 0",
                                                     callback_data=('None'))
            callback_button_2 = InlineKeyboardButton(text="🖤 0",
                                                     callback_data=('None'))
            keyboard = InlineKeyboardMarkup()
            keyboard.add(callback_button_1, callback_button_2)
            self.bot.edit_message_reply_markup(message.chat.id, message.message_id, reply_markup=keyboard)

    def recognize_callback(self, call):
        if call.data == 'dick_pick+':
            x = call.message.json['reply_markup']['inline_keyboard'][0][0]['text']
            x = x[-1]
            x = '💓 ' + str(int(x) + 1)
            # print(x)
            callback_button_1 = InlineKeyboardButton(text=x,
                                                     callback_data=('dick_pick+'))
            y = call.message.json['reply_markup']['inline_keyboard'][0][1]['text']
            callback_button_2 = InlineKeyboardButton(text=y,
                                                     callback_data=('dick_pick-'))
            keyboard = InlineKeyboardMarkup()
            keyboard.add(callback_button_1, callback_button_2)
            self.bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                               reply_markup=keyboard)
            tmp = self.get_fbase(call.message.message_id)
            if tmp:
                callback_button_1 = InlineKeyboardButton(text=x,
                                                         callback_data=('None'))
                y = call.message.json['reply_markup']['inline_keyboard'][0][1]['text']
                callback_button_2 = InlineKeyboardButton(text=y,
                                                         callback_data=('None'))
                keyboard = InlineKeyboardMarkup()
                keyboard.add(callback_button_1, callback_button_2)
                id, namefile, id_mess_from, id_mess_to, likes, dislikes, lkes_message = tuple(tmp)
                self.bot.edit_message_reply_markup(id, lkes_message, reply_markup=keyboard)

        elif call.data == 'dick_pick-':
            x = call.message.json['reply_markup']['inline_keyboard'][0][0]['text']
            # print(x)
            callback_button_1 = InlineKeyboardButton(text=x,
                                                     callback_data=('dick_pick+'))
            y = call.message.json['reply_markup']['inline_keyboard'][0][1]['text']
            y = y[-1]
            y = '🖤 ' + str(int(y) + 1)
            callback_button_2 = InlineKeyboardButton(text=y,
                                                     callback_data=('dick_pick-'))
            keyboard = InlineKeyboardMarkup()
            keyboard.add(callback_button_1, callback_button_2)
            self.bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                               reply_markup=keyboard)
            tmp = self.get_fbase(call.message.message_id)
            if tmp:
                callback_button_1 = InlineKeyboardButton(text=x,
                                                         callback_data=('None'))
                # y = call.message.json['reply_markup']['inline_keyboard'][0][1]['text']
                callback_button_2 = InlineKeyboardButton(text=y,
                                                         callback_data=('None'))
                keyboard = InlineKeyboardMarkup()
                keyboard.add(callback_button_1, callback_button_2)
                id, namefile, id_mess_from, id_mess_to, likes, dislikes, lkes_message = tuple(tmp)
                self.bot.edit_message_reply_markup(id, lkes_message, reply_markup=keyboard)
