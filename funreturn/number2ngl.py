def number_in_english(number):
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
             'nineteen']
    tens = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    result = ''
    if number == 0:
        return 'zero'
    if number // 100 > 0:
        result += ones[number // 100] + ' hundred and '
    if number % 100 > 0:
        if number % 100 < 10:
            return result + ones[number % 10]
        if number % 100 < 20:
            return result + teens[number % 100 - 10]
        if number % 10 == 0:
            return result + tens[number % 100 // 10 - 2]
        return result + tens[number % 100 // 10 - 2] + ' ' + ones[number % 10]
    return result[:-5]


