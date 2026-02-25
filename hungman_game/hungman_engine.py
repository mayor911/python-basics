from random import randint
import hungman_ascii_art as art


def set_word() -> str:
    mystery_words = ['cup', 'lap', 'ram', 'sam', 'hello','jello','mellow']
    mystery_word = mystery_words[randint(0, len(mystery_words)-1)]
    print("My guess is between:")
    for word in mystery_words:
        print(word, end='\t')
    print()
    return mystery_word

def show_blanks(word) -> str:
    print_word = ''
    for xter in word:
        print_word += '_'
    return print_word

def guess() -> chr:
    guessed_letter = input('Guess letter: ')[0]
    try:
        return guessed_letter
    except:
        print('Error occured while getting your letter')
        return guessed_letter

def times_letter_duplicates(word, letter) -> int:
    times_duplicated  = 0
    for xter in word:
        if xter == letter:
            times_duplicated += 1
    return times_duplicated

def add_letter(mystery_word, holder_word, guessed_letter) -> str:
    # check which letter we at incase of duplicate existence of letter in word
    occurence_in_word = times_letter_duplicates(mystery_word, guessed_letter)
    occurence_in_holder = times_letter_duplicates(holder_word, guessed_letter)
    if occurence_in_word == 0 or occurence_in_word == occurence_in_holder:
        return holder_word

            
    # now lets add the letter correctly
    new_holder_word = ''
    times_letter_found = 0
    for xter_index in range(0, len(mystery_word)):
        found_match = mystery_word[xter_index] == guessed_letter
        can_set_letter = occurence_in_holder == times_letter_found
        if found_match and can_set_letter:
            new_holder_word += guessed_letter
            times_letter_found += 1
        elif found_match and not can_set_letter:
            new_holder_word += holder_word[xter_index]
            times_letter_found += 1
        else:
            new_holder_word += holder_word[xter_index]

    return new_holder_word

def show_state(state) -> None:
    if state == 0:
        print(art.state0)
    elif state == 1:
        print(art.state1)
    elif state == 2:
        print(art.state2)
    elif state == 3:
        print(art.state3)
    elif state == 4:
        print(art.state4)
    elif state == 5:
        print(art.state5)
    else:
        print(art.state6)

def show_intro() -> None:
    print(f"""
    \tWelcome to Hungman game.
    This is an arcade mode.
    ***Guess the letters to save the hungman***
    """)
    
def run() -> None:
    show_intro()
    word = set_word()
    original_holder_word = show_blanks(word)
    state = 6
    while True:
        show_state(state)
        print(original_holder_word)
        letter = guess()
        holder_word = add_letter(word,original_holder_word,letter)
        if holder_word == original_holder_word:
            state -= 1
        original_holder_word = holder_word
        if state == 0:
            print("\t You loose")
            break
        elif holder_word == word and state < 6:
            print("\nYou win,(though the hungman is fucked up)You win!'\n")
            break
        elif holder_word == word and state == 6:
            print("\nYou's a fucking god in this game\n\tYou win!!\n")
            break
    print("\t\tBYE BYE!")
    print("\tThanks for playing")


if __name__ == '__main__':
    run()
