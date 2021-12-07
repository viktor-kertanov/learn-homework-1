import random

"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую

"""

questions_and_answers = {
    "Как дела?": ["Гладил крокодила", "Мимо проходила", "Зуб раздрообила", "Кошку побила", "Как сажа бела"],
    "Что делаешь?": ["Бельё развешиваешь", "Себя забыл спросить", "Чай иду пить", "Ещё кофе пью", "Люля кебаб"],
    "Программируешь?": ["Программирую", "Ленюсь", "Думаю пока"],
    "Устал?": ["Да", "А что?", "Нет"]
}


def ask_user(answers_dict):
    answers_dict = {k.lower().strip(): v for k, v in answers_dict.items()}
    proposition = ["Можешь спросить у меня",
                   "Мог бы поинтересоваться",
                   "Узнай у меня",
                   "Выведай у меня",
                   "Хочешь ответ на вопрос"]
    while True:
        user_question = input(f"\n{'-'*25}\nВведи пожалуйста свой вопрос. Если ни одного вопроса не приходит в голову,"
                              "нажми цифру 1, и я подскажу.\nНажми 0, чтобы остановить программу.\n"
                              f"{'-'*25}\n").strip().lower()
        if user_question == '1':
            for q in answers_dict:
                print(f"{random.choice(proposition)}: '{q.capitalize()}'")
        elif user_question == '0':
            print(f"С вами приятно иметь дело! До свидания!")
            break
        elif user_question in answers_dict:
            possible_replies =  answers_dict[user_question]
            random_answer = random.choice(possible_replies)
            print(f"\n{random_answer}")
        else:
            print("Мне нечего тебе сказать -- задай другой вопрос или проси подсказки!")

if __name__ == "__main__":
    try:
        ask_user(questions_and_answers)
    except KeyboardInterrupt:
        print("\nВы не хотите со мной общаться -- я с вами тоже.")
