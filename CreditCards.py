import pickle
from functools import reduce
from random import randint

dictionary= dict()


class CreateCards:
    def __init__(self, cards):
        self.__typeCards = cards

    @property
    def stype_cards(self):
        return self.__typeCards

    def create_cards(self):
        i = 0
        sfd=tuple()
        if self.__typeCards == 1:
            sfd = (4, 0, 0, 0, 0, 0)
        if self.__typeCards == 2:
            sfd = (3, 4, 0, 0, 0, 0)
        if self.__typeCards == 3:
            sfd = (5, 1, 0, 0, 0, 0)
        sdf2 = list()
        while i < 9:
            sdf2.append(randint(0, 9))
            i += 1
#        print(sdf2)
        for f in range(len(sdf2)):
            if f % 2 == 0:
                if sdf2[f] * 2 > 9:
                    sdf2[f] = (randint(0, 9))

        sfd += tuple(sdf2)
#        print(sum(sfd))
#        print(sfd)
        if sum(sfd) % 10 == 0:
            sdf2.clear()
            sdf2.append(0)
            sfd += tuple(sdf2)
        else:
            sdf2.clear()
            sdf2.append((10 - sum(sfd) % 10))
            sfd += tuple(sdf2)
#        print(sfd)
#        print(sum(sfd))
        number_of_cards = reduce(lambda x, y: x * 10 + y, sfd)
        print("Ваш номер карты: ",number_of_cards)
        return number_of_cards

    def create_vin(self):
        sdf2 = list()
        i=0
        while i<4:
            sdf2.append(randint(0, 9))
            i+=1
        vin_of_cards = reduce(lambda x, y: x * 10 + y, sdf2)
        print("Ваш пинкод: ", vin_of_cards)
        return vin_of_cards

    pass;



while True:
    print(" Оформить новую карту банка-->1\n Войти в свой аккаунт-->2\n Выход-->3")
    menu = int(float(input("ваш выбор-->")))
    if menu ==1:
        print("Меню\nВыберите формат карты которой хотите выпустить:\nVisa--=> 1\nAmerican Express--=> 2\nMastercard--=> 3")
        try:
            TypeCards = int(float(input("ваш выбор-->")))
            if TypeCards == 0:
                with open('data.pickle', 'rb') as f:
                    dictionary = pickle.load(f)
                    print("SAVE@$#")
                    print(dictionary)
                    print("Save@!")
            elif TypeCards < 1 or TypeCards > 3:
                print("Введено некорректное данные. Повторитте ввод:")
                TypeCards = int(float(input("ваш выбор-->")))
            elif TypeCards == 1 or TypeCards == 2 or TypeCards == 3:
                dictionary[CreateCards(TypeCards).create_cards()] = CreateCards(TypeCards).create_vin()
                print(dictionary)
            with open('data.pickle', 'wb') as f:
                pickle.dump(dictionary, f)
        except ValueError:
            print("Повторрите ввод введен неверный формат.")
    elif menu ==2:
        namber_of_cards = int(float(input("Введите номер карты:")))
        vin_cards = int(float(input("Введите VIN код карты:")))
        for key, value in dictionary.items():
            if namber_of_cards==key:
                if vin_cards==value:
                    print("Успех")
                else:print("Incorrect")
            else:print("Incorrect")


