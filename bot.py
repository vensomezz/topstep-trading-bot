import requests
import time

class TopstepXTradingBot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.topstepx.com/v1/'

    def get_account_info(self):
        response = requests.get(f'{self.base_url}account', headers={'Authorization': f'Bearer {self.api_key}'})
        return response.json()

    def place_order(self, symbol, quantity, order_type='market'):
        order_data = {
            'symbol': symbol,
            'quantity': quantity,
            'order_type': order_type
        }
        response = requests.post(f'{self.base_url}orders', headers={'Authorization': f'Bearer {self.api_key}'}, json=order_data)
        return response.json()

    def trade_aapl(self):
        # Basic trading logic
        while True:
            account_info = self.get_account_info()
            if account_info['balance'] > 100:  # simple check for sufficient balance
                self.place_order('AAPL', 1)
                print('Placed order for AAPL')
            time.sleep(60)  # wait for a minute before checking again

if __name__ == '__main__':
    bot = TopstepXTradingBot(api_key='YOUR_API_KEY_HERE')
    bot.trade_aapl()