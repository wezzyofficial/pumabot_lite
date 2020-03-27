import os, random, time
from modules import symbCheck, anek
from plugins import profiles, entertaining, economy, bank, game, nick, farm, gf, shop, salem

helpTextPath = 'help.txt'
users_dir = os.path.join(r"users/")

#Проверка на ник
def check_user_mention(from_id):
    get_data = gf.loadjson(users_dir + str(from_id) + ".json")
    if get_data['nick'] == '0':
        return '@id{}'.format(from_id) + '(' + get_data['first_name'] + ')'
    else:
        return '@id{}'.format(from_id) + '(' + get_data['user_nick'] + ')'

def reg(first_name, last_name, from_id):
    user_id = str(from_id)
    fist_name = str(first_name)
    last_name = str(last_name)

    bonus_money = 50000
    profileList = {"first_name": '{}'.format(fist_name), "last_name": '{}'.format(last_name),
                   "id": '{}'.format(str(user_id)), "nick": '{}'.format(str('0')),
                   "user_nick": '{}'.format('None'), "balance": '{}'.format(int(bonus_money)),
                   "bank_balance": '{}'.format(0), "bank_cr_balance": '{}'.format(20),
                   "bonus_timer": '{}'.format('0.0'), "group": '{}'.format('Player'),
                   "country": '{}'.format('Пумаляндия'), "bank_vd": '{}'.format('0'),
                   "bank_vd_id": '{}'.format('0'), "bank_vd_proc": '{}'.format('0.0'),
                   "bank_vd_time": '{}'.format('0.0'), "bank_vd_money": '{}'.format('0.0'),
                    "own_housing": '{}'.format(0), "own_car": '{}'.format(0),
                   "own_yacht": '{}'.format(0), "own_air": '{}'.format(0), "own_helicopter": '{}'.format(0),
                   "own_farm": '{}'.format(0), "own_comp": '{}'.format(0), "own_smart": '{}'.format(0),
                   "farm_profit": '{}'.format(0), "farm_time": '{}'.format(0.0),
                   "data_reg": '{}'.format(str(time.strftime("%d.%m.%Y", time.localtime())))}
    gf.dumpjson(profileList, users_dir + str(user_id) + ".json")

def pluginMg(text, from_id):
    text = text.lower()

    #Подключение плагинов
    ballPl = entertaining.choiceBall(text)
    choicePl = entertaining.choiceWord(text)
    infaPl = entertaining.infaWord(text)
    casinoPl = game.casino(text, str(from_id))
    profilesPl = profiles.profiles(text, str(from_id))
    economyPl = economy.economy(text, str(from_id))
    bankPl = bank.bankSys(text, str(from_id))
    farmPl = farm.farm(text, str(from_id))
    salemPl = salem.salem(text, str(from_id))
    nickPl = nick.nicks(text, str(from_id))
    shopPl = shop.shop(text, str(from_id))

    if not symbCheck.symbCheck(text):
        if text != '':
            if text == 'начать':
                return 'Привет, ' + str(check_user_mention(from_id)) + '! Вижу ты впервые, я развлекательный бот для тебя и твоих друзей! :)\n\nРад познакомиться, держи 50.000€ в ПОДАРОК! 🤑\n\nСписок моих команд ты всегда можешь посмотреть, для этого напиши мне "помощь" 😉'
            elif text in ['помощь', '📚 помощь']:
                helpFile = open(helpTextPath, encoding='utf-8')
                return str(check_user_mention(from_id)) + helpFile.read()
            elif text == 'анекдот':
                return str(check_user_mention(from_id)) + ', лови —' + random.choice(anek.get_aneks(delimeter='', count=1))
            elif profilesPl:
                return str(check_user_mention(from_id)) + profilesPl
            elif shopPl:
                return str(check_user_mention(from_id)) + shopPl
            elif salemPl:
                return str(check_user_mention(from_id)) + salemPl
            elif choicePl:
                return str(check_user_mention(from_id)) + choicePl
            elif ballPl:
                return str(check_user_mention(from_id)) + ballPl
            elif infaPl:
                return str(check_user_mention(from_id)) + infaPl
            elif nickPl:
                return str(check_user_mention(from_id)) + nickPl
            elif economyPl:
                return str(check_user_mention(from_id)) + economyPl
            elif casinoPl:
                return str(check_user_mention(from_id)) + casinoPl
            elif bankPl:
                return str(check_user_mention(from_id)) + bankPl
            elif farmPl:
                return str(check_user_mention(from_id)) + farmPl
        else:
            pass
    else:
        pass