tools = [
    {
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
]