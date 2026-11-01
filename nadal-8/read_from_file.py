import random

from utils import clean_list


def read_data(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        data = f.readlines()
        clean_data = clean_list(data)

        random_item = random.choice(clean_data)
        return random_item