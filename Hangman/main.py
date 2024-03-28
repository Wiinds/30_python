from random import choice


def run_game():
    word: str = choice(['apple', 'pear', 'pineapple', 'banana'])
    username: str  = input('Hello, what is your name? >> ')
    print(f'Welcome to hangman, {username}. You have 5 attempts to guess the word.')
    
    guessed: str = ''
    tries: int = 5
    
    while tries > 0:
        blanks: int = 0
        
        print('Word: ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1

        #*adds a blank line 
        print()
        
        if blanks == 0:
            print('Good job, you got it right!')
            break
        
        guess: str = input('Enter a letter: ').strip()
        
        if guess.lower() == 'exit':
                print("Thanks for playing! ")
                break
        
        if len(guess) != 1 or not guess.isalpha():  #* Check for single alphabetic character
            print("Please enter only a single letter or try guessing the entire word.")
            continue
        
        
        if len(guess) == len(word) and guess.isalpha():  #* Attempt to guess the entire word
            if guess.lower() == word:
                print('Wow! You guessed the entire word correctly!')
                break
            else:
                print(f'Oops, "{guess}" is not the word... ({attempts-1} attempts remaining)')
                attempts -= 1
                continue
        
        if guess in guessed:
            print(f'You have already used: {guess}. Try another letter')
            continue
        
        guessed += guess
        
        if guess not in word:
            tries -= 1
            print(f'Sorry, that was wrong... ({tries} attempts remaining)')
            
            if tries == 5:
                print('You have used all your attempts... Game Over')
                break


if __name__ == "__main__":
    run_game()
