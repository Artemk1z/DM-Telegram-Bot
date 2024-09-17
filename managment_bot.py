import subprocess
import os
import signal

bot_process = None

def start_bot():
    global bot_process
    if bot_process is None:
        bot_process = subprocess.Popen(['python', 'bot.py'])
        print("Бот запущен.")
    else:
        print("Бот уже работает.")

def stop_bot():
    global bot_process
    if bot_process:
        os.kill(bot_process.pid, signal.SIGTERM)
        bot_process = None
        print("Бот остановлен.")
    else:
        print("Бот не запущен.")

def restart_bot():
    stop_bot()
    start_bot()

def menu():
    while True:
        print("\n1. Запустить бота\n2. Остановить бота\n3. Перезапустить бота\n4. Выйти")
        choice = input("Выберите действие: ")
        
        if choice == '1':
            start_bot()
        elif choice == '2':
            stop_bot()
        elif choice == '3':
            restart_bot()
        elif choice == '4':
            stop_bot()
            print("Выход...")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == '__main__':
    menu()
