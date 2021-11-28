def beautiful_numbers(number):
    """ добавляет пробел между разрядами в больших числах """
    num = []
    while len(str(number)) > 3:
        numb = str(number % 1000)
        while len(numb) < 3:
            numb = '0' + numb
        num.insert(0, numb)
        number //= 1000
    else:
        num.insert(0, str(number))
        number = ' '.join(num)
    return number


if __name__ == '__main__':
    print(beautiful_numbers(12), type(beautiful_numbers(12)))
    print(beautiful_numbers(12005), type(beautiful_numbers(12005)))
    print(beautiful_numbers(1234567089), type(beautiful_numbers(1234567089)))
