import threading
import time

def f(x):
    if x % 2 == 0:
        return 1
    elif x == 111:
        return 0
    else:
        while True:
            time.sleep(10)

def g(x):
    if x > 0 and x < 100:
        return 1
    elif x > 100 and x < 200:
        return 0
    else:
        while True:
            time.sleep(10)

def check_progress(f_thread, g_thread):
    flag = False
    wait_time = 10
    while True:
        if flag == False:
            time.sleep(wait_time)
            if f_thread.is_alive():
                if g_thread.is_alive():
                    choice = input("Обчислення f та g ще тривають. Продовжити? (1 - продовжити обчислення, 2 - припинити, 3 - продовжити без питань): ")
                else:
                    choice = input("Обчислення f ще триває. Продовжити? (1 - продовжити обчислення, 2 - припинити, 3 - продовжити без питань): ")
            else:
                if g_thread.is_alive():
                    choice = input("Обчислення g ще триває. Продовжити? (1 - продовжити обчислення, 2 - припинити, 3 - продовжити без питань): ")
                else:
                # Якщо обидва потоки завершилися, вийти з циклу
                    break
            if choice == '2':
            # Припинити обчислення
                break
            elif choice == '3':
                flag = True

def main():
    x = int(input("Введіть значення x: "))

    f_thread = threading.Thread(target=f, args=(x,))
    g_thread = threading.Thread(target=g, args=(x,))

    f_thread.start()
    g_thread.start()

    check_progress(f_thread, g_thread)

    if not f_thread.is_alive() and not g_thread.is_alive():
        result = f(x) or g(x)
        print("Результат f(x) || g(x):", result)

if __name__ == "__main__":
    main()
