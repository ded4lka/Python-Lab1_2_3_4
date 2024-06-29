# Функция конвертации числа в слова
def ConvertNumberToWords(number):
    
    # Списки возможных слов
    units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']                # Цифры
    teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', \
             'sixteen', 'seventeen', 'eighteen', 'nineteen']                                            # 11-19
    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']    # Десятки
    thousands = ['', 'thousand', 'million', 'billion', 'trillion']                                      # Тысячи

    # Функция конвертации группы в слова
    def ConvertGroup(num):
        if num == 0:    # Если число равно нулю
            return ''   # Возвращаем пустую строку
        elif num < 10:          # Если число меньше 10
            return units[num]   # Возвращаем соответствующее слово из списка цифр
        elif num == 10:     # Если число равно 10
            return tens[1]  # Возвращаем конкретное слово
        elif num < 20:              # Если число меньше 20
            return teens[num - 10]  # Возвращаем соответствующее слово из списка чисел 11-19
        elif num < 100:                                     # Если число меньше 100
            return tens[num // 10] + ' ' + units[num % 10]  # Возвращаем комбинацию слов из массива десятков и цифр
        else:                                                                   
            return units[num // 100] + ' hundred ' + ConvertGroup(num % 100)    # Возвращаем кол-во тысяч

    # Разбиваем число на группы по три цифры
    groups = []                         # Список групп
    while number:                       # Пока число не кончилось
        groups.append(number % 1000)    # Добавляем очередную тройку в список групп
        number //= 1000                 # Отсекаем Записанную часть

    # Конвертируем каждую группу и объединяем вместе
    if not groups:          # Если список групп пуст
        return 'zero'       # Возвращаем ноль
    words = ''              # Будущее предложение
    for i, group in enumerate(groups):                                      # Итерируемся по группам и их инедксу
        if group != 0:
            words = ConvertGroup(group) + ' ' + thousands[i] + ' ' + words  # Конвертируем группу, добавляем тысячи и предыдущее
    return words


# Пример использования
number = int(input("Введите целое число: ").replace(' ', ''))   # Вводим число и убираем лишние пробелы
print("Полученная строка: " + ConvertNumberToWords(number))