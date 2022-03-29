
def is_whole_number(number):
    if number % 1 == 0:
        return True

    return False

whole_number = is_whole_number(8)
print(whole_number)