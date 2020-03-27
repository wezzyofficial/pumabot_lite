import random
import json
import os
from plugins import gf

users_dir = os.path.join(r"users/")

casinoHelp = ', помощь по играм:\n\n⠀⠀🚀 Казино Platinum – развлекательный центр, готовый принять всех. У персонала Platinum одна забота: сделать так, чтобы гости хорошо провели время. Platinum удовлетворит любой ваш каприз. 😉\n\n❓ Помощь:\n⠀⠀🎰 Казино [сумма/все]\n⠀⠀📈 Трейд [вверх/вниз] [сумма]\n⠀⠀🎲 Кубик [число 1-6]\n⠀⠀🥛 Стаканчик [1-3] [сумма]\n⠀⠀🔘 Монетка [орел/решка]'
casinoHelp2 = '⠀🚀 Казино Platinum – развлекательный центр, готовый принять всех. У персонала Platinum одна забота: сделать так, чтобы гости хорошо провели время. Platinum удовлетворит любой ваш каприз. 😉\n\n❓ Помощь:\n⠀⠀🎰 Казино [сумма/все]\n⠀⠀📈 Трейд [вверх/вниз] [сумма]\n⠀⠀🎲 Кубик [число 1-6]\n⠀⠀🥛 Стаканчик [1-3] [сумма]\n⠀⠀🔘 Монетка [орел/решка]'

def casino(sourceText, id):
    get_data = gf.loadjson(users_dir + str(id) + ".json")
    if 'казино' == sourceText.split()[0].lower():
        if len(sourceText.split()) > 1:
            summa = sourceText.split()[1].lower()
            if summa.isdigit():
                if int(summa) >= 1:
                    if int(summa) <= int(get_data['balance']):
                        if int(get_data['balance']) > 0:
                            if summa.isdigit():
                                casino_win = gf.check_casino_win(id)
                                if str(casino_win) == '1':
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    balance_do = int(get_data['balance'])
                                    user_balance = int(get_data['balance']) + int(summa)
                                    balance_posle = user_balance - balance_do
                                    get_data.update({"balance": '{}'.format(str(user_balance))})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    message_1 = ', вы выиграли: ' + str(balance_posle) + '€ 😯\n💰 Ваш баланс: ' + str(user_balance) + '€'
                                    return message_1
                                elif str(casino_win) == '2':
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    balance_do = int(get_data['balance'])
                                    user_balance = int(get_data['balance']) - int(summa)
                                    balance_posle = balance_do - user_balance
                                    get_data.update({"balance": '{}'.format(str(user_balance))})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    message_2 = ', вы проиграли: ' + str(balance_posle) + '€ 😔\n💰 Ваш баланс: ' + str(user_balance) + '€'
                                    return message_2
                                else:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    user_balance = int(get_data['balance'])
                                    message_3 = ', деньги остаются при Вас! ☺\n💰 Ваш баланс: ' + str(user_balance) + '€'
                                    return message_3
                            else:
                                return ', буквы и символы запрещены, Используйте цифры! 😕'
                        else:
                            return ', ваш баланс равен 0 рублей! 😕'
                    else:
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        user_balance = get_data['balance']
                        return ', у вас недостаточно денег, ставка выше чем денег у вас на балансе! 😔\n💰 Ваш баланс: ' + str(user_balance) + '€'
                else:
                    return ', ставка должна быть больше 0! 😔'

            elif sourceText.split()[1].lower() == 'все':
                user_balance = int(get_data['balance'])
                if user_balance >= 1:
                    casino_win = gf.check_casino_win(id)
                    if str(casino_win) == '1':
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        summa = int(get_data['balance'])
                        user_balance = int(get_data['balance']) + int(user_balance)
                        get_data.update({"balance": '{}'.format(str(user_balance))})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        message_1 = ', вы выиграли: ' + str(summa) + '€ 😯\n💰 Ваш баланс: ' + str(user_balance) + '€'
                        return message_1
                    elif str(casino_win) == '2':
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        summa = int(get_data['balance'])
                        user_balance = int(get_data['balance']) - int(user_balance)
                        balance_posle = user_balance - user_balance
                        get_data.update({"balance": '{}'.format(str(user_balance))})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        message_2 = ', вы проиграли: ' + str(summa) + '€ 😔\n💰 Ваш баланс: ' + str(balance_posle) + '€'
                        return message_2
                    else:
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        user_balance = int(get_data['balance'])
                        message_3 = ', деньги остаются при Вас! ☺\n💰 Ваш баланс: ' + str(user_balance) + '€'
                        return message_3
                else:
                    return ', ваш баланс равен 0 рублей! 😕'
            else:
                return ', буквы и символы запрещены! 😕'
        else:
            return casinoHelp
    elif 'кубик' == sourceText.split()[0].lower():
        if len(sourceText.split()) > 1:
            chislo = sourceText.split()[1].lower()
            if chislo.isdigit():
                get_data = gf.loadjson(users_dir + str(id) + ".json")
                group = str(get_data['group'])
                cubic_win = random.randint(1, 6)
                if int(chislo) <= 6:
                    if str(chislo) == '0': return ', слишком маленькое число! Используйте (число от 1 до 6) 😕'
                    chislo = int(chislo)
                    if chislo != cubic_win:
                        if group == 'VIP':
                            pass_count = 4
                            while pass_count and cubic_win != chislo:
                                cubic_win = random.randint(1, 6)
                                pass_count -= 1
                        elif group == 'Premium':
                            pass_count = 3
                            while pass_count and cubic_win != chislo:
                                cubic_win = random.randint(1, 6)
                                pass_count -= 1
                        else:
                            pass_count = 1
                            while pass_count and cubic_win != chislo:
                                cubic_win = random.randint(1, 6)
                                pass_count -= 1

                    if str(chislo) == str(cubic_win):
                        with open(users_dir + str(id) + ".json", "r", encoding='utf-8') as user_profile:
                            get_data = json.load(user_profile, encoding='utf-8')
                            user_balance = int(get_data['balance']) + int(2000)
                            get_data.update({"balance": '{}'.format(str(user_balance))})
                        with open(users_dir + str(id) + ".json", "w", encoding='utf-8') as write_file:
                            json.dump(get_data, write_file, ensure_ascii=False)
                        message_1 = ', вы угадали! Ваш выигрыш +2.000€ 🤩'
                        return message_1
                    else:
                        message_2 = ', вы проиграли! Выпало число: ' + str(cubic_win) + ' 😔'
                        return message_2
                else:
                    return ', слишком большое число! Используйте (число от 1 до 6) 😕'
            else:
                return ', буквы и символы запрещены! Используйте (число от 1 до 6) 😕'
        else:
            return casinoHelp
    elif 'монетка' == sourceText.split()[0].lower():
        if len(sourceText.split()) == 2:
            get_data = gf.loadjson(users_dir + str(id) + ".json")
            group = str(get_data['group'])
            chislo = sourceText.split()[1].lower()
            summa = 2000
            monetka_win = random.randint(1, 2)
            if chislo.isalpha() and chislo in ['орёл', 'орел', 'решка']:
                chislo = gf.check_word_monetka(chislo)
                if chislo != monetka_win:
                    if group == 'Premium':
                        pass_count = 2
                        while pass_count and monetka_win != chislo:
                            monetka_win = random.randint(1, 2)
                            pass_count -= 1
                    elif group == 'VIP':
                        pass_count = 1
                        while pass_count and monetka_win != chislo:
                            monetka_win = random.randint(1, 2)
                            pass_count -= 1
                    else:
                        pass_count = 0
                        while pass_count and monetka_win != chislo:
                            monetka_win = random.randint(1, 2)
                            pass_count -= 1

                if int(chislo) == int(monetka_win):
                    with open(users_dir + str(id) + ".json", "r", encoding='utf-8') as user_profile:
                        get_data = json.load(user_profile, encoding='utf-8')
                        user_balance = int(get_data['balance']) + int(summa)
                        get_data.update({"balance": '{}'.format(str(user_balance))})
                    with open(users_dir + str(id) + ".json", "w", encoding='utf-8') as write_file:
                        json.dump(get_data, write_file, ensure_ascii=False)
                    message_1 = ', вы угадали! 😍 Ваш приз: +2.000€ 🤑\n💰 В кошельке: ' + str(user_balance) + '€'
                    gen_chislo = random.randint(1, 2)
                    if int(gen_chislo) == 1:
                        return message_1
                    else:
                        return message_1
                else:
                    message_2 = ', вы не угадали! 😣 ' + str(gf.convert_win_monetka(monetka_win)) + '. 😔'
                    gen_chislo = random.randint(1, 2)
                    if int(gen_chislo) == 1:
                        return message_2
                    else:
                        return message_2
            else:
                return ', использование: «Монетка [орел/решка]»'
        elif len(sourceText.split()) >= 3:
            return casinoHelp
        else:
            return casinoHelp

    elif 'трейд' == sourceText.split()[0].lower():
        if len(sourceText.split()) == 3:
            get_data = gf.loadjson(users_dir + str(id) + ".json")
            group = str(get_data['group'])
            word = sourceText.split()[1].lower()
            traid_win = random.randint(1, 2)
            summa = sourceText.split()[2].lower()
            if word.isalpha() and word in ['вверх', 'вниз']:
                user_balance = int(get_data['balance'])
                if user_balance >= 1:
                    if summa.isdigit():
                        chislo = gf.check_word_traid(word)
                        if chislo != traid_win:
                            if group == 'Premium':
                                pass_count = 2
                                while pass_count and traid_win != chislo:
                                    traid_win = random.randint(1, 2)
                                    pass_count -= 1
                            elif group == 'VIP':
                                pass_count = 1
                                while pass_count and traid_win != chislo:
                                    traid_win = random.randint(1, 2)
                                    pass_count -= 1
                            else:
                                pass_count = 0
                                while pass_count and traid_win != chislo:
                                    traid_win = random.randint(1, 2)
                                    pass_count -= 1

                        if int(chislo) == int(traid_win):
                            gen_traid = random.randint(5, 45)
                            trade_wins = random.randint(200, 500)
                            with open(users_dir + str(id) + ".json", "r", encoding='utf-8') as user_profile:
                                get_data = json.load(user_profile, encoding='utf-8')
                                user_balance = int(get_data['balance']) + int(trade_wins)
                                get_data.update({"balance": '{}'.format(str(user_balance))})
                            with open(users_dir + str(id) + ".json", "w", encoding='utf-8') as write_file:
                                json.dump(get_data, write_file, ensure_ascii=False)
                            message_1 = ', курс поднялся⤴ на ' + str(gen_traid) + '€\n✅ Вы заработали +' + str(trade_wins) + '€\n💰 В кошельке: ' + str(user_balance) + '€'
                            message_2 = ', курс упал⤵ на ' + str(gen_traid) + '€\n✅ Вы заработали +' + str(trade_wins) + '€\n💰 В кошельке: ' + str(user_balance) + '€'
                            gen_chislo = random.randint(1, 2)
                            if int(gen_chislo) == 1:
                                return message_1
                            else:
                                return message_2
                        else:
                            gen_traid = random.randint(5, 45)
                            with open(users_dir + str(id) + ".json", "r", encoding='utf-8') as user_profile:
                                get_data = json.load(user_profile, encoding='utf-8')
                                user_balance = int(get_data['balance']) - int(summa)
                                get_data.update({"balance": '{}'.format(str(user_balance))})
                            with open(users_dir + str(id) + ".json", "w", encoding='utf-8') as write_file:
                                json.dump(get_data, write_file, ensure_ascii=False)

                            gen_chislo = random.randint(1, 2)
                            message_1 = ', курс поднялся⤴ на ' + str(gen_traid) + '€\n❌ Вы потеряли: ' + str(summa) + '€\n💰 В кошельке: ' + str(user_balance) + '€'
                            message_2 = ', курс упал⤵ на ' + str(gen_traid) + '€\n❌ Вы потеряли: ' + str(summa) + '€\n💰 В кошельке: ' + str(user_balance) + '€'
                            if int(gen_chislo) == 1:
                                return message_1
                            else:
                                return message_2
                    else:
                        return ', использование: «Трейд [вверх/вниз] [сумма]»'
                else:
                    return ', ваш баланс равен 0 рублей! 😕'
            else:
                return ', использование: «Трейд [вверх/вниз] [сумма]»'
        elif len(sourceText.split()) >= 3:
            return casinoHelp
        else:
            return casinoHelp

    elif 'стаканчик' == sourceText.split()[0].lower():
        if len(sourceText.split()) > 2:
            get_data = gf.loadjson(users_dir + str(id) + ".json")
            group = str(get_data['group'])
            user_balance = get_data['balance']
            chislo = sourceText.split()[1].lower()
            summa = sourceText.split()[2].lower()
            if chislo.isdigit() and summa.isdigit():
                if int(summa) <= int(user_balance):
                    if int(get_data['balance']) > 0:
                            glass_win = random.randint(1, 3)
                            if int(chislo) <= 3:
                                if int(chislo) == 0: return ', число должно быть больше 0! Используйте (число от 1 до 3) 😕'
                                if int(summa) == 0: return ', сумма должна быть больше 0! 😕'
                                chislo = int(chislo)
                                if chislo != glass_win:
                                    if group == 'Premium':
                                        pass_count = 3
                                        while pass_count and glass_win != chislo:
                                            glass_win = random.randint(1, 3)
                                            pass_count -= 1
                                    elif group == 'VIP':
                                        pass_count = 1
                                        while pass_count and glass_win != chislo:
                                            glass_win = random.randint(1, 3)
                                            pass_count -= 1
                                    else:
                                        pass_count = 0
                                        while pass_count and glass_win != chislo:
                                            glass_win = random.randint(1, 3)
                                            pass_count -= 1

                                if int(chislo) == int(glass_win):
                                    with open(users_dir + str(id) + ".json", "r", encoding='utf-8') as user_profile:
                                        get_data = json.load(user_profile, encoding='utf-8')
                                        user_balance = int(get_data['balance']) + int(summa)
                                        get_data.update({"balance": '{}'.format(str(user_balance))})
                                    with open(users_dir + str(id) + ".json", "w", encoding='utf-8') as write_file:
                                        json.dump(get_data, write_file, ensure_ascii=False)
                                    return ', вы угадали! 😯 Приз: ' + str(summa) + '€\n💰 Ваш баланс: ' + str(user_balance) + '€'
                                else:
                                    with open(users_dir + str(id) + ".json", "r", encoding='utf-8') as user_profile:
                                        get_data = json.load(user_profile, encoding='utf-8')
                                        user_balance = int(get_data['balance']) - int(summa)
                                        get_data.update({"balance": '{}'.format(str(user_balance))})
                                    with open(users_dir + str(id) + ".json", "w", encoding='utf-8') as write_file:
                                        json.dump(get_data, write_file, ensure_ascii=False)
                                    return ', вы не угадали, это был: ' + str(glass_win) + '-ый стаканчик! 😔\n💰 Ваш баланс: ' + str(user_balance) + '€'
                            else:
                                return ', слишком большое число! 😕'
                    else:
                        return ', ваш баланс равен 0 рублей! 😕'
                else:
                    file = open(users_dir + str(id) + ".json", "r", encoding='utf-8')
                    get_data = json.load(file, encoding='utf-8')
                    file.close()
                    user_balance = get_data['balance']
                    return ', у вас недостаточно денег, ставка выше чем денег у вас на балансе! 😔\n💰 Ваш баланс: ' + str(user_balance) + '€'
            else:
                return ', буквы и символы запрещены! 😕'

        else:
            return casinoHelp
    else:
        return None