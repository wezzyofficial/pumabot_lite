import random
import os
import time
from datetime import datetime
from plugins import gf

users_dir = os.path.join(r"users/")

def bonus_time(id):
    get_data = gf.loadjson(users_dir + str(id) + ".json")
    if get_data['group'] == 'Player':
        return 86399
    elif get_data['group'] == 'VIP':
        return 43200
    elif get_data['group'] == 'Premium':
        return 21600

def economy(sourceText, id):
    if sourceText != '':
        if 'баланс' == sourceText.split()[0].lower():
            get_data = gf.loadjson(users_dir + str(id) + ".json")
            return ', в кошельке: ' + get_data['balance'] + '€ 💰'
        elif sourceText.split()[0].lower() in ['бонус', '💎']:
            get_data = gf.loadjson(users_dir + str(id) + ".json")
            group = get_data['group']
            bonus_time_in = get_data['bonus_timer']
            if time.time() > float(bonus_time_in):
                if group == 'Player':
                    random_bonus = int(random.randint(1, 2))
                    if random_bonus == 1:
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        BonusMoney = int(random.randint(5000, 15000))
                        user_balance = int(get_data['balance'])
                        goBonus = user_balance + BonusMoney
                        get_data.update({"balance": '{}'.format(str(goBonus))})
                        get_data.update({"bonus_timer": '{}'.format(time.time() + int(bonus_time(id)))})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        return ', ваш бонус: ' + str(BonusMoney) + '€ 💰'
                    else:
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        BonusCoin = int(random.randint(5, 15))
                        user_coin_balance = int(get_data['bank_cr_balance'])
                        goBonus = user_coin_balance + BonusCoin
                        get_data.update({"bank_cr_balance": '{}'.format(goBonus)})
                        get_data.update({"bonus_timer": '{}'.format(time.time() + int(bonus_time(id)))})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        return ', ваш бонус: ' + str(BonusCoin) + '฿ 🏮'
                elif group == 'VIP':
                    random_bonus = random.randint(1, 2)
                    if random_bonus == 1:
                        BonusMoney = int(random.randint(15000, 25000))
                        user_balance = int(get_data['balance'])
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        goBonus = user_balance + BonusMoney
                        get_data.update({"balance": '{}'.format(goBonus)})
                        get_data.update({"bonus_timer": '{}'.format(time.time() + int(bonus_time(id)))})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        return ', ваш бонус: ' + str(BonusMoney) + '€! 😄'
                    else:
                        BonusCoin = int(random.randint(10, 20))
                        user_coin_balance = int(get_data['bank_cr_balance'])
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        goBonus = user_coin_balance + BonusCoin
                        get_data.update({"bank_cr_balance": '{}'.format(goBonus)})
                        get_data.update({"bonus_timer": '{}'.format(time.time() + int(bonus_time(id)))})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        return ', ваш бонус: ' + str(BonusCoin) + '฿! 😄'
                elif group == 'Premium':
                    random_bonus = random.randint(1, 2)
                    if random_bonus == 1:
                        BonusMoney = int(random.randint(25000, 55000))
                        user_balance = int(get_data['balance'])
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        goBonus = user_balance + BonusMoney
                        get_data.update({"balance": '{}'.format(goBonus)})
                        get_data.update({"bonus_timer": '{}'.format(time.time() + int(bonus_time(id)))})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        return ', ваш бонус: ' + str(BonusMoney) + '€! 😄'
                    else:
                        BonusCoin = int(random.randint(25, 55))
                        user_coin_balance = int(get_data['bank_cr_balance'])
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        goBonus = user_coin_balance + BonusCoin
                        get_data.update({"bank_cr_balance": '{}'.format(goBonus)})
                        get_data.update({"bonus_timer": '{}'.format(time.time() + int(bonus_time(id)))})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        return ', ваш бонус: ' + str(BonusCoin) + '฿! 😄'
            else:
                get_data = gf.loadjson(users_dir + str(id) + ".json")
                rasnica = float(get_data['bonus_timer']) - time.time()
                return ', вы уже получали бонус, пожалуйста повторите попытку через: ' + str(datetime.strftime(datetime.utcfromtimestamp(rasnica), '%H:%M:%S')) + ' ☺'

        elif 'перевод' == sourceText.split()[0].lower():
            if len(sourceText.split()) > 2:
                perevodToId = str(gf.removeLink(sourceText.split()[1].lower()))
                summa_perevoda = sourceText.split()[2].lower()
                if summa_perevoda.isdigit() and perevodToId.isdigit():
                    if perevodToId != id:
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        balanсe_out = get_data['balance']

                        check_profile = os.path.exists(users_dir + str(perevodToId) + ".json")
                        if check_profile == True:
                            if int(summa_perevoda) <= int(get_data['balance']):
                                get_data = gf.loadjson(users_dir + str(id) + ".json")
                                goBonus = int(get_data['balance']) - int(summa_perevoda)
                                get_data.update({"balance": '{}'.format(str(goBonus))})
                                users_otID_name = get_data['first_name'] + ' ' + get_data['last_name']
                                gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                balanсe_out = get_data['balance']

                                get_data = gf.loadjson(users_dir + str(perevodToId) + ".json")
                                goBonus = int(get_data['balance']) + int(summa_perevoda)
                                get_data.update({"balance": '{}'.format(str(goBonus))})
                                users_toID_name = get_data['first_name'] + ' ' + get_data['last_name']
                                users_toID_balance = get_data['balance']
                                gf.dumpjson(get_data, users_dir + str(perevodToId) + ".json")
                                gf.sendMessageTOid(', перевод от: ' + str(users_otID_name) + ' на сумму ' + str(summa_perevoda) + '€ 😯\n💰 Ваш баланс: ' + str(users_toID_balance) + '€', perevodToId)
                                return ', вы перевели пользователю: ' + str(users_toID_name) + ' - ' + str(summa_perevoda) + '€ 😯\n💰 Ваш баланс: ' + str(balanсe_out) + '€'
                            else:
                                return ', у вас недостаточно денег для перевода! 😔\n💰 Ваш баланс: ' + str(balanсe_out) + '€'
                        else:
                            return ', такой пользователь не зарегистрирован! 😔'
                    else:
                        return ', выполнить перевод самому себе - нельзя! 😔'
                else:
                    return ', буквы и символы запрещены! 😕\n🤝 Используйте: «Перевод [ID игрока] [сумма]»'
            else:
                return ', команда перевод позволяет перевести игровую валюту с баланса - другому игроку! 😉\n🤝 Используйте: «Перевод [ID игрока] [сумма]»'
        else:
            return None
    pass
