def clean_list(my_list):

    clean_list = []

    for element in my_list:
        clean_element = element.strip()
        clean_list.append(clean_element)

    return clean_list