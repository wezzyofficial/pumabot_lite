import json
import os
import time

users_dir = os.path.join(r"users/")

def loadjson(filepath):
    with open(filepath, 'r', encoding='utf-8') as jsonfile:
        return json.load(jsonfile, encoding='utf-8')

def dumpjson(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as jsonfile:
        return json.dump(data, jsonfile, ensure_ascii=False)

def bankSys(sourceText, id):
    bankHelp = '\n\n❓ Помощь:\n⠀⠀📈 Банк курс\n⠀⠀💱 Банк обмен\n⠀⠀💸 Банк снять [сумма/все]\n⠀⠀💶 Банк пополнить [сумма/все]'
    procHelp = '\n\n✅ Автоматический вклад под 1.2% каждый день!'
    NoprocHelp = '\n\n🔔 Авто-вклад работает, когда на карте меньше 10.000.000€!'

    if sourceText != '':
        if 'банк' == sourceText.split()[0].lower():
            get_data = loadjson(users_dir + str(id) + ".json")
            if int(get_data['own_smart']) >= 1:
                if len(sourceText.split()) > 1:
                    if sourceText.split()[1].lower() == 'обмен':
                        get_data = loadjson("curs.json")
                        price_coin = int(get_data['coin'])
                        get_data = loadjson(users_dir + str(id) + ".json")
                        bank_cr_balance = int(get_data['bank_cr_balance'])
                        if bank_cr_balance >= 1:
                            get_data = loadjson(users_dir + str(id) + ".json")
                            user_balance = int(get_data['balance'])

                            algo_obmen_euro = price_coin * bank_cr_balance
                            algo_update_balance = user_balance + algo_obmen_euro
                            algo_obmen_btc = bank_cr_balance - bank_cr_balance
                            get_data.update({"balance": '{}'.format(algo_update_balance)})
                            get_data.update({"bank_cr_balance": '{}'.format(algo_obmen_btc)})

                            dumpjson(get_data, users_dir + str(id) + ".json")
                            return ', вы обменяли: ' + str(bank_cr_balance) + '฿ на ' + str(algo_obmen_euro) + '€! 🤑\n💰 В кошельке: ' + str(algo_update_balance) + '€'
                        else:
                            return ', на счёте в банке - у вас меньше 1 биткоина! 🙁'
                    elif sourceText.split()[1].lower() == 'пополнить':
                        if len(sourceText.split()) > 2:
                            get_data = loadjson(users_dir + str(id) + ".json")
                            summa_up = sourceText.split()[2].lower()
                            user_balance = get_data['balance']
                            if summa_up.isdigit():
                                if int(summa_up) == 0: return ', сумма должна быть больше 0! 😕'
                                if int(user_balance) >= int(summa_up):
                                    get_data = loadjson(users_dir + str(id) + ".json")
                                    bank_balance = int(get_data['bank_balance'])
                                    user_balance = int(get_data['balance'])
                                    algo_popoln_bank_balance = int(bank_balance) + int(summa_up)
                                    algo_snyat_user_balance = int(user_balance) - int(summa_up)
                                    get_data.update({"bank_balance": '{}'.format(int(algo_popoln_bank_balance))})
                                    get_data.update({"balance": '{}'.format(int(algo_snyat_user_balance))})
                                    dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы пополнили карту на: ' + str(summa_up) + '€ 😀\n💳 В банке: ' + str(algo_popoln_bank_balance) + '€\n💰 В кошельке: ' + str(algo_snyat_user_balance) + '€'
                                else:
                                    get_data = loadjson(users_dir + str(id) + ".json")
                                    balanсe_out = get_data['balance']
                                    return ', у вас недостаточно средств в кошельке, для пополнение карты! 😔\n💰 У вас в кошельке: ' + str(balanсe_out) + '€'
                            elif sourceText.split()[2].lower() == 'все':
                                if int(user_balance) >= int(1):
                                    get_data = loadjson(users_dir + str(id) + ".json")
                                    bank_balance = int(get_data['bank_balance'])
                                    user_balance = int(get_data['balance'])
                                    algo_popoln_bank_balance = int(bank_balance) + int(user_balance)
                                    algo_snyat_user_balance = int(user_balance) - int(user_balance)
                                    get_data.update({"bank_balance": '{}'.format(int(algo_popoln_bank_balance))})
                                    get_data.update({"balance": '{}'.format(int(algo_snyat_user_balance))})
                                    dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы пополнили карту на: ' + str(user_balance) + '€ 😀\n💳 В банке: ' + str(algo_popoln_bank_balance) + '€\n💰 В кошельке: ' + str(algo_snyat_user_balance) + '€'
                                else:
                                    get_data = loadjson(users_dir + str(id) + ".json")
                                    balanсe_out = get_data['balance']
                                    return ', у вас недостаточно средств в кошельке, для пополнение карты! 😔\n💰 В кошельке: ' + str(balanсe_out) + '€'
                            elif sourceText.split()[2].lower() == 'всё':
                                if int(user_balance) >= int(1):
                                    get_data = loadjson(users_dir + str(id) + ".json")
                                    bank_balance = int(get_data['bank_balance'])
                                    user_balance = int(get_data['balance'])
                                    algo_popoln_bank_balance = int(bank_balance) + int(user_balance)
                                    algo_snyat_user_balance = int(user_balance) - int(user_balance)
                                    get_data.update({"bank_balance": '{}'.format(int(algo_popoln_bank_balance))})
                                    get_data.update({"balance": '{}'.format(int(algo_snyat_user_balance))})
                                    dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы пополнили карту на: ' + str(user_balance) + '€ 😀\n💳 В банке: ' + str(algo_popoln_bank_balance) + '€\n💰 В кошельке: ' + str(algo_snyat_user_balance) + '€'
                                else:
                                    get_data = loadjson(users_dir + str(id) + ".json")
                                    balanсe_out = get_data['balance']
                                    return ', у вас недостаточно средств в кошельке, для пополнение карты! 😔\n💰 У вас в кошельке: ' + str(balanсe_out) + '€'
                            else:
                                return ', для пополнения карты, используйте для суммы - цифры! 😉'
                        else:
                            return ', использование: 💶 Банк пополнить [сумма/все]'
                    elif sourceText.split()[1].lower() == 'курс':
                        get_data = loadjson("curs.json")
                        price_coin = int(get_data['coin'])
                        return ', курс игровой валюты!\n\n⠀📈 По информации Банка на сегодня, цена за каждую единицу валюты составляет:\n\n⠀⠀🏮 Биткоин: ' + str(price_coin) + '€ за 1฿.'
                    elif sourceText.split()[1].lower() == 'снять':
                        if len(sourceText.split()) > 2:
                            get_data = loadjson(users_dir + str(id) + ".json")
                            summa_up = sourceText.split()[2].lower()
                            bank_balance = get_data['bank_balance']
                            if summa_up.isdigit():
                                if int(summa_up) == 0: return ', сумма должна быть больше 0! 😕'
                                if int(bank_balance) >= int(summa_up):
                                    get_data = loadjson(users_dir + str(id) + ".json")
                                    bank_balance = int(get_data['bank_balance'])
                                    user_balance = int(get_data['balance'])
                                    algo_popoln_bank_balance = int(bank_balance) - int(summa_up)
                                    algo_snyat_user_balance = int(user_balance) + int(summa_up)
                                    get_data.update({"bank_balance": '{}'.format(int(algo_popoln_bank_balance))})
                                    get_data.update({"balance": '{}'.format(int(algo_snyat_user_balance))})
                                    dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы сняли: ' + str(summa_up) + '€ с карты! 😀\n💳 В банке: ' + str(algo_popoln_bank_balance) + '€\n💰 В кошельке: ' + str(algo_snyat_user_balance) + '€'
                                else:
                                    get_data = loadjson(users_dir + str(id) + ".json")
                                    user_balance = get_data['balance']
                                    bank_balance = get_data['bank_balance']
                                    return ', у вас недостаточно средств на карте, для получение наличных! 😔\n💳 В банке: ' + str(bank_balance) + '€\n💰 В кошельке: ' + str(user_balance) + '€'
                            elif sourceText.split()[2].lower() == 'все':
                                if int(bank_balance) >= int(1):
                                    get_data = loadjson(users_dir + str(id) + ".json")
                                    bank_balance = int(get_data['bank_balance'])
                                    user_balance = int(get_data['balance'])
                                    algo_snyat_user_balance = int(user_balance) + int(bank_balance)
                                    algo_popoln_bank_balance = int(bank_balance) - int(bank_balance)
                                    get_data.update({"bank_balance": '{}'.format(int(algo_popoln_bank_balance))})
                                    get_data.update({"balance": '{}'.format(int(algo_snyat_user_balance))})
                                    dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы сняли ' + str(bank_balance) + '€ с карты! 😀\n💳 В банке: ' + str(algo_popoln_bank_balance) + '€\n💰 В кошельке: ' + str(algo_snyat_user_balance) + '€'
                                else:
                                    get_data = loadjson(users_dir + str(id) + ".json")
                                    user_balance = get_data['balance']
                                    bank_balance = get_data['bank_balance']
                                    return ', у вас недостаточно средств на карте, для получение наличных! 😔\n💳 В банке: ' + str(bank_balance) + '€\n💰 В кошельке: ' + str(user_balance) + '€'
                            elif sourceText.split()[2].lower() == 'всё':
                                if int(bank_balance) >= int(1):
                                    get_data = loadjson(users_dir + str(id) + ".json")
                                    bank_balance = int(get_data['bank_balance'])
                                    user_balance = int(get_data['balance'])
                                    algo_snyat_user_balance = int(user_balance) + int(bank_balance)
                                    algo_popoln_bank_balance = int(bank_balance) - int(bank_balance)
                                    get_data.update({"bank_balance": '{}'.format(int(algo_popoln_bank_balance))})
                                    get_data.update({"balance": '{}'.format(int(algo_snyat_user_balance))})
                                    dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы сняли ' + str(bank_balance) + '€ с карты! 😀\n💳 В банке: ' + str(algo_popoln_bank_balance) + '€\n💰 В кошельке: ' + str(algo_snyat_user_balance) + '€'
                                else:
                                    get_data = loadjson(users_dir + str(id) + ".json")
                                    user_balance = get_data['balance']
                                    bank_balance = get_data['bank_balance']
                                    return ', у вас недостаточно средств на карте, для получение наличных! 😔\n💳 В банке: ' + str(bank_balance) + '€\n💰 В кошельке: ' + str(user_balance) + '€'
                            else:
                                return ', для снятие денег с банковского счёта, используйте для суммы - цифры! 😉'
                        else:
                            return ', использование: 💸 Банк снять [сумма/все]'
                    else:
                        get_data = loadjson(users_dir + str(id) + ".json")
                        if int(get_data['bank_balance']) <= 20000000:
                            bank_proc_raznica_time = float(time.time()) - float(get_data['bank_vd_time'])
                            bank_hours = int(bank_proc_raznica_time) / 3600
                            bank_balance = int(get_data['bank_balance'])
                            if bank_hours >= 24:
                                bank_proc_profit = int(1.2 * bank_balance)
                                get_data = loadjson(users_dir + str(id) + ".json")
                                get_data.update({"bank_balance": '{}'.format(int(bank_proc_profit))})
                                get_data.update({"bank_vd_time": '{}'.format(time.time())})
                                dumpjson(get_data, users_dir + str(id) + ".json")
                                return ', помощь по банку:\n\n📋 Счёт в банке:\n⠀⠀💳 На карте: ' + str(bank_proc_profit) + '€\n⠀⠀🏮 Биткоинов: ' + str(get_data['bank_cr_balance']) + '฿' + bankHelp + procHelp
                            else:
                                get_data = loadjson(users_dir + str(id) + ".json")
                                return ', помощь по банку:\n\n📋 Счёт в банке:\n⠀⠀💳 На карте: ' + str(get_data['bank_balance']) + '€\n⠀⠀🏮 Биткоинов: ' + str(get_data['bank_cr_balance']) + '฿' + bankHelp + procHelp
                        else:
                            get_data = loadjson(users_dir + str(id) + ".json")
                            return ', помощь по банку:\n\n📋 Счёт в банке:\n⠀⠀💳 На карте: ' + str(get_data['bank_balance']) + '€\n⠀⠀🏮 Биткоинов: ' + str(get_data['bank_cr_balance']) + '฿' + bankHelp + NoprocHelp
                else:
                    get_data = loadjson(users_dir + str(id) + ".json")
                    if int(get_data['bank_balance']) <= 20000000:
                        bank_proc_raznica_time = float(time.time()) - float(get_data['bank_vd_time'])
                        bank_hours = int(bank_proc_raznica_time) / 3600
                        bank_balance = int(get_data['bank_balance'])
                        if bank_hours >= 24:
                            bank_proc_profit = int(1.2 * bank_balance)
                            get_data = loadjson(users_dir + str(id) + ".json")
                            get_data.update({"bank_balance": '{}'.format(int(bank_proc_profit))})
                            get_data.update({"bank_vd_time": '{}'.format(time.time())})
                            dumpjson(get_data, users_dir + str(id) + ".json")
                            return ', помощь по банку:\n\n📋 Счёт в банке:\n⠀⠀💳 На карте: ' + str(bank_proc_profit) + '€\n⠀⠀🏮 Биткоинов: ' + str(get_data['bank_cr_balance']) + '฿' + bankHelp + procHelp
                        else:
                            get_data = loadjson(users_dir + str(id) + ".json")
                            return ', помощь по банку:\n\n📋 Счёт в банке:\n⠀⠀💳 На карте: ' + str(
                                get_data['bank_balance']) + '€\n⠀⠀🏮 Биткоинов: ' + str(get_data['bank_cr_balance']) + '฿' + bankHelp + procHelp
                    else:
                        get_data = loadjson(users_dir + str(id) + ".json")
                        return ', помощь по банку:\n\n📋 Счёт в банке:\n⠀⠀💳 На карте: ' + str(get_data['bank_balance']) + '€\n⠀⠀🏮 Биткоинов: ' + str(get_data['bank_cr_balance']) + '฿' + bankHelp + NoprocHelp
            else:
                return ', для использования банка, преобретите телефон! 😐\n📱 Посмотреть телефоны: Магазин телефон'
        else:
            return None
    pass