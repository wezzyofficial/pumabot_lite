import os
import time
from plugins import gf

users_dir = os.path.join(r"users/")

def shop(sourceText, id):
    get_data = gf.loadjson(users_dir + str(id) + ".json")
    user_balance = int(get_data['balance'])

    shopHelp = ', помощь по магазину:\n\n⠀🛒 Покупайте различное имущество в один клик! После покупки дома, вы сможете преобрести транспорт и ферму для майнинга биткоинов.\n\n📌 Основное:\n⠀⠀🏠 Дома\n⠀⠀🚗 Машины\n⠀⠀✈ Самолёты\n⠀⠀🚁 Вертолёты\n⠀⠀🛥 Яхты\n\n💡 Остальное:\n⠀⠀🖥 Компьютеры\n⠀⠀📱 Телефоны\n⠀⠀🔋 Фермы\n\n❓ Помощь:\n⠀⠀🔎 Магазин [категория] - товары.\n⠀⠀🛒 Магазин [категория] [номер] - купить товар.'

    if sourceText != '':
        if 'магазин' == sourceText.split()[0].lower():
            if len(sourceText.split()) == 2:
                if sourceText.split()[1].lower() in ['дом', 'дома']:
                    return ', список доступных домов:\n\n⠀🔔 После покупки дома, вы сможете купить транспорт и ферму!\n\n⠀⠀🏠 1. Коробка — 25.000€\n⠀⠀🏠 2. Подвал — 65.000€\n⠀⠀🏠 3. Сарай — 225.000€\n⠀⠀🏠 4. Гараж — 595.000€\n⠀⠀🏠 5. Ветхая хижина — 655.000€\n⠀⠀🏠 6. Деревянный домик — 1.525.000€\n⠀⠀🏠 7. Кирпичный дом — 8.525.000€\n⠀⠀🏠 8. Коттедж — 35.650.000€\n⠀⠀🏠 9. Дом на Пумавуде — 68.250.000€\n⠀⠀🏠 10. Вилла на Пумавуде — 93.500.000€\n⠀⠀🏠 11. Личный остров — 999.999.999€\n\n❓ Для покупки дома, используйте:\n⠀⠀🛒 Магазин дом [номер]'
                elif sourceText.split()[1].lower() in ['машина', 'машины']:
                    return ', список доступных машин:\n\n⠀🔔 Покупайте транспорт в один клик!\n\n⠀⠀🚗 1. Велосипед — 125.000€\n⠀⠀🚗 2. Гироскутер — 255.000€\n⠀⠀🏍 3. Ducati Scrambler — 525.000€\n⠀⠀🏍 4. Honda CTX1300 — 1.275.000€\n⠀⠀🚗 5. Ferrari California front — 1.650.000€\n⠀⠀🚗 6. Porsche 911 — 2.000.000€\n⠀⠀🚗 7. Nissan GT-R — 4.350.000€\n⠀⠀🚗 8. BMW X6 — 15.650.000€\n⠀⠀🚗 9. Jaguar F-Type — 25.735.000€\n⠀⠀🚗 10. Lamborghini Huracán — 30.800.000€\n⠀⠀🚗 11. Lamborghini Gallardo — 37.580.000€\n⠀⠀🚗 12. Ferrari F80 Concept — 57.999.999€\n⠀⠀🚗 13. Lamborghini Sesto — 108.555.000€\n⠀⠀🚗 14. Various Ford-based trucks — 999.999.999€\n⠀⠀🚗 15. Tesla Cybertruck — 1.500.000.000€\n\n❓ Для покупки транспорта, используйте:\n⠀⠀🛒 Магазин машина [номер]'
                elif sourceText.split()[1].lower() in ['яхта', 'яхты']:
                    return ', список доступных яхт:\n\n⠀⠀🛥 1. RHIB — 575.000€\n⠀⠀🛥 2. Kawasaki — 1.225.000€\n⠀⠀🛥 3. Riva Aquarama — 2.500.000€\n⠀⠀🛥 4. Various — 3.650.000€\n⠀⠀🛥 5. Рrinсеss 60 — 8.355.000€\n⠀⠀🛥 6. Аzimut 70 — 12.850.000€\n⠀⠀🛥 7. Dоminаtоr 40M — 23.125.000€\n⠀⠀🛥 8. Mооnеn 124 — 34.666.000€\n⠀⠀🛥 9. Widеr 150 — 66.225.000€\n⠀⠀🛥 10. Palmer Jоhnsоn 42M SuреrSроrt — 96.000.000€\n⠀⠀🛥 11. Widеr 165 — 126.650.000€\n⠀⠀🛥 12. Есliрsе — 527.777.777€\n⠀⠀🛥 13. Dubаi — 999.999.999€\n⠀⠀🛥 14. Strееts оf Mоnасо — 1.255.000.000€\n\n❓ Для покупки транспорта, используйте:\n⠀⠀🛒 Магазин яхта [номер]'
                elif sourceText.split()[1].lower() in ['самолёт', 'самолет', 'самолёты', 'самолеты']:
                    return ', список доступных самолётов:\n\n⠀🔔 Покупайте транспорт в один клик!\n\n⠀⠀✈ 1. de Havilland Canada DHC-2 — 500.000€\n⠀⠀✈ 2. Piper PA-46 — 3.995.000€\n⠀⠀✈ 3. Cessna 310 — 6.350.000€\n⠀⠀✈ 4. Learjet 55 — 15.500.000€\n⠀⠀✈ 5. Bombardier Global Express — 17.800.000€\n⠀⠀✈ 6. Cessna Citation X — 22.250.000€\n⠀⠀✈ 7. C-130 — 43.000.000€\n⠀⠀✈ 8. VOLATOL — 65.505.000€\n⠀⠀✈ 9. RM-10 BOMBUSHKA — 75.985.000€\n⠀⠀✈ 10. AVENGER — HYV — 86.495.000€\n⠀⠀✈ 11. F-16 Fighting Falcon — 109.999.999€\n⠀⠀✈ 12. RM-10 BOMBUSHKA — 313.000.000€\n⠀⠀✈ 13. TULA — MAMMOTH — 617.555.000€\n⠀⠀✈ 14. V-65 MOLOTOK — 850.000.000€\n⠀⠀✈ 15. MOGUL — MAMMOTH — 2.000.000.000€\n\n❓ Для покупки транспорта, используйте:\n⠀⠀🛒 Магазин самолёт [номер]'
                elif sourceText.split()[1].lower() in ['вертолёт', 'вертолет', 'вертолёты', 'вертолеты']:
                    return ', список доступных вертолётов:\n\n⠀🔔 Покупайте транспорт в один клик!\n\n⠀⠀🚁 1. Eurocopter EC130/135/14 — 1.300.000€\n⠀⠀🚁 2. Boeing MH-6 — 1.750.000€\n⠀⠀🚁 3. Sikorsky UH-60 — 2.225.000€\n⠀⠀🚁 4. HAVOK — NAGASAKI — 3.500.000€\n⠀⠀🚁 5. Eurocopter EC145 — 8.850.000€\n⠀⠀🚁 6. Airbus H160 — 25.555.555€\n⠀⠀🚁 7. Mil Mi-24 — 58.000.000€\n⠀⠀🚁 8. POLICE MAVERICK — 215.000.000€\n⠀⠀🚁 9. MAVERICK — 525.000.000€\n\n❓ Для покупки транспорта, используйте:\n⠀⠀🛒 Магазин вертолёт [номер]'
                elif sourceText.split()[1].lower() in ['ферма', 'фермы']:
                    return ', список доступных ферм:\n\n⠀🔔 После покупки фермы, вы сможете майнить биткоины!\n\n⠀⠀🔋 1. Miner (5฿/день) — 500.000€\n⠀⠀🔋 2. Miner S (50฿/день) — 5.000.000€\n⠀⠀🔋 3. Miner X (1 000฿/день) — 500.000.000€\n\n❓ Для покупки фермы, используйте:\n⠀⠀🛒 Магазин ферма [номер]'
                elif sourceText.split()[1].lower() in ['комп', 'компьютер', 'ноут', 'ноутбук', 'компы', 'компьютеры', 'ноуты', 'ноутбуки']:
                    return ', список доступных компьютеров:\n\n⠀🔔 После покупки компьютера, вы сможете производить взломы!\n\n⠀⠀🖥 1. Book — 35.000.000€\n⠀⠀🖥 2. Book Air — 45.000.000€\n⠀⠀🖥 3. Book Pro — 150.000.000€\n\n❓ Для покупки компьютера, используйте:\n⠀⠀🛒 Магазин компьютер [номер]'
                elif sourceText.split()[1].lower() in ['телефон', 'смартфон', 'телефоны', 'смартфоны']:
                    return ', список доступных телефонов:\n\n⠀🔔 Покупайте телефоны в один клик!\n\n⠀⠀📱 1. iPhone — 25.800.000€\n⠀⠀📱 2. iPhone Pro — 30.000.000€\n⠀⠀📱 3. iPhone Pro Max — 35.250.000€\n\n❓ Для покупки смартфона, используйте:\n⠀⠀🛒 Магазин смартфон [номер]'
            elif len(sourceText.split()) == 3:
                id_own = str(sourceText.split()[2].lower())
                if sourceText.split()[1].lower() in ['дом', 'дома']:
                    own_housing = int(get_data['own_housing'])
                    price_own_housing1 = 25000
                    price_own_housing2 = 65000
                    price_own_housing3 = 225000
                    price_own_housing4 = 595000
                    price_own_housing5 = 655000
                    price_own_housing6 = 1525000
                    price_own_housing7 = 8525000
                    price_own_housing8 = 35650000
                    price_own_housing9 = 68250000
                    price_own_housing10 = 93500000
                    price_own_housing11 = 999999999
                    if id_own.isdigit():
                        if int(id_own) == 1:
                            if own_housing == 0:
                                if price_own_housing1 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing1
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 🏠 Коробку за ' + str(price_own_housing1) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть дом! 😉'
                        elif int(id_own) == 2:
                            if own_housing == 0:
                                if price_own_housing2 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing2
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 🏠 Подвал за ' + str(price_own_housing2) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть дом! 😉'
                        elif int(id_own) == 3:
                            if own_housing == 0:
                                if price_own_housing3 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing3
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 🏠 Сарай за ' + str(price_own_housing3) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть дом! 😉'
                        elif int(id_own) == 4:
                            if own_housing == 0:
                                if price_own_housing4 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing4
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 🏠 Гараж за ' + str(price_own_housing4) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть дом! 😉'
                        elif int(id_own) == 5:
                            if own_housing == 0:
                                if price_own_housing5 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing5
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 🏠 Ветхую хижину за ' + str(price_own_housing5) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть дом! 😉'
                        elif int(id_own) == 6:
                            if own_housing == 0:
                                if price_own_housing6 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing6
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 🏠 Деревянный домик за ' + str(price_own_housing6) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть дом! 😉'
                        elif int(id_own) == 7:
                            if own_housing == 0:
                                if price_own_housing7 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing7
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 🏠 Кирпичный дом за ' + str(price_own_housing7) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть дом! 😉'
                        elif int(id_own) == 8:
                            if own_housing == 0:
                                if price_own_housing8 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing8
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 🏠 Коттедж за ' + str(price_own_housing8) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть дом! 😉'
                        elif int(id_own) == 9:
                            if own_housing == 0:
                                if price_own_housing9 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing9
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 🏠 Дом на Пумавуде за ' + str(price_own_housing9) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть дом! 😉'
                        elif int(id_own) == 10:
                            if own_housing == 0:
                                if price_own_housing10 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing10
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 🏠 Виллу на Пумавуде за ' + str(price_own_housing10) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть дом! 😉'
                        elif int(id_own) == 11:
                            if own_housing == 0:
                                if price_own_housing11 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing11
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 🏠 Личный остров за ' + str(price_own_housing11) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть дом! 😉'
                        else:
                            return ', дома с таким ID не существует! 😔'
                    else:
                        return ', символы и буквы запрещены! 😔'

                elif sourceText.split()[1].lower() in ['машина', 'машины']:
                    own_car = int(get_data['own_car'])
                    own_housing = int(get_data['own_housing'])
                    if own_housing >= 1 or own_housing != 30:
                        price_own_car1 = 125000
                        price_own_car2 = 255000
                        price_own_car3 = 525000
                        price_own_car4 = 1275000
                        price_own_car5 = 1650000
                        price_own_car6 = 2000000
                        price_own_car7 = 4350000
                        price_own_car8 = 15650000
                        price_own_car9 = 25735000
                        price_own_car10 = 30800000
                        price_own_car11 = 37580000
                        price_own_car12 = 57999999
                        price_own_car13 = 108555000
                        price_own_car14 = 999999999
                        price_own_car15 = 1500000000

                        if id_own.isdigit():
                            if int(id_own) == 1:
                                if own_car == 0:
                                    if price_own_car1 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car1
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Велосипед за ' + str(price_own_car1) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 2:
                                if own_car == 0:
                                    if price_own_car2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Гироскутер за ' + str(price_own_car2) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'

                            elif int(id_own) == 3:
                                if own_car == 0:
                                    if price_own_car3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🏍 Ducati Scrambler за ' + str(price_own_car3) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 4:
                                if own_car == 0:
                                    if price_own_car4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🏍 Honda CTX1300 за ' + str(price_own_car4) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'

                            elif int(id_own) == 5:
                                if own_car == 0:
                                    if price_own_car5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Ferrari California front за ' + str(price_own_car5) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 6:
                                if own_car == 0:
                                    if price_own_car6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Porsche 911 за ' + str(price_own_car6) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 7:
                                if own_car == 0:
                                    if price_own_car7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Nissan GT-R за ' + str(price_own_car7) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 8:
                                if own_car == 0:
                                    if price_own_car8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 BMW X6 за ' + str(price_own_car8) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 9:
                                if own_car == 0:
                                    if price_own_car9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Jaguar F-Type за ' + str(price_own_car9) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 10:
                                if own_car == 0:
                                    if price_own_car10 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car10
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Lamborghini Huracán за ' + str(price_own_car10) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 11:
                                if own_car == 0:
                                    if price_own_car11 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car11
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Lamborghini Gallardo за ' + str(price_own_car11) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 12:
                                if own_car == 0:
                                    if price_own_car12 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car12
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Ferrari F80 Concept за ' + str(price_own_car12) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 13:
                                if own_car == 0:
                                    if price_own_car13 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car13
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Lamborghini Sesto за ' + str(price_own_car13) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 14:
                                if own_car == 0:
                                    if price_own_car14 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car14
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Various Ford-based trucks за ' + str(price_own_car14) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 15:
                                if own_car == 0:
                                    if price_own_car15 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car15
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Tesla Cybertruck за ' + str(price_own_car15) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            else:
                                return ', машины с таким ID не существует! 😔'
                        else:
                            return ', символы и буквы запрещены! 😔'
                    else:
                        return ', для покупки транспорта необходимо дом! 😉'
                elif sourceText.split()[1].lower() in ['яхта', 'яхты']:
                    own_housing = int(get_data['own_housing'])
                    if own_housing >= 1 or own_housing != 30:
                        own_yacht = int(get_data['own_yacht'])
                        price_own_yacht1 = 575000
                        price_own_yacht2 = 1225000
                        price_own_yacht3 = 2500000
                        price_own_yacht4 = 3650000
                        price_own_yacht5 = 8355000
                        price_own_yacht6 = 12850000
                        price_own_yacht7 = 23125000
                        price_own_yacht8 = 34666000
                        price_own_yacht9 = 66225000
                        price_own_yacht10 = 96000000
                        price_own_yacht11 = 126650000
                        price_own_yacht12 = 527777777
                        price_own_yacht13 = 999999999
                        price_own_yacht14 = 1255000000

                        if id_own.isdigit():
                            if int(id_own) == 1:
                                if own_yacht == 0:
                                    if price_own_yacht1 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht1
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 RHIB за ' + str(price_own_yacht1) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            elif int(id_own) == 2:
                                if own_yacht == 0:
                                    if price_own_yacht2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Kawasaki за ' + str(price_own_yacht2) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'

                            elif int(id_own) == 3:
                                if own_yacht == 0:
                                    if price_own_yacht3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Riva Aquarama за ' + str(price_own_yacht3) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            elif int(id_own) == 4:
                                if own_yacht == 0:
                                    if price_own_yacht4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Various за ' + str(price_own_yacht4) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'

                            elif int(id_own) == 5:
                                if own_yacht == 0:
                                    if price_own_yacht5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Рrinсеss 60 за ' + str(price_own_yacht5) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            elif int(id_own) == 6:
                                if own_yacht == 0:
                                    if price_own_yacht6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Аzimut 70 за ' + str(price_own_yacht6) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            elif int(id_own) == 7:
                                if own_yacht == 0:
                                    if price_own_yacht7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Dоminаtоr 40M за ' + str(price_own_yacht7) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            elif int(id_own) == 8:
                                if own_yacht == 0:
                                    if price_own_yacht8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Mооnеn 124 за ' + str(price_own_yacht8) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            elif int(id_own) == 9:
                                if own_yacht == 0:
                                    if price_own_yacht9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Widеr 150 за ' + str(price_own_yacht9) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            elif int(id_own) == 10:
                                if own_yacht == 0:
                                    if price_own_yacht10 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht10
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Palmer Jоhnsоn 42M SuреrSроrt за ' + str(
                                            price_own_yacht10) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            elif int(id_own) == 11:
                                if own_yacht == 0:
                                    if price_own_yacht11 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht11
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Widеr 165 за ' + str(price_own_yacht11) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            elif int(id_own) == 12:
                                if own_yacht == 0:
                                    if price_own_yacht12 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht12
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Есliрsе за ' + str(price_own_yacht12) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            elif int(id_own) == 13:
                                if own_yacht == 0:
                                    if price_own_yacht13 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht13
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Dubаi за ' + str(price_own_yacht13) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            elif int(id_own) == 14:
                                if own_yacht == 0:
                                    if price_own_yacht14 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht14
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Strееts оf Mоnасо за ' + str(price_own_yacht14) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            else:
                                return ', яхты с таким ID не существует! 😔'
                        else:
                            return ', символы и буквы запрещены! 😔'
                    else:
                        return ', для покупки транспорта необходим дом! 😉'
                elif sourceText.split()[1].lower() in ['самолёт', 'самолет', 'самолёты', 'самолеты']:
                    own_housing = int(get_data['own_housing'])
                    if own_housing >= 1 or own_housing != 30:
                        own_air = int(get_data['own_air'])
                        price_own_air1 = 500000
                        price_own_air2 = 3995000
                        price_own_air3 = 6350000
                        price_own_air4 = 15500000
                        price_own_air5 = 17800000
                        price_own_air6 = 22250000
                        price_own_air7 = 43000000
                        price_own_air8 = 65505000
                        price_own_air9 = 75985000
                        price_own_air10 = 86495000
                        price_own_air11 = 109999999
                        price_own_air12 = 313000000
                        price_own_air13 = 617555000
                        price_own_air14 = 850000000
                        price_own_air15 = 2000000000

                        if id_own.isdigit():
                            if int(id_own) == 1:
                                if own_air == 0:
                                    if price_own_air1 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air1
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ de Havilland Canada DHC-2 за ' + str(price_own_air1) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 2:
                                if own_air == 0:
                                    if price_own_air2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ Piper PA-46 за ' + str(price_own_air2) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'

                            elif int(id_own) == 3:
                                if own_air == 0:
                                    if price_own_air3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ Cessna 310 за ' + str(price_own_air3) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 4:
                                if own_air == 0:
                                    if price_own_air4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ Learjet 55 за ' + str(price_own_air4) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'

                            elif int(id_own) == 5:
                                if own_air == 0:
                                    if price_own_air5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ Bombardier Global Express за ' + str(price_own_air5) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 6:
                                if own_air == 0:
                                    if price_own_air6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ Cessna Citation X за ' + str(price_own_air6) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 7:
                                if own_air == 0:
                                    if price_own_air7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ C-130 за ' + str(price_own_air7) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 8:
                                if own_air == 0:
                                    if price_own_air8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ VOLATOL за ' + str(price_own_air8) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 9:
                                if own_air == 0:
                                    if price_own_air9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ RM-10 BOMBUSHKA за ' + str(
                                            price_own_air9) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 10:
                                if own_air == 0:
                                    if price_own_air10 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air10
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ AVENGER — HYV за ' + str(price_own_air10) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 11:
                                if own_air == 0:
                                    if price_own_air11 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air11
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ F-16 Fighting Falcon за ' + str(price_own_air11) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 12:
                                if own_air == 0:
                                    if price_own_air12 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air12
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ RM-10 BOMBUSHKA за ' + str(price_own_air12) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 13:
                                if own_air == 0:
                                    if price_own_air13 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air13
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ TULA — MAMMOTH за ' + str(price_own_air13) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 14:
                                if own_air == 0:
                                    if price_own_air14 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air14
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ V-65 MOLOTOK за ' + str(price_own_air14) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 15:
                                if own_air == 0:
                                    if price_own_air15 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air15
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ MOGUL — MAMMOTH за ' + str(price_own_air15) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            else:
                                return ', самолёта с таким ID не существует! 😔'
                        else:
                            return ', символы и буквы запрещены! 😔'
                    else:
                        return ', для покупки транспорта необходим дом! 😉'
                elif sourceText.split()[1].lower() in ['вертолёт', 'вертолет', 'вертолёты', 'вертолеты']:
                    own_housing = int(get_data['own_housing'])
                    if own_housing >= 1 or own_housing != 30:
                        own_helicopter = int(get_data['own_helicopter'])
                        price_own_helicopter1 = 1300000
                        price_own_helicopter2 = 1750000
                        price_own_helicopter3 = 2225000
                        price_own_helicopter4 = 3500000
                        price_own_helicopter5 = 8850000
                        price_own_helicopter6 = 25555555
                        price_own_helicopter7 = 58000000
                        price_own_helicopter8 = 215000000
                        price_own_helicopter9 = 525000000

                        if id_own.isdigit():
                            if int(id_own) == 1:
                                if own_helicopter == 0:
                                    if price_own_helicopter1 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter1
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚁 Eurocopter EC130/135/14 за ' + str(price_own_helicopter1) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть вертолёт! 😉'
                            elif int(id_own) == 2:
                                if own_helicopter == 0:
                                    if price_own_helicopter2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚁 Boeing MH-6 за ' + str(price_own_helicopter2) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть вертолёт! 😉'

                            elif int(id_own) == 3:
                                if own_helicopter == 0:
                                    if price_own_helicopter3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚁 Sikorsky UH-60 за ' + str(price_own_helicopter3) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть вертолёт! 😉'
                            elif int(id_own) == 4:
                                if own_helicopter == 0:
                                    if price_own_helicopter4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚁 HAVOK — NAGASAKI за ' + str(price_own_helicopter4) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть вертолёт! 😉'

                            elif int(id_own) == 5:
                                if own_helicopter == 0:
                                    if price_own_helicopter5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚁 Eurocopter EC145 за ' + str(price_own_helicopter5) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть вертолёт! 😉'
                            elif int(id_own) == 6:
                                if own_helicopter == 0:
                                    if price_own_helicopter6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚁 Airbus H160 за ' + str(price_own_helicopter6) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть вертолёт! 😉'
                            elif int(id_own) == 7:
                                if own_helicopter == 0:
                                    if price_own_helicopter7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚁 Mil Mi-24 за ' + str(price_own_helicopter7) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть вертолёт! 😉'
                            elif int(id_own) == 8:
                                if own_helicopter == 0:
                                    if price_own_helicopter8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚁 POLICE MAVERICK за ' + str(price_own_helicopter8) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть вертолёт! 😉'
                            elif int(id_own) == 9:
                                if own_helicopter == 0:
                                    if price_own_helicopter9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚁 MAVERICK за ' + str(price_own_helicopter9) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть вертолёт! 😉'
                            else:
                                return ', вертолёта с таким ID не существует! 😔'
                        else:
                            return ', символы и буквы запрещены! 😔'
                    else:
                        return ', для покупки транспорта необходим дом! 😉'
                elif sourceText.split()[1].lower() in ['ферма', 'фермы']:
                    own_farm = int(get_data['own_farm'])
                    own_housing = int(get_data['own_housing'])
                    price_own_farm1 = 500000
                    price_own_farm2 = 5000000
                    price_own_farm3 = 500000000
                    if own_housing >= 1 or own_housing == 30:
                        if id_own.isdigit():
                            if int(id_own) == 1:
                                if own_farm == 0:
                                    if price_own_farm1 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_farm1
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_farm": '{}'.format(id_own)})
                                        get_data.update({"farm_profit": '{}'.format(5)})
                                        get_data.update({"farm_time": '{}'.format(time.time())})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🔋 Miner за ' + str(price_own_farm1) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть ферма! 😉'
                            elif int(id_own) == 2:
                                if own_farm == 0:
                                    if price_own_farm2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_farm2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_farm": '{}'.format(id_own)})
                                        get_data.update({"farm_profit": '{}'.format(50)})
                                        get_data.update({"farm_time": '{}'.format(time.time())})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🔋 Miner S за ' + str(price_own_farm2) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть ферма! 😉'

                            elif int(id_own) == 3:
                                if own_farm == 0:
                                    if price_own_farm3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_farm3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_farm": '{}'.format(id_own)})
                                        get_data.update({"farm_profit": '{}'.format(1000)})
                                        get_data.update({"farm_time": '{}'.format(time.time())})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🔋 Miner X за ' + str(price_own_farm3) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть ферма! 😉'
                            else:
                                return ', фермы с таким ID не существует! 😔'
                        else:
                            return ', символы и буквы запрещены! 😔'
                    else:
                        return ', для покупки фермы необходим дом! 😉'
                elif sourceText.split()[1].lower() in ['комп', 'компьютер', 'ноут', 'ноутбук', 'компы','компьютеры', 'ноуты', 'ноутбуки']:
                    own_comp = int(get_data['own_comp'])
                    price_own_comp1 = 35000000
                    price_own_comp2 = 45000000
                    price_own_comp3 = 150000000

                    if id_own.isdigit():
                        if int(id_own) == 1:
                            if own_comp == 0:
                                if price_own_comp1 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_comp1
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_comp": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 🖥 Book за ' + str(price_own_comp1) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть компьютер! 😉'
                        elif int(id_own) == 2:
                            if own_comp == 0:
                                if price_own_comp2 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_comp2
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_comp": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 🖥 Book Air за ' + str(price_own_comp2) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть компьютер! 😉'

                        elif int(id_own) == 3:
                            if own_comp == 0:
                                if price_own_comp3 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_comp3
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_comp": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 🖥 Book Pro за ' + str(price_own_comp3) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть компьютер! 😉'
                        else:
                            return ', компьютера с таким ID не существует! 😔'
                    else:
                        return ', символы и буквы запрещены! 😔'
                elif sourceText.split()[1].lower() in ['телефон', 'смартфон', 'телефоны', 'смартфоны']:
                    own_smart = int(get_data['own_smart'])
                    price_own_smart1 = 25800000
                    price_own_smart2 = 30000000
                    price_own_smart3 = 35250000

                    if id_own.isdigit():
                        if int(id_own) == 1:
                            if own_smart == 0:
                                if price_own_smart1 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_smart1
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_smart": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 📱 iPhone за ' + str(price_own_smart1) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть смартфон! 😉'
                        elif int(id_own) == 2:
                            if own_smart == 0:
                                if price_own_smart2 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_smart2
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_smart": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 📱 iPhone Pro за ' + str(price_own_smart2) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть смартфон! 😉'

                        elif int(id_own) == 3:
                            if own_smart == 0:
                                if price_own_smart3 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_smart3
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_smart": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 📱 iPhone Pro Max за ' + str(price_own_smart3) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть смартфон! 😉'
                        else:
                            return ', смартфона с таким ID не существует! 😔'
                    elif sourceText.split()[1].lower() in ['телефон', 'смартфон', 'телефоны', 'смартфоны']:
                        own_smart = int(get_data['own_smart'])
                        price_own_smart1 = 800000
                        price_own_smart2 = 1000000
                        price_own_smart3 = 1250000

                        if id_own.isdigit():
                            if int(id_own) == 1:
                                if own_smart == 0:
                                    if price_own_smart1 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_smart1
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_smart": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 📱 iPhone за ' + str(
                                            price_own_smart1) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть смартфон! 😉'
                            elif int(id_own) == 2:
                                if own_smart == 0:
                                    if price_own_smart2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_smart2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_smart": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 📱 iPhone Pro за ' + str(
                                            price_own_smart2) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть смартфон! 😉'

                            elif int(id_own) == 3:
                                if own_smart == 0:
                                    if price_own_smart3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_smart3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_smart": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 📱 iPhone Pro Max за ' + str(
                                            price_own_smart3) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть смартфон! 😉'
                            else:
                                return ', смартфона с таким ID не существует! 😔'
                    else:
                        return ', символы и буквы запрещены! 😔'
                else:
                    return ', такой категории не существует! 😔'
            else:
                return shopHelp
        else:
            return None
    pass