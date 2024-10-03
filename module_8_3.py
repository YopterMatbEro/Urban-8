class Car:
    def __init__(self, model: str, vin_number: int, numbers: str):
        check_vin = self.__is_valid_vin(vin_number)
        if check_vin:
            self.__vin = vin_number
        check_numbers = self.__is_valid_numbers(numbers)
        if check_numbers:
            self.__numbers = numbers
        self.model = model

    def __is_valid_vin(self, vin_number) -> bool:
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип данных для vin номера')
        elif vin_number not in range(1000000, 10000000):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self, numbers) -> bool:
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номера')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


if __name__ == '__main__':
    try:
        first = Car('Model1', 1000000, 'f123dj')  # успешный вариант
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')  # неверный диапазон vin номера
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')  # некорректная длина номера
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')

    try:
        fourth = Car('Model1', '1000000', 'f123dj')  # вместо номера строка
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{fourth.model} успешно создан')


    try:
        fifth = Car('Model1', 1000000, ('f123dj',))  # вместо номеров кортеж
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{fifth.model} успешно создан')
