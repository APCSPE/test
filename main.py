import random
from os import system, name


def pick_secret_word():
    words = []
    f = open("Words", "r")
    for w in f:
        words.append(w.rstrip())
    r = random.randint(0, len(words) - 1)
    f.close()
    random_word = words[r]
    return random_word.upper()


def create_secret_word_list(word):
    word_letters = []
    for letter in word:
        word_letters.append(letter)
    return word_letters


def create_guessed_letter_list(secret_list):
    blank_list = []
    for letter in secret_list:
        letter = "__"
        blank_list.append(letter)
    return blank_list


def print_guess_list(guessed_letter_list):
    for letter in guessed_letter_list:
        print(letter, end=" ")
    print()
    return 0


def check_letter(secret_list, letter):
    true = 0
    for i in range(len(secret_list)):
        if letter == secret_list[i]:
            true = true + 1
    if true >= 1:
        return True
    else:
        return False


def update_guessed_letters(secret_list, guessed_letters, letter):
    i = 0
    while i in range(len(secret_list)):
        if letter == secret_list[i] and letter != guessed_letters[i]:
            guessed_letters.pop(i)
            guessed_letters.insert(i, letter)
        i = i + 1
    return guessed_letters


def is_word_guessed(guessed_letters):
    not_guessed = 0
    for letter in guessed_letters:
        if letter == "__":
            not_guessed = not_guessed + 1
    if not_guessed >= 1:
        return False
    else:
        return True


def main():
    win = False
    wrong_guess = []
    num_guesses = 6

    w = pick_secret_word()
    print("Secret word is " + w)
    unkwon_word = create_secret_word_list(w)
    hint_list = create_guessed_letter_list(w)

    while num_guesses > -1 and not win:
        print("----------------------------------")
        print("Guess the word:", end=" ")
        blank = print_guess_list(hint_list)
        print()
        print("wrong guesses:", wrong_guess)
        print()
        print("You have", num_guesses, " guesses remaining")
        print()
        user_letter = input("pick a letter: ")
        user_letter = user_letter.upper()
        check_user_1 = check_letter(unkwon_word, user_letter)
        check_user_2 = str(check_user_1)
        # is_user_done = is_word_guessed(hint_list)

        if check_user_2 == "True":
            hint_list = update_guessed_letters(unkwon_word, hint_list, user_letter)
            num_guesses = num_guesses
            print("You guessed correctly!")
            print("Guess the word:")
            blank = print_guess_list(hint_list)
            num_guesses = num_guesses
            is_user_done = is_word_guessed(hint_list)
            if is_user_done:
                win = True
                print("You guessed entire word!")
                break
            print("----------------------------------")
            print()
            continue


        elif check_user_2 == "False":
            print(user_letter, "is not in the word.")
            print("Guess the word:", end=" ")
            blank = print_guess_list(hint_list)
            print("----------------------------------")
            print()
            if user_letter not in wrong_guess:
                wrong_guess.append(user_letter)
                num_guesses = num_guesses - 1
                if num_guesses == 0:
                    print("You have 0 guesses remaining!")
                    print("The secret word is", end=" ")
                    end_word = print_guess_list(unkwon_word)
                    break
            continue

        return win  # your main() function should return a True or False depending on


## to test your program, call the main() function 
# main()

test = main()


# DO NOT DELETE OR EDIT THE CODE BELOW... FOR TESTING 
def test_answer(monkeypatch):
    inputs = iter(['T', 'E', 'S'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = main()
    assert result == True


def test_answer_2(monkeypatch):
    inputs = iter(['T', 'E', 'X', 'F', 'Z', 'B', 'Q', 'M'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = main()
    assert result == False


def test_answer_3(monkeypatch):
    inputs = iter(['X', 'X', 'Z', 'B', 'Q', 'M', 'I'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = main()
    assert result == False
