from random import randint, choice
from datetime import datetime 
from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def index():
    phrase: list[str] = ["Welcome to the home page", "The Weather is nice today", "keep grinding your time is coming"]
    return {'phrase': choice(phrase),
            'date': datetime.now()}
    

@app.route('/api/random')
def random():
    number_input = request.args.get('number', type=int)
    text_input = request.args.get('text', type=str, default='default_text')
    
    if isinstance(number_input, int):
        return{'input': number_input,
               'random': randint(0, number_input),
               'text': text_input,
               'date': datetime.now()}
    else:
        return {'Error': 'Please eneter a number.'}


if __name__ == '__main__':
    app.run()




