"""
Данная функция перебирает элементы в строке, проверя каждый символ на то, является ли символ числом
Если элемент является числом, то он попадает в список digits, где хранятся все числа из строки
В конце функция возвращает длинну списка digits
"""
def count_digits(line):
    digits = []

    if type(line) != str:
        raise TypeError('Полученная строка: {}'.format(type(line)))

    for element in line.lower():
        if str(element).isdigit():
            digits.appent(element)

            return len(digits)

if __name__ == '__main__':
    input_line = input('Введите предложение: ')
    print(count_digits(input_line))

