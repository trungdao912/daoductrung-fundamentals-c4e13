def get_even_list(number_list):
    even_list = []
    for number in number_list:
        if number % 2 == 0:
            even_list.append(number)
        else:
            continue
    return even_list

