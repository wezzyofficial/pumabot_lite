import json
import os
from plugins import gf

users_dir = os.path.join(r"users/")

def loadjson(filepath):
    with open(filepath, 'r', encoding='utf-8') as jsonfile:
        return json.load(jsonfile, encoding='utf-8')


def dumpjson(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as jsonfile:
        return json.dump(data, jsonfile, ensure_ascii=False)

def check_sale_price(own_type, own_id):
    if own_type == 1:
        if own_id == 1:
            return 25000 / 2
        elif own_id == 2:
            return 65000 / 2
        elif own_id == 3:
            return 225000 / 2
        elif own_id == 4:
            return 595000 / 2
        elif own_id == 5:
            return 655000 / 2
        elif own_id == 6:
            return 1525000 / 2
        elif own_id == 7:
            return 8525000 / 2
        elif own_id == 8:
            return 35650000 / 2
        elif own_id == 9:
            return 68250000 / 2
        elif own_id == 10:
            return 93500000 / 2
        elif own_id == 11:
            return 999999999 / 2
        else:
            return 0
    elif own_type == 2:
        if own_id == 1:
            return 125000 / 2
        elif own_id == 2:
            return 255000 / 2
        elif own_id == 3:
            return 525000 / 2
        elif own_id == 4:
            return 1275000 / 2
        elif own_id == 5:
            return 1650000 / 2
        elif own_id == 6:
            return 2000000 / 2
        elif own_id == 7:
            return 4350000 / 2
        elif own_id == 8:
            return 16650000 / 2
        elif own_id == 9:
            return 25735000 / 2
        elif own_id == 10:
            return 30800000 / 2
        elif own_id == 11:
            return 37580000 / 2
        elif own_id == 12:
            return 57999999 / 2
        elif own_id == 13:
            return 108555000 / 2
        elif own_id == 14:
            return 999999999 / 2
        elif own_id == 15:
            return 1500000000 / 2
        else:
            return 0
    elif own_type == 3:
        if own_id == 1:
            return 575000 / 2
        elif own_id == 2:
            return 1225000 / 2
        elif own_id == 3:
            return 2500000 / 2
        elif own_id == 4:
            return 3650000 / 2
        elif own_id == 5:
            return 8355000 / 2
        elif own_id == 6:
            return 12850000 / 2
        elif own_id == 7:
            return 23125000 / 2
        elif own_id == 8:
            return 34666000 / 2
        elif own_id == 9:
            return 66225000 / 2
        elif own_id == 10:
            return 96000000 / 2
        elif own_id == 11:
            return 126650000 / 2
        elif own_id == 12:
            return 527777777 / 2
        elif own_id == 13:
            return 999999999 / 2
        elif own_id == 14:
            return 1255000000 / 2
        else:
            return 0
    elif own_type == 4:
        if own_id == 1:
            return 500000 / 2
        elif own_id == 2:
            return 3995000 / 2
        elif own_id == 3:
            return 6350000 / 2
        elif own_id == 4:
            return 15500000 / 2
        elif own_id == 5:
            return 17800000 / 2
        elif own_id == 6:
            return 22250000 / 2
        elif own_id == 7:
            return 43000000 / 2
        elif own_id == 8:
            return 65505000 / 2
        elif own_id == 9:
            return 75985000 / 2
        elif own_id == 10:
            return 86495000 / 2
        elif own_id == 11:
            return 109999999 / 2
        elif own_id == 12:
            return 313000000 / 2
        elif own_id == 13:
            return 617555000 / 2
        elif own_id == 14:
            return 850000000 / 2
        elif own_id == 15:
            return 2000000000 / 2
        else:
            return 0
    elif own_type == 5:
        if own_id == 1:
            return 1300000 / 2
        elif own_id == 2:
            return 1750000 / 2
        elif own_id == 3:
            return 2225000 / 2
        elif own_id == 4:
            return 3500000 / 2
        elif own_id == 5:
            return 8850000 / 2
        elif own_id == 6:
            return 25555555 / 2
        elif own_id == 7:
            return 58000000 / 2
        elif own_id == 8:
            return 215000000 / 2
        elif own_id == 9:
            return 525000000 / 2
        else:
            return 0
    elif own_type == 6:
        if own_id == 1:
            return 500000 / 2
        elif own_id == 2:
            return 5000000 / 2
        elif own_id == 3:
            return 500000000 / 2
        else:
            return 0
    elif own_type == 7:
        #компы
        if own_id == 1:
            return 35000000 / 2
        elif own_id == 2:
            return 45000000 / 2
        elif own_id == 3:
            return 150000000 / 2
        else:
            return 0
    elif own_type == 8:
        if own_id == 1:
            return 25800000 / 2
        elif own_id == 2:
            return 30000000 / 2
        elif own_id == 3:
            return 35250000 / 2
        else:
            return 0

def salem(sourceText, id):
    get_data = loadjson(users_dir + str(id) + ".json")
    saleMhelp = ', помощь по продажам:\n\n⠀💠 Купленное имущество можно легко продавать. За продажу имущества - вы получаете половину стоимости имущества на баланс!\n\n⭐ Для продажи имущества укажите категорию!\n\n❓ Помощь:\n⠀⠀⛏ Копать [железо/золото/алмазы]\n⠀⠀💠 Продать [железо/золото/алмазы]'

    if sourceText != '':
        if 'продать' == sourceText.split()[0].lower():
            if len(sourceText.split()) > 1:
                if sourceText.split()[1].lower() == 'дом':
                    get_data = loadjson(users_dir + str(id) + ".json")
                    own_housing = int(get_data['own_housing'])
                    own_car = int(check_sale_price(2, int(get_data['own_car'])))
                    own_yacht = int(check_sale_price(3, int(get_data['own_yacht'])))
                    own_air = int(check_sale_price(4, int(get_data['own_air'])))
                    own_helicopter = int(check_sale_price(5, int(get_data['own_helicopter'])))
                    own_farm = int(check_sale_price(6, int(get_data['own_farm'])))
                    user_balance = int(get_data['balance'])
                    algo_sale_house = user_balance + int(check_sale_price(1, own_housing)) + own_car + own_yacht + own_air + own_helicopter + own_farm
                    if own_housing >= 1:
                        if own_housing != 30:
                            get_data = loadjson(users_dir + str(id) + ".json")
                            get_data.update({"own_housing": '{}'.format(0)})
                            get_data.update({"own_car": '{}'.format(0)})
                            get_data.update({"own_yacht": '{}'.format(0)})
                            get_data.update({"own_air": '{}'.format(0)})
                            get_data.update({"own_helicopter": '{}'.format(0)})
                            get_data.update({"own_farm": '{}'.format(0)})
                            get_data.update({"farm_profit": '{}'.format(0)})
                            get_data.update({"farm_time": '{}'.format(0.0)})
                            get_data.update({"balance": '{}'.format(algo_sale_house)})
                            dumpjson(get_data, users_dir + str(id) + ".json")
                            return ', вы продали свой дом, а также всё имущество (если оно есть), кроме - Телефона и Компьютера! ✅'
                        else:
                            return ', продать секретное имущество нельзя! 😄'
                    else:
                        return ', у вас нет дома! ⛔'
                elif sourceText.split()[1].lower() in ['машину', 'машина']:
                    get_data = loadjson(users_dir + str(id) + ".json")
                    own_car = int(get_data['own_car'])
                    user_balance = int(get_data['balance'])
                    algo_sale = user_balance + int(check_sale_price(2, own_car))
                    if own_car >= 1:
                        if own_car != 30:
                            get_data = loadjson(users_dir + str(id) + ".json")
                            get_data.update({"own_car": '{}'.format(0)})
                            get_data.update({"balance": '{}'.format(algo_sale)})
                            dumpjson(get_data, users_dir + str(id) + ".json")
                            return ', вы продали свою машину! ✅'
                        else:
                            return ', продать секретное имущество нельзя! 😄'
                    else:
                        return ', у вас нет машины! ⛔'
                elif sourceText.split()[1].lower() in ['яхту', 'яхта']:
                    get_data = loadjson(users_dir + str(id) + ".json")
                    own_yacht = int(get_data['own_yacht'])
                    user_balance = int(get_data['balance'])
                    algo_sale = user_balance + int(check_sale_price(3, own_yacht))
                    if own_yacht >= 1:
                        if own_yacht != 30:
                            get_data = loadjson(users_dir + str(id) + ".json")
                            get_data.update({"own_yacht": '{}'.format(0)})
                            get_data.update({"balance": '{}'.format(algo_sale)})
                            dumpjson(get_data, users_dir + str(id) + ".json")
                            return ', вы продали свою яхту! ✅'
                        else:
                            return ', продать секретное имущество нельзя! 😄'
                    else:
                        return ', у вас нет яхты! ⛔'
                elif sourceText.split()[1].lower() in ['самолет', 'самолёт']:
                    get_data = loadjson(users_dir + str(id) + ".json")
                    own_air = int(get_data['own_air'])
                    user_balance = int(get_data['balance'])
                    algo_sale = user_balance + int(check_sale_price(4, own_air))
                    if own_air >= 1:
                        if own_air != 30:
                            get_data = loadjson(users_dir + str(id) + ".json")
                            get_data.update({"own_air": '{}'.format(0)})
                            get_data.update({"balance": '{}'.format(algo_sale)})
                            dumpjson(get_data, users_dir + str(id) + ".json")
                            return ', вы продали свой самолёт! ✅'
                        else:
                            return ', продать секретное имущество нельзя! 😄'
                    else:
                        return ', у вас нет самолёта! ⛔'
                elif sourceText.split()[1].lower() in ['вертолет', 'вертолёт']:
                    get_data = loadjson(users_dir + str(id) + ".json")
                    own_helicopter = int(get_data['own_helicopter'])
                    user_balance = int(get_data['balance'])
                    algo_sale = user_balance + int(check_sale_price(5, own_helicopter))
                    if own_helicopter >= 1:
                        if own_helicopter != 30:
                            get_data = loadjson(users_dir + str(id) + ".json")
                            get_data.update({"own_helicopter": '{}'.format(0)})
                            get_data.update({"balance": '{}'.format(algo_sale)})
                            dumpjson(get_data, users_dir + str(id) + ".json")
                            return ', вы продали свой вертолёт! ✅'
                        else:
                            return ', продать секретное имущество нельзя! 😄'
                    else:
                        return ', у вас нет вертолёта! ⛔'
                elif sourceText.split()[1].lower() in ['ферму', 'ферма']:
                    get_data = loadjson(users_dir + str(id) + ".json")
                    own_farm = int(get_data['own_farm'])
                    user_balance = int(get_data['balance'])
                    algo_sale = user_balance + int(check_sale_price(6, own_farm))
                    if own_farm >= 1:
                        get_data = loadjson(users_dir + str(id) + ".json")
                        get_data.update({"own_farm": '{}'.format(0)})
                        get_data.update({"farm_profit": '{}'.format(0)})
                        get_data.update({"farm_time": '{}'.format(0.0)})
                        get_data.update({"balance": '{}'.format(algo_sale)})
                        dumpjson(get_data, users_dir + str(id) + ".json")
                        return ', вы продали свою ферма! ✅'
                    else:
                        return ', у вас нет фермы! ⛔'
                elif sourceText.split()[1].lower() in ['компьютер', 'комп']:
                    get_data = loadjson(users_dir + str(id) + ".json")
                    own_comp = int(get_data['own_comp'])
                    user_balance = int(get_data['balance'])
                    algo_sale = user_balance + int(check_sale_price(7, own_comp))
                    if own_comp >= 1:
                        get_data = loadjson(users_dir + str(id) + ".json")
                        get_data.update({"own_comp": '{}'.format(0)})
                        get_data.update({"balance": '{}'.format(algo_sale)})
                        dumpjson(get_data, users_dir + str(id) + ".json")
                        return ', вы продали свой компьютер! ✅'
                    else:
                        return ', у вас нет компьютера! ⛔'
                elif sourceText.split()[1].lower() in ['смартфон', 'телефон']:
                    get_data = loadjson(users_dir + str(id) + ".json")
                    own_smart = int(get_data['own_smart'])
                    user_balance = int(get_data['balance'])
                    algo_sale = user_balance + int(check_sale_price(8, own_smart))
                    if own_smart >= 1:
                        get_data = loadjson(users_dir + str(id) + ".json")
                        get_data.update({"own_smart": '{}'.format(0)})
                        get_data.update({"balance": '{}'.format(algo_sale)})
                        dumpjson(get_data, users_dir + str(id) + ".json")
                        return ', вы продали свой телефон! ✅'
                    else:
                        return ', у вас нет телефона! ⛔'
                else:
                    return saleMhelp
            else:
                return saleMhelp
        else:
            return None
    pass