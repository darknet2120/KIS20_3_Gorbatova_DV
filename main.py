def count_digits(line):
    digits = []

    if type(line) != str:
        raise TypeError('Полученная строка: {}'.format(type(line)))

    for element in line.lower():
        if str(element).isdigit():
            digits.appent(element)

            return len(digits)