# Stock Price Checker

A clean CLI-based async stock price checker using Finnhub.

## Features
- Search company name -> possible stock symbols
- Clean CLI output
- Rate limiting between requests
- Reusable `aiohttp` session
- Modular folder structure
- Retry support
- 
## Run

```bash
pip install aiohttp
python main.py
```

## Project Structure

```text
stock_price_checker/
├── main.py
├── README.md
└── stock_checker/
    ├── __init__.py
    ├── api_client.py
    ├── cli.py
    ├── config.py
    ├── rate_limiter.py
    └── stock_service.py
```
