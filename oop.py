import re # Для 3 задания

class Person:
    """
    Задание 1

    Класс Person имеет атрибуты объекта: __first_name, __last_name,
    __age.
    
    Необходимо:
        добавить конструктор класса, который принимает три аргумента.

        добавить свойства атрибутов (только геттеры)

        добавить метод is_major, который возвращает True, если человек
        совершеннолетний (больше или равно 18 лет) иначе False

    >>> p = Person('First', 'Last', 43)
    >>> print(p.first_name)
    First
    >>> print(p.last_name)
    Last
    >>> print(p.age)
    43
    >>> p.first_name = "Test"
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> p.last_name = "Test"
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> p.age = 43
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> p.is_major()
    True
    >>> p = Person('First', 'Last', 18)
    >>> p.is_major()
    True
    >>> p = Person('First', 'Last', 17)
    >>> p.is_major()
    False
    """

    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def age(self):
        return self.__age

    def is_major(self):
        if self.age >= 18:
            return True
        else:
            return False
    pass


class Address:
    """
    Задание 2

    Реализуйте класс Address, который должен иметь атрибуты объекта: __street,
    __state, __country, __zipcode.

    Необходимо:
        добавить конструктор с необходимыми параметрами

        добавить свойства street, state, country и zipcode (только геттеры)

        написать метод is_valid_zipcode, который возвращает True если __zipcode
        содержить 5 цифр

        написать метод get_full_address, который возвращает строку содержащую
        улицу, область, страну и почтовый индекс. Каждое значение выводится с новой
        строки
    
    >>> address = Address('Javornitskogo, 101', 'Dnepropetrovskaja', 'Ukraine', 49000)
    >>> address.street
    'Javornitskogo, 101'
    >>> address.state
    'Dnepropetrovskaja'
    >>> address.country
    'Ukraine'
    >>> address.zipcode
    49000
    >>> address.street = 'Lazarana'
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> address.state = 'Hmelnitskaja'
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> address.country = 'USA'
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> address.zipcode = '12345'
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute
    >>> address.is_valid_zipcode()
    True
    >>> print(address.get_full_address())
    Javornitskogo, 101
    Dnepropetrovskaja
    Ukraine
    49000
    """
    def __init__(self, street, state, country, zipcode):
        self.__street = street
        self.__state = state
        self.__country = country
        self.__zipcode = zipcode

    @property
    def street(self):
        return self.__street

    @property
    def state(self):
        return self.__state

    @property
    def country(self):
        return self.__country

    @property
    def zipcode(self):
        return self.__zipcode

    def is_valid_zipcode(self):
        if len(str(self.__zipcode)) == 5:
            return True
        else:
            return False

    def get_full_address(self):
        return "{}\n{}\n{}\n{}".format(self.__street, self.__state, self.__country, self.__zipcode)
    pass

class ContactInfo(object):
    """
    Задание 3

    Реализуйте класс ContactInfo, который должен
    содержать два свойства: email и phone (геттеры и сеттеры).

    Добавить конструктор с параметрами, а также деструктор, в
    котором выводиться сообщение Bye.

    Реализовать метод is_valid_email возвращающий True, если
    введенный email правильный, и is_valid_phone возвращающий
    True, если введенный тоже записан в правильном формате, т.е.
         +3 8 (ццц) ццц-цц-цц

    >>> ci = ContactInfo('mail@mail.com', '+38 (050) 123-45-56')
    >>> ci.email
    'mail@mail.com'
    >>> ci.phone
    '+38 (050) 123-45-56'
    >>> ci.is_valid_email()
    True
    >>> ci.is_valid_phone()
    True
    >>> ci.email = "test"
    >>> ci.email
    'test'
    >>> ci.is_valid_email()
    False
    >>> ci.phone = "#12"
    >>> ci.phone
    '#12'
    >>> ci.is_valid_phone()
    False
    """
    def __init__(self, email, phone):
        self.__email = email
        self.__phone = phone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    def __del__(self):
        print('Bye')

    def is_valid_email(self):
        pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        email_re = re.compile(pattern)
        if email_re.findall(self.email):
            return True
        else:
            return False


    def is_valid_phone(self):
        regex = r"(?:|\+|\d)[\d\-\(\) ]{7,}\d"
        return bool(re.search(regex, self.__phone))
    pass


def main():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    main()


