# Wordle
### Video Demo: https://youtu.be/-g0Awkkawtc
### Description:
Wordle is a game where the player must attempt to guess a secret five-letter word.
The player has six attempts to guess the target word before they lose the game.
The player's guess words are limited to words with exactly five letters and must not contain digits nor non-alphanumeric characters.
Whenever players attempt to provide an invalid guess word, then that input is discarded, and the player is re-prompted.
After each of the player's guesses, they are rewarded with feedback based on the similarity of their proposed word relative to the secret target word.

Each round, the player proposes their guessed word and then this program responds by color coding the guessed word's letters.
<font color="green">Green letters</font> indicate that both the letter and that letter's position in the word are correct.
<font color="red">Red letters</font> indicate that the letter is not present inside the target word.
<font color="yellow">Yellow letters </font> indicate that the letter is present inside the target word, but it is at a different position.

If the player determines the target word within six attempts, then they win the game and are rewarded with the <font color="green">Congratulations You Win!</font> message.
Otherwise, the game displays the <font color="red">You Lose!</font> message and displays the target word.

### Project Files

---
#### color_constants.py
This file contains bindings for ANSI escape sequences to change terminal text to different colors and a sequence to stop printing in color.
These constants are used by the color_text() and build_color_word() functions, which embed the sequences in the formatted strings passed to Python's print() function.

#### wordle_word_list.py
This file contains a list that contains thousands of five-letter words.
Upon program startup, the main() function calls the pick_random_target_word() function, which uses the Python random module to randomly select a target word from the word list.

#### project.py
This file contains the core game logic.
The main() function prints player instructions to the terminal before launching the core game loop.
The game loop lasts until either the player runs out of their six attempts or successfully guesses the target word.
Each loop iteration reads the player's input and then validates that the input is a five-letter word by using a regular expression defined in the validate_word() function.
If the player's input is not a valid word, then the game skips back to the top of the loop and re-prompts the player.
No attempts are consumed during a re-prompt.
Whenever the guess word does not match the target word, then the get_colored_letters() and build_color_word() functions are used to construct a string with colored text. The letter colors match the specifications defined in the description above.

One important consideration for the get_colored_letters() function was the best way to avoid prematurely labeling <font color="yellow">yellow letters</font> before all letters had been verified. For example, consider that the target word is "KITTY" and the player guesses "YYYYY".
If all the game does is loop through the guess letters in order, then the letters will be incorrectly colored as
 <font color="yellow">Y</font><font color="red">Y</font><font color="red">Y</font><font color="red">Y</font><font color="green">Y</font> despite the fact that "KITTY" only has one Y in it.
 The correct result should be <font color="red">Y</font><font color="red">Y</font><font color="red">Y</font><font color="red">Y</font><font color="green">Y</font>, so that the player understands that the target word only contains a single Y.
 This is due to the fact that a single loop would identify the first Y as a target word member before reaching the correctly placed Y at the end. I solved this issue by creating the get_letter_frequencies() function.
 It returns a Python dictionary that models the letter frequency of the target word.
 Now the get_colored_letters() function loops through the guess word twice.
 The first time is to check for <font color="green">green letter</font> matches, since they should receive priority.
 Each time a <font color="green">green match</font> is found, then the loop decrements the frequency for that specific letter.
 That way, during the second pass through the guess word, before a letter is marked <font color="yellow">yellow</font>, the game must check to see if there are any remaining unmatched letters in order to avoid counting them twice.

#### test_project.py
This file contains the Python unit tests for the following functions from the project.py file:
- validate_word()
- pick_random_target_word()
- get_letter_frequencies()
- get_colored_letters()
- color_text()
