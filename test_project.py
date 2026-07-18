from project import validate_word, pick_random_target_word, get_letter_frequencies, get_colored_letters, color_text
from wordle_word_list import word_list
from color_constants import RED_TEXT, GREEN_TEXT, YELLOW_TEXT, RESET_COLOR

def test_validate_word():
    # test 5 lowercase letters
    assert validate_word("begin") == True
    # test 5 uppercase letters
    assert validate_word("BEGIN") == True
    # test 5 mixed letter
    assert validate_word("beGIN") == True
    # test input that's too short
    assert validate_word("a") == False
    # test input that's too long
    assert validate_word("a"*6) == False
    # test input containing digits
    assert validate_word("12345") == False
    # test non-alphanumeric characters
    assert validate_word(";;;;;") == False

def test_pick_random_target_word():
    # ensure target word is from valid list
    assert pick_random_target_word() in word_list
    # ensure selected word is exactly 5 letters
    assert validate_word(pick_random_target_word()) == True

def test_get_letter_frequencies():
    # test word frequency is captured
    assert get_letter_frequencies("ABCDE") == {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    # ensure multi-frequent letters
    assert get_letter_frequencies("AZZZB") == {'A': 1, 'B': 1, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 3}

def test_get_colored_letters():
    # ensure that later letters do not create false positive yellow characters
    assert get_colored_letters("KITTY", "YYYYY") == [(RED_TEXT,"Y"),(RED_TEXT,"Y"),(RED_TEXT,"Y"),(RED_TEXT,"Y"),(GREEN_TEXT,"Y")]
    # ensure full match are all green
    assert get_colored_letters("KITTY", "KITTY") == [(GREEN_TEXT,"K"),(GREEN_TEXT,"I"),(GREEN_TEXT,"T"),(GREEN_TEXT,"T"),(GREEN_TEXT,"Y")]
    # ensure entire mismatch is red
    assert get_colored_letters("KITTY", "AAAAA") == [(RED_TEXT,"A"),(RED_TEXT,"A"),(RED_TEXT,"A"),(RED_TEXT,"A"),(RED_TEXT,"A")]
    # ensure that mispositioned letters are yellow
    assert get_colored_letters("KITTY", "TTYKI") == [(YELLOW_TEXT,"T"),(YELLOW_TEXT,"T"),(YELLOW_TEXT,"Y"),(YELLOW_TEXT,"K"),(YELLOW_TEXT,"I")]
    # ensure all three cases can be labeled in the same word
    assert get_colored_letters("ABCDE", "ADBCZ") == [(GREEN_TEXT,"A"),(YELLOW_TEXT,"D"),(YELLOW_TEXT,"B"),(YELLOW_TEXT,"C"),(RED_TEXT,"Z")]

def test_color_text():
    assert color_text(GREEN_TEXT, "A") == f"{GREEN_TEXT}A{RESET_COLOR}"
    assert color_text(RED_TEXT, "A") == f"{RED_TEXT}A{RESET_COLOR}"
    assert color_text(YELLOW_TEXT, "A") == f"{YELLOW_TEXT}A{RESET_COLOR}"
