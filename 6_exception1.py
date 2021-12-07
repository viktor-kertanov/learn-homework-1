"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    while True:
        try:
            user_input = input("Как дела?\n").lower().strip()
            if user_input == "хорошо":
                print("Ну, наконец-то! Я уж думал у тебя никогда не хорошо.")
                break
        except:
            print("\nПока-пока")
            break
    
if __name__ == "__main__":
    hello_user()
