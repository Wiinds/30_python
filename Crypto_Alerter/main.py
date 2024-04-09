from crypto_data import get_coins, Coin



def alert(symbol: str, bottom: float, top: float, coins_list: list[Coin]):
    
    for coin in coins_list:
        if coin.symbol == symbol:
            if coin.current_price > top or coin.current_price < bottom:
                print(coin, 'Triggered')
            else:
                print(coin)



if __name__ == '__main__':
    coins: list[Coin] = get_coins()
    
    
    alert('BTC', bottom=63_000, top=72_000, coins_list=coins)
    alert('ETH', bottom=3_200, top=3_800, coins_list=coins)
    
    


