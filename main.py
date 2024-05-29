print("Добро пожаловать на игру 'Superbrain' ")
n = input("Введите ваше имя: ")
print(f"Приятно познакомиться {n}")

while True:
    l = input("Хотите начать игру? Выберите да/нет: ")
    if l == 'да':
        print("Мы начинаем! ")
        break
    elif l == 'нет':
        print("Игра окончина! ")
        exit()
    else:
        print("Ошибка, введите только да/нет")



def quiz(p):
    p = p.replace(" ","")
    return p == p[::-1]
word = "топот"
pol = quiz(word)
while True:
    m = input(f"Вопрос 1) Слово '{word}' является ли палиндромом? да/нет: ")
    if (pol and m == 'да') or (not pol and m == 'нет'):
     print("Правильно!!! ")
     break
    else:
        print("Неверно, подумай еще! ")





def quizz(p):
    p = str(p)
    return p == p[::-1]
num = 123321
lol = quizz(num)
while True:
    n = input(f"Вопрос 2) Число '{num}' является ли палиндромом? да/нет: ")
    if (lol and n == 'да') or (not lol and n == 'нет'):
     print("Правильно!!! ")
     break
    else:
        print("Неверно, подумай еще! ")





def quizzz(q):
    q = q.replace(" ","")
    return q == q[::-1]
wordd = "заказать"
kol = quizzz(wordd)
while True:
    b = input(f"Вопрос 1) Слово '{wordd}' является ли палиндромом? да/нет: ")
    if (kol and b == 'да') or (not kol and b == 'нет'):
     print("Правильно!!! ")
     break
    else:
        print("Неверно, подумай еще! ")


print("Поздравляю вы прошли игру, удачи! ")