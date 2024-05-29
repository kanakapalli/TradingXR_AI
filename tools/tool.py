import importlib

import functions

module = importlib.import_module('functions')


tools = [
    functions.get_news_sentiment_description,
    functions.get_time_series_daily_description,
    functions.get_time_series_daily_adjusted_description,
    
    
]