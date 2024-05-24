import json
import requests

api_key = 'D9FSHNEMC8Z5AWVR'


def get_news_sentiment(api_key, tickers=None, topics=None, time_from=None, time_to=None, sort='LATEST', limit=50):
    base_url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT'
    params = {
        'apikey': api_key,
        'tickers': tickers,
        'topics': topics,
        'time_from': time_from,
        'time_to': time_to,
        'sort': sort,
        'limit': limit
    }
    
    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}
    
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return json.dumps(response.json())
    else:
        return json.dumps({'error': f'Error {response.status_code}: {response.text}'})

