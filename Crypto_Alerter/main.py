from crypto_data import get_coins, Coin

def alert(symbol: str, bottom: float, top: float, coins_list: list[Coin]):
    
    for coin in coins_list:
        if coin.symbol == symbol:
            if coin.current_price > top:
                print(f'{coin}, Above Set Alert price!')
            elif coin.current_price < bottom:
                print(f'{coin}, Under Set Alert price!')
            else:
                print(coin)



if __name__ == '__main__':
    coins: list[Coin] = get_coins()
    
    
    alert('btc', bottom=63000, top=67000, coins_list=coins)
    alert('eth', bottom=3200, top=3500, coins_list=coins)
    alert('sol', bottom=145, top=170, coins_list=coins)
    
    


