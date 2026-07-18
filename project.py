from wordle_word_list import word_list
from re import fullmatch
from random import choice
from string import ascii_uppercase
from color_constants import RED_TEXT, GREEN_TEXT, YELLOW_TEXT, RESET_COLOR

def main():
    print("Welcome to Worlde!")
    print("Your objective is to guess a secret five letter word within six attempts.")
    print("After each of your guesses, I will color-code the letters from your guess.")
    print(f"{color_text(GREEN_TEXT, "A GREEN letter")} means that both the {color_text(GREEN_TEXT, "letter")} and its {color_text(GREEN_TEXT, "position")} are {color_text(GREEN_TEXT, "correct")}.")
    print(f"{color_text(RED_TEXT, "A RED letter")} means that the {color_text(RED_TEXT, "letter is not present")} in the target word.")
    print(f"{color_text(YELLOW_TEXT, "A YELLOW letter")} means that the {color_text(GREEN_TEXT, "letter is present inside the target word")}, but its {color_text(RED_TEXT, "position is incorrect")}.")
    print(f"Each guess must be a word of {color_text(YELLOW_TEXT, "EXACTLY 5 LETTERS")}.")
    print("Any input containing non-letters or a different length will cause a re-prompt.\n")

    remaining_guesses = 6
    won_game = False
    target_word = pick_random_target_word().upper()

    while remaining_guesses > 0:
        guess = input("Enter guess: ").upper().strip()
        if not validate_word(guess):
            continue # re-prompt user
        if guess == target_word:
            won_game = True
            break
        else:
            remaining_guesses -= 1
            print(f"{build_color_word(get_colored_letters(target_word, guess))}")

    if won_game:
        print(f"{color_text(GREEN_TEXT, "Congratulations You Win!")}")
    else:
        print(f"{color_text(RED_TEXT, f"You Lose!\nThe answer was {target_word}")}")

def validate_word(guess):
    regex = r"^[A-Z]{5}$"
    return bool(fullmatch(regex, guess.upper()))

def pick_random_target_word():
    return choice(word_list)

def get_letter_frequencies(word):
    letters = list(ascii_uppercase)
    letter_freq = dict(zip(letters, [0]*len(letters)))
    for letter in word:
        letter_freq[letter] += 1
    return letter_freq

def get_colored_letters(target_word, guess_word):
    color_with_letter_pairs = []
    letter_freq = get_letter_frequencies(target_word)
    # First, reduce the dictionary frequencies by the number of matches
    # This will prevent false positively labeling characters yellow
    for i in range(len(target_word)):
        target_letter = target_word[i]
        guess_letter = guess_word[i]
        if target_letter == guess_letter:
            letter_freq[target_letter] -= 1
    # Now collect the correct colors per match/non-match
    for i in range(len(target_word)):
        target_letter = target_word[i]
        guess_letter = guess_word[i]
        if target_letter == guess_letter:
            color_with_letter_pairs.append((GREEN_TEXT, guess_letter))
        elif letter_freq[guess_letter] > 0:
            color_with_letter_pairs.append((YELLOW_TEXT, guess_letter))
            letter_freq[guess_letter] -= 1
        else:
            color_with_letter_pairs.append((RED_TEXT, guess_letter))
    return color_with_letter_pairs

def color_text(color, text):
    return f"{color}{text}{RESET_COLOR}"

def build_color_word(color_with_letter_pairs):
    word = ""
    for color, letter in color_with_letter_pairs:
        word += color_text(color, letter)
    return word

if __name__ == "__main__":
    main()
