def count_digits(line):
    digits = []
    for element in line.ower():
        if str(element).isdigit():
            digits.append(element)
            return len(digits)