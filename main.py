"""

Цель: Созд-ть программу по расчету экономических формул
Дополнительно: Программа должна быть максимально простой и удобной

"""
import time

"""
Функция рентаельности активов (ROA)

Показатель ROA рассчитывают, что бы понять, насколько эффективно используются активы компании
здания, оборудования, сырье, деньги - и какую в итоге они приносят прибыль.
Если рентабельность активов ниже нуля, значит, предприятия работает в убыток. Чем выше ROA,
тем эффективнее орг-ия использует ресурсы.
"""


def profitability_roa():
    print("Описание: Показатель ROA рассчитывают, что бы понять,\n"
          "насколько эффективно используются активы компании\n"
          "здания, оборудования, сырье, деньги - и какую в итоге они приносят прибыль.\n"
          "Если рентабельность активов ниже нуля, значит, предприятия работает в убыток. Чем выше ROA,\n"
          "тем эффективнее орг-ия использует ресурсы.")
    passed = input()
    print("Формула: ROA = П/ЦА * 100%\n"
          "П - прибыль за период работы\n"
          "ЦА - средняя цена активов, которые находились на балансе в это же время")
    passed = input()
    form_one = int(input("У Вас есть параметр \"П\"?\n1.Да\n2.Нет"))
    if form_one == 1:
        print("Давайте рассчетаем ее...")
        time.sleep(2)
        




def menu():
    manager = int(input("Выбор формулы:\n1. Рентабельность активов(ROA)\n"))
    if manager == 1:
        profitability_roa()


#Запуск
print('\"Экономические формулы\" - рассчет и обучение')

time.sleep(2)

menu()