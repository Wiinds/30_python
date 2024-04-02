import itertools
import string
import time


def common_guess(word: str) -> str | None:
    with open('words.txt', 'r') as words:
        word_list: list[str] = words.read().splitlines()
    
    for i, match in enumerate(word_list, start=1):
        if match == word:
            return f'Common Match: {match} (#{i})'
        

def brute_force(word: str, length: int, 
                digits: bool=False, symbols: bool=False) -> str | None:
    chars: str = string.ascii_lowercase
    
    if digits:
        chars += string.digits
        
    if symbols:
        chars += string.punctuation
        
    attempts: int = 0
    for guess in itertools.product(chars, repeat=length):
        attempts += 1
        guess: str = ''.join(guess)
        
        if guess == word:
            return f'"{word}" was cracked in {attempts:,} attempts'
        

def main():
    print('Searching...')
    password: str = 'acdc17'
    
    start_time: float = time.perf_counter()
    
    if common_match := common_guess(password):
        print(common_match)



if __name__ == "__main__":
    print(common_guess('caomch'))
