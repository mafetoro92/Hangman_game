from words import select_word
from hagman_game import hagman_code


def main():
    pick_word = select_word()
    hagman_code(pick_word)


if __name__ == '__main__':
    main()
