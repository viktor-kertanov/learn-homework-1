"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
from config import load
import random
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    print("Вызван /start")
    replies = [
        "Hello!",
        "Привет!",
        "Что делаешь?",
        "Йоу Пайтон реплай"
    ]
    random_int = random.randint(0,len(replies)-1)
    final_reply = replies[random_int]

    update.message.reply_text(final_reply)



def planets(update, context):
    """
    Команда /planets показывает список доступных в ephem планет
    """
    print("Выводим имеющиеся планеты")
    astro_bodies = ephem._libastro.builtin_planets()
    planets = [body[2] for body in astro_bodies if body[1] == 'Planet']
    planets_reply = "\n".join(planets)
    update.message.reply_text(planets_reply)


def constellation(update, context):
    print("Ищем созвездие планеты")
    planets_input = context.args
    planets_input = [p.lower().strip() for p in planets_input]
    print(planets_input)
    astro_bodies = ephem._libastro.builtin_planets()
    planets = [body[2].lower() for body in astro_bodies if body[1] == 'Planet']
    print(planets)
    for planet in planets_input:
        print(planet)
        if planet in planets:
            planet = planet.capitalize()
            print(f"The planet is: {planet}")
            planet_object = getattr(ephem, planet)()
            planet_object.compute(epoch=ephem.now())
            constellation = ephem.constellation(planet_object)[1]
            print(constellation)
            const_reply = f"{planet} is in {constellation}.\n"
            print(const_reply)
            update.message.reply_text(const_reply)
        else:
            const_reply = f"\n{planet} is not in the list of planets. Call /planets to see the list."
            update.message.reply_text(const_reply)

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    config = load()
    mybot = Updater(config.api_token, request_kwargs=PROXY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planets", planets))
    dp.add_handler(CommandHandler("constellation", constellation, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
