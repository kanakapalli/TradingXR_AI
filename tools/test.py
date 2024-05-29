from functions import *


def main():
    # Call create_post function to obtain API key
    api_key = create_post(occupation='Data Scientist', organization='ABC Corp', email='example@example.com')

    # Ensure that api_key is obtained before proceeding
    if api_key.startswith('Error'):
        print(api_key)
        return

    # Example usage of get_news_sentiment
    print("\nFetching news sentiment data for IBM...")
    news_sentiment_data = get_news_sentiment(api_key, tickers='IBM')
    print(news_sentiment_data)

    # Example usage of get_time_series_intraday
    print("\nFetching intraday data for IBM...")
    intraday_data = get_time_series_intraday(api_key, symbol='IBM', interval='5min')
    print(intraday_data)

    # Example usage of get_time_series_daily
    print("\nFetching daily time series data for IBM...")
    daily_data = get_time_series_daily(api_key, symbol='IBM')
    print(daily_data)

    # Example usage of get_time_series_daily_adjusted
    print("Fetching daily adjusted time series data for IBM...")
    daily_adjusted_data = get_time_series_daily_adjusted(api_key, symbol='IBM')
    print(daily_adjusted_data)

    # Example usage of get_time_series_weekly
    print("Fetching weekly time series data for IBM...")
    weekly_data = get_time_series_weekly(api_key, symbol='IBM')
    print(weekly_data)

    # Example usage of get_time_series_weekly_adjusted
    print("\nFetching weekly adjusted time series data for IBM...")
    weekly_adjusted_data = get_time_series_weekly_adjusted(api_key, symbol='IBM')
    print(weekly_adjusted_data)

    # Example usage of get_time_series_monthly
    print("Fetching monthly time series data for IBM...")
    monthly_data = get_time_series_monthly(api_key, symbol='IBM')
    print(monthly_data)

    # Example usage of get_time_series_monthly_adjusted
    print("Fetching monthly adjusted time series data for IBM...")
    monthly_adjusted_data = get_time_series_monthly_adjusted(api_key, symbol='IBM')
    print(monthly_adjusted_data)

    # Example usage of get_global_quote
    print("Fetching the latest price and volume information for IBM...")
    global_quote_data = get_global_quote(api_key, symbol='IBM')
    print(global_quote_data)

    # Example usage of symbol_search
    print("Searching for symbols and market information based on keywords...")
    search_results = symbol_search(api_key, keywords='tesco')
    print(search_results)

    # Example usage of market_status
    print("\nFetching the current market status...")
    status = market_status(api_key)
    print(status)


if __name__ == "__main__":
    main()
