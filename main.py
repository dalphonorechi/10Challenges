import math


# 1. Degrees to radians


def radians_to_degrees(num):
    d = 180 / math.pi
    return num * d

radians = 13
print(f'{radians} radians in degrees {radians_to_degrees(radians)}')


# 2. sort a list using asc, desc ,none


def sort_list(sort, how):
    if how == "none":
        return sort
    elif how == 'asc':
        sort.sort()
        return sort
    elif how == 'desc':
        sort.sort(reverse=True)
        return sort

ll = [2, 5, 3, 5]
typ = "desc"
print(f'{ll}, sorted criteria  = \'{typ}\' is {sort_list(ll, typ)}')


# 3.decimal to binary


def decimal_to_binary(num):

    binary_numbers = []
    binary = ''
    while num > 0:
        k = num / 2
        if num % 2 == 0:
            binary_numbers.insert(0, 0)
        elif num == 1:
            binary_numbers.insert(0, 1)
            break
        else:
            binary_numbers.insert(0, 1)
        num = math.floor(k)
    for i in binary_numbers:
        binary += str(i)

    return binary


decimal = 294
print(f'Binary of {decimal} is {decimal_to_binary(decimal)}')


# 4.count vowels in a string

def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']

    count = 0
    for v in vowels:
        c = string.lower().count(v)
        count += c
    return count


string = "a e i o u A E I O U"
print(f'The string \'{string}\' has {count_vowels(string)} vowels.')


# 5.Calculate

def calculate(num1, num2, sign):
    expression = f'{num1}{sign}{num2}'
    return eval(expression)


num1 = 1234
num2 = 100
sign = "-"

print(f'The operands are {num1} and {num2}, the operation is \'{sign}\' and result is {calculate(num1, num2, sign)}')


# 6.Discount


def count(total, percentage):
    d = (percentage / 100) * total
    discount = total - d
    return discount


total = 250.75
pct = 12
print(f'The amount to pay for ${total} of after {pct}% discount is ${count(total, pct)}.')


# 7. Are the Xs equal to the Os?
def count_x_o(string):
    vowels = ['o', 'x']
    x_count = 0
    o_count = 0
    for v in vowels:
        if v == "x":
            c = string.lower().count(v)
            x_count += c
        else:
            c = string.lower().count(v)
            o_count += c
    return {"X": x_count, "O": o_count, "Ratio of X And O is Equal": o_count == x_count}


print(count_x_o("xodvkyugsdkvbnvkjxoxox"))


# 8. Hide the credit card number


def censor_card(string):
    b = [i for i in string]
    c = ""
    for i in range(0, len(string) - 4):
        b[i] = "X"

    for i in b:
        c += i

    return c


card_n = "4444444444444444"
print(f'The censored card number is {censor_card(card_n)}')


# 9.Just Number


def just_number(string):
    f = []
    for i in string:
        try:
            k = int(i)
            f.append(k)
        except ValueError:
            pass

    return f


string_extract = "ge55678978gfvhsdfhg87r87y777"
print(f'The numbers from \'{string_extract}\' is {just_number(string_extract)}')


# 10. Repeat the characters


def repeat(string):
    s = ''
    for i in string:
        s += i * 2

    return s


ss = "What are you up to today ?"
print(f'The repeated word \'{ss}\' is {repeat(ss)}')
