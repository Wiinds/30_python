from textblob import TextBlob
from dataclasses import dataclass

import sys

@dataclass
class Mood:
    emoji: str 
    sentiment: float 
    
    #@classmethod
    def get_mood(input_text: str, *, sensitivity: float) -> 'Mood':
        polarity: float = TextBlob(input_text).sentiment.polarity
        
        friendly_threshold: float = sensitivity
        hostile_threshold: float = -sensitivity
        
        if input_text == 'Exit'.lower():
            sys.exit()
        
        if polarity >= friendly_threshold:
            return Mood('😁', polarity)
        elif polarity <= hostile_threshold:
            return Mood('👿', polarity)
        else:
            return Mood('😐', polarity)
        
    #@staticmethod  
    def run_athena():
        print('Athena: Enter some test and i will perform a sentiment analysis on it')
        while True:
            user_input: str = input('You: ')
            mood: Mood = Mood.get_mood(user_input, sensitivity=0.7)
            print(f'Athena: {mood.emoji} ({mood.sentiment})')


if __name__ == '__main__':
    Mood.run_athena()





