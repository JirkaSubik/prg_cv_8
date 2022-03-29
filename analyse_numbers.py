
def is_whole_number(number):
    if number % 1 == 0 and number > 0:
        return True

    return False


whole_number = is_whole_number(8)
print(whole_number)

def is_even_number(number):
    if number % 2 == 0:
        return True
    return False


even_number = is_even_number(whole_number)
print(even_number)