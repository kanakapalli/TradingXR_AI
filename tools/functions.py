import json
import requests

api_key = '9Z761MFGD9LS3BWQ'


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
    # desc - get_news_sentiment_description


get_news_sentiment_description = {
    "type": "function",
    "function": {
        "name": "get_news_sentiment",
        "description": "Fetch news sentiment data from Alpha Vantage",
        "parameters": {
            "type": "object",
            "properties": {
                "tickers": {
                    "type": "string",
                    "description": "The stock/crypto/forex symbols to filter news by",
                },
                "topics": {
                    "type": "string",
                    "description": "The news topics to filter by",
                },
                "time_from": {
                    "type": "string",
                    "description": "The start time for the news articles in YYYYMMDDTHHMM format",
                },
                "time_to": {
                    "type": "string",
                    "description": "The end time for the news articles in YYYYMMDDTHHMM format",
                },
                "sort": {
                    "type": "string",
                    "description": "The sorting order of the results (LATEST, EARLIEST, RELEVANCE)",
                    "default": "LATEST"
                },
                "limit": {
                    "type": "integer",
                    "description": "The maximum number of results to return",
                    "default": 50
                },
            },
            "required": ["tickers"],
        },
    },
}


# func def - get_time_series_intraday
def get_time_series_intraday(api_key, symbol, interval, adjusted=True, extended_hours=True, month=None,
                             outputsize='compact', datatype='json'):
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': interval,
        'adjusted': 'true' if adjusted else 'false',
        'extended_hours': 'true' if extended_hours else 'false',
        'outputsize': outputsize,
        'datatype': datatype,
        'apikey': api_key
    }
    if month:
        params['month'] = month

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return json.dumps(response.json())
    else:
        return json.dumps({'error': f'Error {response.status_code}: {response.text}'})


# desc - get_time_series_intraday
time_series_intraday_description = {
    "type": "function",
    "function": {
        "name": "get_time_series_intraday",
        "description": "Fetches current and historical intraday OHLCV time series data of the specified equity.",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "description": "The name of the equity for which to retrieve intraday data. Example: symbol=IBM"
                },
                "interval": {
                    "type": "string",
                    "description": "Time interval between two consecutive data points in the time series. Supported values: 1min, 5min, 15min, 30min, 60min"
                },
                "adjusted": {
                    "type": "boolean",
                    "description": "Specifies whether the output time series is adjusted by historical split and dividend events. Default: true"
                },
                "extended_hours": {
                    "type": "boolean",
                    "description": "Specifies whether to include both regular trading hours and extended trading hours in the output time series. Default: true"
                },
                "month": {
                    "type": "string",
                    "description": "Specifies a specific month in history (YYYY-MM format) from which to retrieve intraday data. Default: None"
                },
                "outputsize": {
                    "type": "string",
                    "description": "Specifies the size of the output data. Options: compact (latest 100 data points), full (full intraday data for a specific month). Default: compact"
                },
                "datatype": {
                    "type": "string",
                    "description": "Specifies the format of the output data. Options: json, csv. Default: json"
                }
            },
            "required": ["symbol", "interval", "apikey"]
        }
    }
}


# func def - get_time_series_daily
def get_time_series_daily(api_key, symbol, outputsize='compact', datatype='json'):
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': api_key,
        'outputsize': outputsize,
        'datatype': datatype
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return json.dumps(response.json())
    else:
        return json.dumps({'error': f'Error {response.status_code}: {response.text}'})


# desc - get_time_series_daily
get_time_series_daily_description = {
    "type": "function",
    "function": {
        "name": "get_time_series_daily",
        "description": "Fetch daily time series data for a specified equity from Alpha Vantage",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "description": "The name of the equity of your choice. For example: symbol=IBM",
                },
                "outputsize": {
                    "type": "string",
                    "description": "Data size of each API call. Options: compact, full. Default is compact.",
                    "default": "compact"
                },
                "datatype": {
                    "type": "string",
                    "description": "Format of the output data. Options: json, csv. Default is json.",
                    "default": "json"
                }
            },
            "required": ["symbol"],
        },
    },
}


# func def - get_time_series_daily_adjusted
def get_time_series_daily_adjusted(api_key, symbol, outputsize='compact', datatype='json'):
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': symbol,
        'apikey': api_key,
        'outputsize': outputsize,
        'datatype': datatype
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return json.dumps(response.json())
    else:
        return json.dumps({'error': f'Error {response.status_code}: {response.text}'})


# desc - get_time_series_daily_adjusted
get_time_series_daily_adjusted_description = {
    "type": "function",
    "function": {
        "name": "get_time_series_daily_adjusted",
        "description": "Fetch daily adjusted time series data for a specified equity from Alpha Vantage",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "description": "The name of the equity of your choice. For example: symbol=IBM",
                },
                "outputsize": {
                    "type": "string",
                    "description": "Data size of each API call. Options: compact, full. Default is compact.",
                    "default": "compact"
                },
                "datatype": {
                    "type": "string",
                    "description": "Format of the output data. Options: json, csv. Default is json.",
                    "default": "json"
                }
            },
            "required": ["symbol"],
        },
    },
}


# func def - get_time_series_weekly
def get_time_series_weekly(api_key, symbol, datatype='json'):
    """
    Fetch weekly time series data for a specified equity from Alpha Vantage.

    Parameters:
        api_key (str): Your Alpha Vantage API key.
        symbol (str): The name of the equity of your choice. For example: symbol=IBM.
        datatype (str, optional): Format of the output data. Options: json, csv. Default is json.

    Returns:
        str: JSON string containing the weekly time series data.

    Example:
        # Fetch weekly data for IBM
        weekly_data = get_time_series_weekly(api_key='YOUR_API_KEY', symbol='IBM')
    """
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_WEEKLY',
        'symbol': symbol,
        'apikey': api_key,
        'datatype': datatype
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return json.dumps(response.json())
    else:
        return json.dumps({'error': f'Error {response.status_code}: {response.text}'})


# desc - get_time_series_weekly
get_time_series_weekly_description = {
    "type": "function",
    "function": {
        "name": "get_time_series_weekly",
        "description": "Fetch weekly time series data for a specified equity from Alpha Vantage",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "description": "The name of the equity of your choice. For example: symbol=IBM",
                },
                "datatype": {
                    "type": "string",
                    "description": "Format of the output data. Options: json, csv. Default is json.",
                    "default": "json"
                }
            },
            "required": ["symbol"],
        },
    },
}


# func def - get_time_series_weekly_adjusted
def get_time_series_weekly_adjusted(api_key, symbol, datatype='json'):
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_WEEKLY_ADJUSTED',
        'symbol': symbol,
        'apikey': api_key,
        'datatype': datatype
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return json.dumps(response.json())
    else:
        return json.dumps({'error': f'Error {response.status_code}: {response.text}'})


# desc - get_time_series_weekly_adjusted
get_time_series_weekly_adjusted_description = {
    "type": "function",
    "function": {
        "name": "get_time_series_weekly_adjusted",
        "description": "Fetch weekly adjusted time series data for a specified equity from Alpha Vantage",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "description": "The name of the equity of your choice. For example: symbol=IBM",
                },
                "datatype": {
                    "type": "string",
                    "description": "Format of the output data. Options: json, csv. Default is json.",
                    "default": "json"
                }
            },
            "required": ["symbol"],
        },
    },
}


# func def - get_time_series_monthly
def get_time_series_monthly(api_key, symbol, datatype='json'):
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_MONTHLY',
        'symbol': symbol,
        'apikey': api_key,
        'datatype': datatype
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return json.dumps(response.json())
    else:
        return json.dumps({'error': f'Error {response.status_code}: {response.text}'})


# desc - get_time_series_monthly
get_time_series_monthly_description = {
    "type": "function",
    "function": {
        "name": "get_time_series_monthly",
        "description": "Fetch monthly time series data for a specified equity from Alpha Vantage",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "description": "The name of the equity of your choice. For example: symbol=IBM",
                },
                "datatype": {
                    "type": "string",
                    "description": "Format of the output data. Options: json, csv. Default is json.",
                    "default": "json"
                }
            },
            "required": ["symbol"],
        },
    },
}


# func def - get_time_series_monthly_adjusted
def get_time_series_monthly_adjusted(api_key, symbol, datatype='json'):
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_MONTHLY_ADJUSTED',
        'symbol': symbol,
        'apikey': api_key,
        'datatype': datatype
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return json.dumps(response.json())
    else:
        return json.dumps({'error': f'Error {response.status_code}: {response.text}'})


# desc - get_time_series_monthly_adjusted
get_time_series_monthly_adjusted_description = {
    "type": "function",
    "function": {
        "name": "get_time_series_monthly_adjusted",
        "description": "Fetch monthly adjusted time series data for a specified equity from Alpha Vantage",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "description": "The name of the equity of your choice. For example: symbol=IBM",
                },
                "datatype": {
                    "type": "string",
                    "description": "Format of the output data. Options: json, csv. Default is json.",
                    "default": "json"
                }
            },
            "required": ["symbol"],
        },
    },
}


# func def - get_global_quote
def get_global_quote(api_key, symbol, datatype='json'):
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': api_key,
        'datatype': datatype
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return json.dumps(response.json())
    else:
        return json.dumps({'error': f'Error {response.status_code}: {response.text}'})


# desc - get_global_quote
get_global_quote_description = {
    "type": "function",
    "function": {
        "name": "get_global_quote",
        "description": "Fetch the latest price and volume information for a ticker of your choice from Alpha Vantage",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "description": "The symbol of the global ticker of your choice. For example: symbol=IBM",
                },
                "datatype": {
                    "type": "string",
                    "description": "Format of the output data. Options: json, csv. Default is json.",
                    "default": "json"
                }
            },
            "required": ["symbol"],
        },
    },
}


# func def - symbol_search
def symbol_search(api_key, keywords, datatype='json'):
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'SYMBOL_SEARCH',
        'keywords': keywords,
        'apikey': api_key,
        'datatype': datatype
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return json.dumps(response.json())
    else:
        return json.dumps({'error': f'Error {response.status_code}: {response.text}'})


# desc - symbol_search
symbol_search_description = {
    "type": "function",
    "function": {
        "name": "symbol_search",
        "description": "Search for symbols and market information based on keywords of your choice using Alpha Vantage's Search Endpoint",
        "parameters": {
            "type": "object",
            "properties": {
                "keywords": {
                    "type": "string",
                    "description": "A text string of your choice. For example: keywords=microsoft.",
                },
                "datatype": {
                    "type": "string",
                    "description": "Format of the output data. Options: json, csv. Default is json.",
                    "default": "json"
                }
            },
            "required": ["keywords"],
        },
    },
}


# func def - market_status
def market_status(api_key):
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'MARKET_STATUS',
        'apikey': api_key
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return json.dumps(response.json())
    else:
        return json.dumps({'error': f'Error {response.status_code}: {response.text}'})


# desc - market_status
market_status_description = {
    "type": "function",
    "function": {
        "name": "market_status",
        "description": "Get the current market status (open vs. closed) of major trading venues for equities, forex, and cryptocurrencies around the world",
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },
}


def create_post(occupation, organization, email):
    url = 'https://www.alphavantage.co/create_post/'
    form_data = {
        'occupation_text': occupation,
        'organization_text': organization,
        'email_text': email
    }

    response = requests.post(url, data=form_data)

    if response.status_code == 200:
        response_json = response.json()
        api_key = response_json.get('text').split('API key: ')[1].split('. ')[0]
        print(f"response.json --- >>> {response_json}")
        print(f"response.json api key --- >>> {api_key}")
        return api_key
    else:
        return f'Error {response.status_code}: {response.text}'


