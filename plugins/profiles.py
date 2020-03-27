import os
from plugins import gf

users_dir = os.path.join(r"users/")

def profiles(sourceText, id):
    get_data = gf.loadjson(users_dir + str(id) + ".json")

    own_housing = int(get_data['own_housing'])
    own_car = int(get_data['own_car'])
    own_yacht = int(get_data['own_yacht'])
    own_air = int(get_data['own_air'])
    own_helicopter = int(get_data['own_helicopter'])
    own_comp = int(get_data['own_comp'])
    own_smart = int(get_data['own_smart'])
    own_farm = int(get_data['own_farm'])

    profile = ', ваш профиль:\n\n⭐ Основное:\n⠀⠀👤 ' + '@id{}'.format(id) + '(' + str(get_data['first_name']) + ' ' + str(get_data['last_name']) + ')'  + '\n⠀⠀🔎 ID: ' + str(get_data['id']) + '\n⠀⠀' + str(gf.check_group(id)) +  '\n⠀⠀💰 В кошельке: ' + str(get_data['balance']) + '€\n⠀⠀🎮 Ник: ' + str(gf.check_nick(id)) + str(gf.check_own_profile(id)) + str(gf.check_own_housing(own_housing)) + str(gf.check_own_car(own_car)) + str(gf.check_own_yacht(own_yacht)) + str(gf.check_own_air(own_air)) + str(gf.check_own_helicopter(own_helicopter)) + str(gf.check_own_comp(own_comp)) + str(gf.check_own_smart(own_smart)) + str(gf.check_own_farm(own_farm)) + '\n\n Дата Регистрации: ' + str(get_data['data_reg'])
    if sourceText.split()[0].lower() in ['профиль', '📒']:
        return profile
    else:
        return None