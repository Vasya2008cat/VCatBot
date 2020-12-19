import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard  
key = "5cddcaf177c0066bd35aeacb30fcaa1267dc552ff93c7998b4c62d93384899b9b5617af950e73ad18dfa6"
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=key)

def send_message(user_id, message, keyboard = None):  
                from random import randint
                vk.method('messages.send',
                          {'user_id': user_id,
                           "random_id":randint(1,1000) ,
                           'message': message,
                           'keyboard':keyboard.get_keyboard() if keyboard else None,}  
                          )

start_keyboard = VkKeyboard(one_time = True)  
start_keyboard.add_button('START')
start_keyboard.add_line()
start_keyboard.add_button('NOT START')

main_keyboard = VkKeyboard(one_time = True)  
main_keyboard.add_button('Об авторе')
main_keyboard.add_button('Сделать пожертвование')
main_keyboard.add_line()
main_keyboard.add_button('Сыграть в игру')

main_keyboard.add_button('узнать погоду')

back_keyboard = VkKeyboard(one_time = True)
back_keyboard.add_button('Назад')


game_over_keyboard = VkKeyboard(one_time = True)    #<1=====
game_over_keyboard.add_button('Выйти')
game_over_keyboard.add_line()
game_over_keyboard.add_button('Продолжить(просто введи число)')

food_button_keyb = VkKeyboard(one_time = True)
food_button_keyb.add_button('author fav food')
food_button_keyb.add_line()
food_button_keyb.add_button('назад')

doNut_keyb = VkKeyboard(one_time = True)
doNut_button_keyb.add_button('купить нам шаурму')
doNut_button_keyb.add_line()
doNut_button_keyb.add_button('помолиться за нас')
doNut_button_keyb.add_line()
doNut_button_keyb.add_button('сказать спасибо')
doNut_button_keyb.add_line()
doNut_button_keyb.add_button('назад')


gamers={}
# Работа с сообщениями
longpoll = VkLongPoll(vk)
# Основной цикл
for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
            text = event.text.lower()
            user_id = event.user_id
            print(text)
            if user_id in gamers:
                
                try:
                    otvet = int(text)
                except:
                    if text == 'выйти':
                        del gamers[user_id]
                        send_message(user_id,"ну ладно :с",main_keyboard)    #<1=====
                    else:
                        send_message(user_id,"те чо игра надоела?",game_over_keyboard)
                    
                    continue
                if otvet > gamers[user_id]:
                    send_message(user_id,"mnoga")
                elif otvet < gamers[user_id]:
                    send_message(user_id,"malo")
                else:
                    send_message(user_id,"Победил", main_keyboard)
                    del gamers[user_id]
            else:
                if text == 'START'.lower():   
                    send_message(user_id,"Добро пожаловать",main_keyboard)  
                    
                elif text == 'Об авторе'.lower():   
                    send_message(user_id,"Damir & Vasya2008play",food_button_keyb)
                elif text == 'Сделать пожертвование'.lower():     #payment!
                    send_message(user_id,"Выберете тип пожертвование:",back_keyboard)
                elif text == 'Сыграть в игру'.lower():
                    from random import randint
                    gamers[user_id] = randint(1,9000)
                    send_message(user_id,"угадывай")
                elif text == 'author fav food':
                    send_message(user_id,"Шаурма",back_keyboard)
                elif text == 'купить нам шаурму':
                    send_message(user_id,"По мнению автора, шаурму лучше покупать в KFC, но можно купить где хотите",back_keyboard)
                elif text == 'помолиться за нас':
                    send_message(user_id,"🕯🕯🕯📋🕯🕯🕯",back_keyboard)
                elif text == 'сказать спасибо':
                    send_message(user_id,"",back_keyboard)
                elif text == 'назад':
                    send_message(user_id, "Продолжайте",back_keyboard)
                elif text == 'узнать погоду'.lower():   
                    send_message(user_id,"ясно",back_keyboard)
                else:
                    send_message(user_id,"Продолжайте",main_keyboard)

